import google.generativeai as genai
import json
from django.conf import settings
from django.db.models import Avg, Count
from accounts.models import HoSoBacSi, ChuyenKhoa
from appointments.models import LichLamViec
from .models import TrieuChungAnalysis, BacSiRecommendation
from datetime import datetime, timedelta


class OpenAIService:
    """Service để tương tác với Google Gemini API"""
    
    def __init__(self):
        # Lấy API key từ settings
        self.api_key = getattr(settings, 'GEMINI_API_KEY', '')
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-pro')
            self.use_real_ai = True
        else:
            self.use_real_ai = False
    
    def chat_with_gpt(self, message, context=None):
        """Chat với Gemini để hỗ trợ tổng quát"""
        
        if not self.use_real_ai:
            return self._fallback_chat_response(message)
        
        try:
            system_prompt = """Bạn là trợ lý AI y tế thông minh của phòng khám. 
Nhiệm vụ của bạn:
1. Trò chuyện thân thiện, tự nhiên với bệnh nhân
2. Hỏi thêm thông tin về triệu chứng nếu cần
3. Giải đáp thắc mắc về sức khỏe
4. Hướng dẫn quy trình đặt lịch khám
5. Trả lời ngắn gọn, dễ hiểu (tối đa 3-4 câu)

Lưu ý: Không tự ý chẩn đoán bệnh, chỉ gợi ý nên khám chuyên khoa nào."""

            if context:
                system_prompt += f"\n\nThông tin ngữ cảnh: {context}"
            
            full_prompt = f"{system_prompt}\n\nCâu hỏi của bệnh nhân: {message}"
            
            response = self.model.generate_content(full_prompt)
            return response.text.strip()
            
        except Exception as e:
            print(f"Gemini Error: {e}")
            return self._fallback_chat_response(message)
    
    def _fallback_chat_response(self, message):
        """Phản hồi dự phòng khi không có Gemini"""
        message_lower = message.lower()
        
        # Các câu trả lời mẫu
        if any(word in message_lower for word in ['xin chào', 'chào', 'hello', 'hi']):
            return "Xin chào! Tôi là trợ lý AI của phòng khám. Bạn có triệu chứng gì cần tư vấn không?"
        
        elif any(word in message_lower for word in ['cảm ơn', 'thanks', 'thank']):
            return "Rất vui được hỗ trợ bạn! Nếu cần thêm thông tin gì, đừng ngần ngại hỏi nhé."
        
        elif any(word in message_lower for word in ['giá', 'phí', 'chi phí', 'tiền']):
            return "Phí khám tùy thuộc vào bác sĩ và chuyên khoa, thường từ 150,000 - 450,000 VNĐ. Bạn có thể xem chi tiết khi chọn bác sĩ."
        
        elif any(word in message_lower for word in ['lịch', 'giờ', 'thời gian']):
            return "Phòng khám mở cửa từ 8:00 - 17:30 các ngày trong tuần. Bạn có thể đặt lịch trước để được ưu tiên."
        
        else:
            return "Tôi đã hiểu. Để tôi giúp bạn tốt hơn, bạn có thể mô tả chi tiết hơn về triệu chứng không?"
    
    def analyze_symptoms(self, symptoms_text):
        """Phân tích triệu chứng và đề xuất chuyên khoa - Ưu tiên keyword trước"""
        
        # Kiểm tra đơn giản trước khi gọi AI
        symptoms_lower = symptoms_text.lower().strip()
        
        # Danh sách từ không phải triệu chứng (mở rộng)
        non_symptom_words = [
            'hello', 'hi', 'xin chào', 'chào', 'hey', 'yo', 'halo',
            'xin chào bạn', 'chào bạn', 'hi there', 'hey there',
            'cảm ơn', 'thanks', 'thank you', 'bye', 'tạm biệt',
            'ok', 'okay', 'oke', 'uhm', 'ừ', 'à', 'ơ', 'hm', 'hmm',
            'test', 'testing', 'thử', 'kiểm tra'
        ]
        
        # Kiểm tra exact match và substring match
        if (symptoms_lower in non_symptom_words or 
            any(word in symptoms_lower for word in ['hello', 'hi', 'chào', 'xin chào']) or
            len(symptoms_text.strip()) < 3):
            return {
                "is_valid": False,
                "message": "Vui lòng mô tả triệu chứng sức khỏe của bạn (ví dụ: đau đầu, sốt, ho, đau bụng, ngứa da...)",
                "reason": "Input không phải mô tả triệu chứng"
            }
        
        # Kiểm tra nếu chỉ là số
        if symptoms_text.strip().isdigit():
            return {
                "is_valid": False,
                "message": "Vui lòng mô tả triệu chứng bằng chữ, không phải số (ví dụ: đau đầu, sốt, ho...)",
                "reason": "Input chỉ chứa số"
            }
        
        # Kiểm tra nếu chỉ là emoji hoặc ký tự đặc biệt
        import re
        if re.match(r'^[^\w\s]+$', symptoms_text.strip(), re.UNICODE):
            return {
                "is_valid": False,
                "message": "Vui lòng mô tả triệu chứng bằng từ ngữ rõ ràng (ví dụ: đau đầu, sốt, ho...)",
                "reason": "Input chỉ chứa ký tự đặc biệt"
            }
        
        # Kiểm tra URL hoặc code
        if any(pattern in symptoms_lower for pattern in ['http://', 'https://', 'www.', '<?', '<script', 'function']):
            return {
                "is_valid": False,
                "message": "Vui lòng mô tả triệu chứng sức khỏe, không phải URL hay code",
                "reason": "Input chứa URL hoặc code"
            }
        
        # Lấy danh sách chuyên khoa hiện có
        chuyen_khoa_list = list(ChuyenKhoa.objects.values_list('ten', flat=True))
        
        # BƯỚC 1: Thử phân tích bằng keyword trước
        print(f"🔍 [DEBUG] Trying keyword analysis first for: {symptoms_text}")
        keyword_result = self._analyze_with_keywords(symptoms_text, chuyen_khoa_list)
        
        # Kiểm tra xem keyword analysis có tìm thấy match tốt không
        if keyword_result.get('do_tin_cay', 0) >= 70:  # Nếu confidence >= 70%
            print(f"✅ [DEBUG] Keyword analysis successful with confidence: {keyword_result.get('do_tin_cay')}%")
            keyword_result['is_valid'] = True
            keyword_result['analysis_method'] = 'keyword'
            return keyword_result
        
        # BƯỚC 2: Nếu keyword không đủ tin cậy, thử AI
        if self.use_real_ai:
            print(f"🤖 [DEBUG] Keyword confidence too low ({keyword_result.get('do_tin_cay')}%), trying AI...")
            ai_result = self._analyze_with_gemini(symptoms_text, chuyen_khoa_list)
            if ai_result.get('is_valid', True):  # Nếu AI thành công
                ai_result['analysis_method'] = 'ai'
                return ai_result
            else:
                print(f"❌ [DEBUG] AI analysis failed, falling back to keyword result")
        
        # BƯỚC 3: Fallback về keyword result (dù confidence thấp)
        print(f"📝 [DEBUG] Using keyword analysis as final result")
        keyword_result['is_valid'] = True
        keyword_result['analysis_method'] = 'keyword_fallback'
        return keyword_result

    def _get_possible_diseases(self, specialty, matched_keywords):
        """Gợi ý bệnh có thể dựa trên chuyên khoa và từ khóa"""
        
        disease_mapping = {
            'tim mạch': [
                'Tăng huyết áp', 'Bệnh mạch vành', 'Rối loạn nhịp tim', 
                'Suy tim', 'Bệnh van tim', 'Đau thắt ngực'
            ],
            'nội khoa': [
                'Cảm cúm', 'Viêm đường hô hấp', 'Tăng huyết áp', 
                'Tiểu đường', 'Rối loạn tiêu hóa', 'Stress, lo âu'
            ],
            'ngoại khoa': [
                'Chấn thương', 'Gãy xương', 'Bong gân', 
                'U lành tính', 'Viêm ruột thừa', 'Thoát vị'
            ],
            'da liễu': [
                'Viêm da cơ địa', 'Dị ứng da', 'Nấm da', 
                'Mụn trứng cá', 'Vảy nến', 'Zona'
            ],
            'tai mũi họng': [
                'Viêm họng', 'Viêm amidan', 'Viêm xoang', 
                'Viêm tai giữa', 'Polyp mũi', 'Viêm thanh quản'
            ],
            'mắt': [
                'Viêm kết mạc', 'Khô mắt', 'Cận thị', 
                'Tăng nhãn áp', 'Đục thủy tinh thể', 'Lác mắt'
            ],
            'răng hàm mặt': [
                'Sâu răng', 'Viêm nướu', 'Áp xe răng', 
                'Tụt nướu', 'Viêm tủy răng', 'Mọc răng khôn'
            ],
            'thần kinh': [
                'Đau nửa đầu', 'Rối loạn giấc ngủ', 'Đau dây thần kinh', 
                'Tai biến mạch máu não', 'Parkinson', 'Động kinh'
            ],
            'tiêu hóa': [
                'Viêm dạ dày', 'Loét dạ dày', 'Hội chứng ruột kích thích', 
                'Viêm đại tràng', 'Trào ngược dạ dày', 'Viêm gan'
            ],
            'sản phụ khoa': [
                'Rối loạn kinh nguyệt', 'Viêm phụ khoa', 'U xơ tử cung', 
                'Nang buồng trứng', 'Vô sinh hiếm muộn', 'Tiền mãn kinh'
            ],
            'cơ xương khớp': [
                'Thoái hóa khớp', 'Viêm khớp dạng thấp', 'Gout', 
                'Thoát vị đĩa đệm', 'Loãng xương', 'Viêm gân'
            ],
            'nhi khoa': [
                'Sốt virus', 'Tiêu chảy cấp', 'Viêm đường hô hấp', 
                'Suy dinh dưỡng', 'Chậm phát triển', 'Dị ứng thức ăn'
            ]
        }
        
        return disease_mapping.get(specialty, ['Cần khám để xác định chính xác'])
    
    def _analyze_with_gemini(self, symptoms_text, chuyen_khoa_list):
        """Phân tích bằng Gemini"""
        
        print(f"🔍 [DEBUG] Starting Gemini analysis for: {symptoms_text}")
        print(f"🔍 [DEBUG] API Key exists: {bool(self.api_key)}")
        print(f"🔍 [DEBUG] Use real AI: {self.use_real_ai}")
        
        # Bước 1: Kiểm tra xem input có phải triệu chứng hợp lệ không
        validation_prompt = f"""Bạn là bác sĩ AI. Kiểm tra xem đoạn text sau có phải là MÔ TẢ TRIỆU CHỨNG SỨC KHỎE hợp lệ không:

Text: "{symptoms_text}"

Trả về JSON (KHÔNG thêm markdown):
{{
    "is_valid_symptom": true/false,
    "reason": "lý do ngắn gọn",
    "suggestion": "gợi ý nếu không hợp lệ"
}}

Tiêu chí hợp lệ:
- Mô tả cảm giác, triệu chứng cơ thể (đau, ngứa, sốt, ho, chóng mặt...)
- Có ít nhất 2-3 từ có nghĩa
- KHÔNG phải: số, ký tự vô nghĩa, câu hỏi chung chung, lời chào (hello, hi, xin chào)

CHỈ trả về JSON thuần."""

        try:
            print(f"🔍 [DEBUG] Calling Gemini for validation...")
            # Validate input với timeout
            validation_response = self.model.generate_content(validation_prompt)
            
            # Xử lý response text an toàn hơn
            validation_text = validation_response.text.strip()
            
            # Loại bỏ tất cả markdown code blocks
            import re
            validation_text = re.sub(r'```(?:json)?\s*', '', validation_text)
            validation_text = re.sub(r'\s*```', '', validation_text)
            validation_text = validation_text.strip()
            
            print(f"🔍 [DEBUG] Cleaned validation response: {validation_text}")
            
            try:
                validation_result = json.loads(validation_text)
            except json.JSONDecodeError as je:
                print(f"❌ [DEBUG] JSON decode error: {je}")
                print(f"❌ [DEBUG] Raw text: {repr(validation_text)}")
                # Fallback về simple validation
                raise Exception("JSON parsing failed")
            
            # Nếu không phải triệu chứng hợp lệ, trả về lỗi
            if not validation_result.get('is_valid_symptom', False):
                print(f"❌ [DEBUG] Validation failed: {validation_result.get('reason')}")
                return {
                    "is_valid": False,
                    "message": validation_result.get('suggestion', 'Vui lòng mô tả triệu chứng cụ thể hơn (ví dụ: đau đầu, sốt, ho, đau bụng...)'),
                    "reason": validation_result.get('reason', 'Input không phải triệu chứng')
                }
            
            print(f"✅ [DEBUG] Validation passed, proceeding to analysis...")
            
        except Exception as e:
            print(f"❌ [DEBUG] Validation Error: {type(e).__name__}: {str(e)}")
            import traceback
            traceback.print_exc()
            
            # Nếu lỗi validation, kiểm tra đơn giản mạnh hơn
            simple_checks = [
                len(symptoms_text.strip()) < 3,
                symptoms_text.strip().isdigit(),
                any(word in symptoms_text.lower() for word in ['hello', 'hi', 'chào', 'xin chào', 'hey']),
                not any(char.isalpha() for char in symptoms_text)  # Không có chữ cái
            ]
            
            if any(simple_checks):
                return {
                    "is_valid": False,
                    "message": "Vui lòng mô tả triệu chứng cụ thể hơn (ví dụ: đau đầu, sốt, ho, đau bụng...)",
                    "reason": "Input không hợp lệ hoặc lỗi API"
                }
            
            # Nếu lỗi API nhưng input có vẻ hợp lệ, fallback về keyword analysis
            print(f"⚠️ [DEBUG] Falling back to keyword analysis due to API error")
            return self._analyze_with_keywords(symptoms_text, chuyen_khoa_list)
        
        # Bước 2: Phân tích triệu chứng hợp lệ
        prompt = f"""Bạn là bác sĩ AI chuyên nghiệp. Phân tích triệu chứng sau và đề xuất chuyên khoa phù hợp:

Triệu chứng: {symptoms_text}

Danh sách chuyên khoa có sẵn: {', '.join(chuyen_khoa_list)}

Trả về JSON với format chính xác (KHÔNG thêm markdown, chỉ JSON thuần):
{{
    "is_valid": true,
    "chuyen_khoa_de_xuat": "tên chuyên khoa từ danh sách trên",
    "do_tin_cay": số từ 0-100,
    "phan_tich": {{
        "trieu_chung_chinh": ["triệu chứng 1", "triệu chứng 2"],
        "benh_co_the": ["bệnh có thể 1", "bệnh có thể 2"],
        "ly_do_chon_chuyen_khoa": "lý do chi tiết",
        "luu_y": "lưu ý quan trọng"
    }}
}}

CHỈ trả về JSON, không thêm text khác."""

        try:
            response = self.model.generate_content(prompt)
            result_text = response.text.strip()
            
            # Loại bỏ markdown code block nếu có
            result_text = result_text.replace('```json', '').replace('```', '').strip()
            result = json.loads(result_text)
            
            # Validate chuyên khoa có trong danh sách
            if result['chuyen_khoa_de_xuat'] not in chuyen_khoa_list:
                # Tìm chuyên khoa gần nhất
                for ck in chuyen_khoa_list:
                    if ck.lower() in result['chuyen_khoa_de_xuat'].lower():
                        result['chuyen_khoa_de_xuat'] = ck
                        break
                else:
                    result['chuyen_khoa_de_xuat'] = 'Nội khoa'  # Fallback
            
            result['is_valid'] = True
            return result
            
        except Exception as e:
            print(f"Gemini Analysis Error: {e}")
            return self._analyze_with_keywords(symptoms_text, chuyen_khoa_list)
    
    def _analyze_with_keywords(self, symptoms_text, chuyen_khoa_list):
        """Phân tích nhanh dựa trên từ khóa - Mở rộng từ khóa bệnh"""
        
        symptoms_lower = symptoms_text.lower()
        
        # Mapping từ khóa với chuyên khoa (mở rộng đáng kể)
        specialty_keywords = {
            'tim mạch': [
                'tim', 'ngực', 'đau ngực', 'khó thở', 'huyết áp', 'mạch', 'tim đập',
                'đau tim', 'hồi hộp', 'tim nhanh', 'tim chậm', 'thở dốc', 'tức ngực',
                'cao huyết áp', 'huyết áp thấp', 'đau tức ngực', 'khó thở khi gắng sức'
            ],
            'nội khoa': [
                'sốt', 'đau đầu', 'mệt mỏi', 'chóng mặt', 'buồn nôn', 'yếu',
                'cảm lạnh', 'cảm cúm', 'ho khan', 'sổ mũi', 'nhức đầu', 'đau người',
                'mất ngủ', 'stress', 'căng thẳng', 'lo âu', 'trầm cảm', 'mệt lử',
                'không có sức lực', 'uể oải', 'thiếu máu', 'hoa mắt', 'choáng váng'
            ],
            'ngoại khoa': [
                'gãy', 'vết thương', 'phẫu thuật', 'u', 'khối', 'chấn thương',
                'bong gân', 'trật khớp', 'đau xương', 'sưng', 'bầm tím', 'chảy máu',
                'cắt', 'đứt', 'rách', 'bỏng', 'tai nạn', 'va đập', 'ngã', 'đau cột sống'
            ],
            'da liễu': [
                'ngứa', 'phát ban', 'mụn', 'da', 'nấm', 'nổi mẩn',
                'mẩn đỏ', 'dị ứng da', 'viêm da', 'chàm', 'zona', 'mụn nước',
                'nấm da', 'nấm móng', 'lang ben', 'vảy nến', 'mụn trứng cá',
                'da khô', 'da bong tróc', 'đốm đen', 'nám da', 'tàn nhang'
            ],
            'tai mũi họng': [
                'ho', 'đau họng', 'nghẹt mũi', 'tai', 'amidan', 'viêm họng',
                'viêm amidan', 'viêm xoang', 'chảy nước mũi', 'hắt hơi', 'ngạt mũi',
                'đau tai', 'ù tai', 'nghe kém', 'chảy mủ tai', 'viêm tai giữa',
                'khàn tiếng', 'mất tiếng', 'ho có đờm', 'ho ra máu', 'khó nuốt'
            ],
            'mắt': [
                'mắt', 'nhìn mờ', 'đau mắt', 'cận thị', 'mỏi mắt',
                'viêm kết mạc', 'đau mắt đỏ', 'chảy nước mắt', 'khô mắt',
                'nhìn đôi', 'quáng gà', 'lóa mắt', 'mờ mắt', 'giảm thị lực',
                'lác mắt', 'sụp mí', 'mắt sưng', 'ghèn', 'lẹo mắt'
            ],
            'răng hàm mặt': [
                'răng', 'nướu', 'đau răng', 'sâu răng', 'chảy máu nướu',
                'viêm nướu', 'áp xe răng', 'nhức răng', 'răng lung lay',
                'mọc răng khôn', 'tụt nướu', 'hôi miệng', 'cao răng', 'vôi răng',
                'răng ê buốt', 'răng vỡ', 'răng mẻ', 'đau hàm', 'cắn không được'
            ],
            'thần kinh': [
                'đau đầu', 'chóng mặt', 'tê', 'liệt', 'co giật', 'mất ngủ',
                'đau nửa đầu', 'migraine', 'tê tay', 'tê chân', 'run tay',
                'động kinh', 'tai biến', 'đột quỵ', 'mất trí nhớ', 'sa sút trí tuệ',
                'parkinson', 'đau dây thần kinh', 'tê bì', 'yếu liệt', 'co cứng'
            ],
            'tiêu hóa': [
                'đau bụng', 'tiêu chảy', 'táo bón', 'nôn', 'dạ dày', 'ợ nóng',
                'đau dạ dày', 'viêm dạ dày', 'loét dạ dày', 'đầy bụng', 'khó tiêu',
                'ợ chua', 'trào ngược', 'đi ngoài ra máu', 'phân đen', 'bí tiểu',
                'viêm ruột', 'viêm đại tràng', 'hội chứng ruột kích thích', 'đau gan'
            ],
            'sản phụ khoa': [
                'thai', 'mang thai', 'có thai', 'sinh', 'kinh nguyệt', 'phụ khoa',
                'rong kinh', 'rong huyết', 'đau bụng dưới', 'khí hư', 'viêm phụ khoa',
                'u xơ tử cung', 'nang buồng trứng', 'vô sinh', 'hiếm muộn',
                'đau khi quan hệ', 'chậm kinh', 'kinh không đều', 'tiền mãn kinh'
            ],
            'cơ xương khớp': [
                'đau lưng', 'đau khớp', 'viêm khớp', 'thoái hóa khớp', 'gout',
                'đau cột sống', 'thoát vị đĩa đệm', 'đau vai gáy', 'đau cổ',
                'cứng khớp', 'sưng khớp', 'đau xương', 'loãng xương', 'thấp khớp',
                'viêm gân', 'đau cơ', 'chuột rút', 'tê tay chân', 'đau thần kinh tọa'
            ],
            'nhi khoa': [
                'trẻ em', 'trẻ con', 'bé', 'con tôi', 'cháu', 'em bé',
                'sốt cao', 'co giật', 'tiêu chảy cấp', 'nôn trớ', 'quấy khóc',
                'không chịu ăn', 'suy dinh dưỡng', 'chậm phát triển', 'ho lâu ngày'
            ]
        }
        
        # Tìm chuyên khoa phù hợp với scoring cải tiến
        best_match = 'nội khoa'
        max_score = 0
        matched_keywords = []
        
        for specialty, keywords in specialty_keywords.items():
            if specialty in [ck.lower() for ck in chuyen_khoa_list]:
                score = 0
                current_matches = []
                
                for keyword in keywords:
                    if keyword in symptoms_lower:
                        # Tính điểm dựa trên độ dài từ khóa (từ khóa dài hơn = quan trọng hơn)
                        keyword_score = len(keyword.split()) * 2
                        score += keyword_score
                        current_matches.append(keyword)
                
                if score > max_score:
                    max_score = score
                    best_match = specialty
                    matched_keywords = current_matches
        
        # Tìm chuyên khoa trong database
        try:
            chuyen_khoa = ChuyenKhoa.objects.filter(ten__icontains=best_match).first()
            if not chuyen_khoa:
                chuyen_khoa = ChuyenKhoa.objects.first()
            specialty_name = chuyen_khoa.ten
        except:
            specialty_name = 'Nội khoa'
        
        # Tính confidence dựa trên số từ khóa match và độ phức tạp
        base_confidence = 50
        if max_score > 0:
            confidence = min(95, base_confidence + max_score * 8)
        else:
            confidence = base_confidence
        
        # Tạo phân tích chi tiết
        analysis_detail = {
            "trieu_chung_chinh": matched_keywords if matched_keywords else [symptoms_text],
            "benh_co_the": self._get_possible_diseases(best_match, matched_keywords),
            "ly_do_chon_chuyen_khoa": f"Dựa trên các từ khóa: {', '.join(matched_keywords[:3]) if matched_keywords else 'triệu chứng mô tả'}, {specialty_name} là chuyên khoa phù hợp nhất",
            "luu_y": "Đây chỉ là gợi ý ban đầu dựa trên từ khóa, cần khám trực tiếp để chẩn đoán chính xác"
        }
        
        print(f"🔍 [KEYWORD] Specialty: {specialty_name}, Score: {max_score}, Confidence: {confidence}%, Matches: {matched_keywords}")
        
        return {
            "chuyen_khoa_de_xuat": specialty_name,
            "do_tin_cay": confidence,
            "phan_tich": analysis_detail,
            "matched_keywords": matched_keywords,
            "keyword_score": max_score
        }


class DoctorRecommendationService:
    """Service để gợi ý bác sĩ dựa trên rating và chuyên khoa"""
    
    @staticmethod
    def get_top_doctors(chuyen_khoa_name, limit=3):
        """Lấy danh sách bác sĩ rating cao nhất theo chuyên khoa - CHỈ BÁC SĨ CÓ LỊCH TRỐNG"""
        from appointments.models import LichLamViec
        from datetime import datetime, timedelta
        
        try:
            chuyen_khoa = ChuyenKhoa.objects.get(ten=chuyen_khoa_name)
        except ChuyenKhoa.DoesNotExist:
            # Nếu không tìm thấy chuyên khoa, lấy tất cả bác sĩ
            chuyen_khoa = None
        
        # Lấy ngày hiện tại và 7 ngày tới
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=7)
        
        # Query bác sĩ CÓ LỊCH TRỐNG trong 7 ngày tới
        doctors_with_slots = LichLamViec.objects.filter(
            ngay__gte=start_date,
            ngay__lte=end_date,
            con_trong=True
        ).values_list('bac_si_id', flat=True).distinct()
        
        # Query bác sĩ theo chuyên khoa VÀ có lịch trống
        doctors_query = HoSoBacSi.objects.select_related('nguoi_dung', 'chuyen_khoa').filter(
            id__in=doctors_with_slots
        )
        
        if chuyen_khoa:
            doctors_query = doctors_query.filter(chuyen_khoa=chuyen_khoa)
        
        # Sắp xếp theo phí khám thấp nhất
        doctors_query = doctors_query.order_by('phi_kham')[:limit]
        
        recommendations = []
        for i, doctor in enumerate(doctors_query, 1):
            # Đếm số lịch trống của bác sĩ
            available_slots_count = LichLamViec.objects.filter(
                bac_si=doctor,
                ngay__gte=start_date,
                ngay__lte=end_date,
                con_trong=True
            ).count()
            
            # Tính rating dựa trên thứ tự và số lịch trống
            base_rating = 4.5 - (i * 0.1)
            slot_bonus = min(0.3, available_slots_count * 0.05)  # Bonus tối đa 0.3
            rating_score = min(5.0, base_rating + slot_bonus)
            
            recommendations.append({
                'doctor': doctor,
                'priority': i,
                'rating_score': round(rating_score, 1),
                'available_slots': available_slots_count,
                'reason': f"Bác sĩ {doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'đa khoa'} với {available_slots_count} lịch trống"
            })
        
        print(f"🔍 [DEBUG] Found {len(recommendations)} doctors with available slots for {chuyen_khoa_name}")
        return recommendations
    
    @staticmethod
    def check_doctor_optimization(selected_doctor_id, recommended_doctors):
        """Kiểm tra xem bác sĩ được chọn có tối ưu không"""
        
        recommended_ids = [rec['doctor'].id for rec in recommended_doctors]
        
        if selected_doctor_id not in recommended_ids:
            try:
                selected_doctor = HoSoBacSi.objects.get(id=selected_doctor_id)
                return {
                    'is_optimal': False,
                    'warning': f"Bác sĩ {selected_doctor.nguoi_dung.get_full_name()} không phải lựa chọn tối ưu nhất cho triệu chứng của bạn.",
                    'suggestion': "Bạn có muốn chọn bác sĩ được đề xuất để có kết quả khám tốt hơn?"
                }
            except HoSoBacSi.DoesNotExist:
                return {
                    'is_optimal': False,
                    'warning': "Bác sĩ không tồn tại.",
                    'suggestion': "Vui lòng chọn bác sĩ khác."
                }
        
        return {'is_optimal': True}


class AppointmentService:
    """Service để xử lý đặt lịch hẹn"""
    
    @staticmethod
    def get_available_slots(doctor_id, days_ahead=7):
        """Lấy lịch trống gần nhất của bác sĩ"""
        
        try:
            doctor = HoSoBacSi.objects.get(id=doctor_id)
        except HoSoBacSi.DoesNotExist:
            return []
        
        # Lấy lịch làm việc trong 7 ngày tới
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=days_ahead)
        
        available_slots = LichLamViec.objects.filter(
            bac_si=doctor,
            ngay__gte=start_date,
            ngay__lte=end_date,
            con_trong=True
        ).order_by('ngay', 'gio_bat_dau')
        
        return available_slots
    
    @staticmethod
    def create_appointment(benh_nhan, doctor_id, lich_lam_viec_id, symptoms):
        """Tạo lịch hẹn mới"""
        from appointments.models import LichHen
        
        try:
            doctor = HoSoBacSi.objects.get(id=doctor_id)
            lich_lam_viec = LichLamViec.objects.get(id=lich_lam_viec_id, con_trong=True)
            
            # Kiểm tra xem user có profile bệnh nhân không
            if not hasattr(benh_nhan, 'ho_so_benh_nhan'):
                return {
                    'success': False,
                    'message': 'Bạn cần tạo hồ sơ bệnh nhân trước khi đặt lịch'
                }
            
            # Tạo lịch hẹn
            lich_hen = LichHen.objects.create(
                benh_nhan=benh_nhan.ho_so_benh_nhan,
                bac_si=doctor,
                lich_lam_viec=lich_lam_viec,
                ngay=lich_lam_viec.ngay,
                gio=lich_lam_viec.gio_bat_dau,
                trieu_chung=symptoms,
                trang_thai='pending'
            )
            
            # Đánh dấu lịch làm việc không còn trống
            lich_lam_viec.con_trong = False
            lich_lam_viec.save()
            
            return {
                'success': True,
                'appointment': lich_hen,
                'message': 'Đặt lịch thành công! Vui lòng chờ xác nhận từ phòng khám.'
            }
            
        except Exception as e:
            return {
                'success': False,
                'message': f'Lỗi đặt lịch: {str(e)}'
            }
