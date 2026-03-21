import openai
import json
from django.conf import settings
from django.db.models import Avg, Count
from accounts.models import HoSoBacSi, ChuyenKhoa
from appointments.models import LichLamViec
from .models import TrieuChungAnalysis, BacSiRecommendation
from datetime import datetime, timedelta


class OpenAIService:
    """Service để tương tác với OpenAI API"""
    
    def __init__(self):
        # Lấy API key từ settings
        self.api_key = getattr(settings, 'OPENAI_API_KEY', '')
        if self.api_key and self.api_key != 'your-openai-api-key-here':
            openai.api_key = self.api_key
            self.use_real_ai = True
        else:
            self.use_real_ai = False
    
    def chat_with_gpt(self, message, context=None):
        """Chat với GPT để hỗ trợ tổng quát"""
        
        if not self.use_real_ai:
            return self._fallback_chat_response(message)
        
        try:
            system_prompt = """Bạn là trợ lý AI y tế thông minh của phòng khám. 
Nhiệm vụ của bạn:
1. Trò chuyện thân thiện, tự nhiên với bệnh nhân
2. Hỏi thêm thông tin về triệu chứng nếu cần
3. Giải đáp thắc mắc về sức khỏe
4. Hướng dẫn quy trình đặt lịch khám
5. Trả lời ngắn gọn, dễ hiểu

Lưu ý: Không tự ý chẩn đoán bệnh, chỉ gợi ý nên khám chuyên khoa nào."""

            if context:
                system_prompt += f"\n\nThông tin ngữ cảnh: {context}"
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"OpenAI Error: {e}")
            return self._fallback_chat_response(message)
    
    def _fallback_chat_response(self, message):
        """Phản hồi dự phòng khi không có OpenAI"""
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
        """Phân tích triệu chứng và đề xuất chuyên khoa"""
        
        # Lấy danh sách chuyên khoa hiện có
        chuyen_khoa_list = list(ChuyenKhoa.objects.values_list('ten', flat=True))
        
        if self.use_real_ai:
            return self._analyze_with_gpt(symptoms_text, chuyen_khoa_list)
        else:
            return self._analyze_with_keywords(symptoms_text, chuyen_khoa_list)
    
    def _analyze_with_gpt(self, symptoms_text, chuyen_khoa_list):
        """Phân tích bằng GPT"""
        
        prompt = f"""Bạn là bác sĩ AI chuyên nghiệp. Phân tích triệu chứng sau và đề xuất chuyên khoa phù hợp:

Triệu chứng: {symptoms_text}

Danh sách chuyên khoa có sẵn: {', '.join(chuyen_khoa_list)}

Trả về JSON với format chính xác:
{{
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
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Bạn là bác sĩ AI, chỉ trả về JSON như yêu cầu."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=0.3
            )
            
            result_text = response.choices[0].message.content.strip()
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
            
            return result
            
        except Exception as e:
            print(f"GPT Analysis Error: {e}")
            return self._analyze_with_keywords(symptoms_text, chuyen_khoa_list)
    
    def _analyze_with_keywords(self, symptoms_text, chuyen_khoa_list):
        """Phân tích nhanh dựa trên từ khóa (fallback)"""
        
        symptoms_lower = symptoms_text.lower()
        
        # Mapping từ khóa với chuyên khoa
        specialty_keywords = {
            'tim mạch': ['tim', 'ngực', 'đau ngực', 'khó thở', 'huyết áp', 'mạch'],
            'nội khoa': ['sốt', 'đau đầu', 'mệt mỏi', 'chóng mặt', 'buồn nôn'],
            'ngoại khoa': ['gãy', 'vết thương', 'phẫu thuật', 'u', 'khối'],
            'da liễu': ['ngứa', 'phát ban', 'mụn', 'da', 'nấm'],
            'tai mũi họng': ['ho', 'đau họng', 'nghẹt mũi', 'tai', 'amidan'],
            'mắt': ['mắt', 'nhìn mờ', 'đau mắt', 'cận thị'],
            'răng hàm mặt': ['răng', 'nướu', 'đau răng', 'sâu răng'],
            'thần kinh': ['đau đầu', 'chóng mặt', 'tê', 'liệt', 'co giật'],
            'tiêu hóa': ['đau bụng', 'tiêu chảy', 'táo bón', 'nôn', 'dạ dày'],
            'sản phụ khoa': ['thai', 'mang thai', 'có thai', 'sinh', 'kinh nguyệt', 'phụ khoa']
        }
        
        # Tìm chuyên khoa phù hợp
        best_match = 'nội khoa'
        max_score = 0
        
        for specialty, keywords in specialty_keywords.items():
            if specialty in [ck.lower() for ck in chuyen_khoa_list]:
                score = sum(1 for keyword in keywords if keyword in symptoms_lower)
                if score > max_score:
                    max_score = score
                    best_match = specialty
        
        # Tìm chuyên khoa trong database
        try:
            chuyen_khoa = ChuyenKhoa.objects.filter(ten__icontains=best_match).first()
            if not chuyen_khoa:
                chuyen_khoa = ChuyenKhoa.objects.first()
            specialty_name = chuyen_khoa.ten
        except:
            specialty_name = 'Nội khoa'
        
        confidence = min(85, 60 + max_score * 10)
        
        return {
            "chuyen_khoa_de_xuat": specialty_name,
            "do_tin_cay": confidence,
            "phan_tich": {
                "trieu_chung_chinh": [symptoms_text],
                "benh_co_the": ["Cần khám để xác định chính xác"],
                "ly_do_chon_chuyen_khoa": f"Dựa trên triệu chứng mô tả, {specialty_name} là chuyên khoa phù hợp nhất",
                "luu_y": "Đây chỉ là gợi ý ban đầu, cần khám trực tiếp để chẩn đoán chính xác"
            }
        }


class DoctorRecommendationService:
    """Service để gợi ý bác sĩ dựa trên rating và chuyên khoa"""
    
    @staticmethod
    def get_top_doctors(chuyen_khoa_name, limit=3):
        """Lấy danh sách bác sĩ rating cao nhất theo chuyên khoa"""
        
        try:
            chuyen_khoa = ChuyenKhoa.objects.get(ten=chuyen_khoa_name)
        except ChuyenKhoa.DoesNotExist:
            # Nếu không tìm thấy chuyên khoa, lấy tất cả bác sĩ
            chuyen_khoa = None
        
        # Query bác sĩ
        doctors_query = HoSoBacSi.objects.select_related('nguoi_dung', 'chuyen_khoa')
        
        if chuyen_khoa:
            doctors_query = doctors_query.filter(chuyen_khoa=chuyen_khoa)
        
        # Sắp xếp theo phí khám thấp nhất (tạm thời)
        doctors_query = doctors_query.order_by('phi_kham')[:limit]
        
        recommendations = []
        for i, doctor in enumerate(doctors_query, 1):
            # Sử dụng rating mặc định
            rating_score = 4.5 - (i * 0.1)  # Giảm dần theo thứ tự
            
            recommendations.append({
                'doctor': doctor,
                'priority': i,
                'rating_score': round(rating_score, 1),
                'reason': f"Bác sĩ {doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'đa khoa'} với kinh nghiệm {doctor.bang_cap}"
            })
        
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