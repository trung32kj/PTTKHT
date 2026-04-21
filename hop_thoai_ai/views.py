from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.views import View
import json
import uuid

from .models import ChatSession, ChatMessage, TrieuChungAnalysis, BacSiRecommendation
from .services import OpenAIService, DoctorRecommendationService, AppointmentService
from tai_khoan.models import ChuyenKhoa, HoSoBacSi


@login_required
@ensure_csrf_cookie
def chat_interface(request):
    """Giao diện chat chính"""
    return render(request, 'hop_thoai_ai/trang_chat.html')


@method_decorator(login_required, name='dispatch')
class ChatAPIView(View):
    """API xử lý chat với AI"""
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            action = data.get('action')
            
            if action == 'start_chat':
                return self.start_chat(request.user)
            elif action == 'send_message':
                return self.send_message(request.user, data)
            elif action == 'select_doctor':
                return self.select_doctor(request.user, data)
            elif action == 'get_specialty_doctors':
                return self.get_specialty_doctors(request.user, data)
            elif action == 'book_appointment':
                return self.book_appointment(request.user, data)
            else:
                return JsonResponse({'error': 'Action không hợp lệ'}, status=400)
                
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Dữ liệu JSON không hợp lệ'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def start_chat(self, user):
        """Bắt đầu phiên chat mới"""
        session_id = str(uuid.uuid4())
        
        chat_session = ChatSession.objects.create(
            benh_nhan=user,
            session_id=session_id
        )
        
        # Tin nhắn chào hỏi từ AI
        welcome_message = ChatMessage.objects.create(
            chat_session=chat_session,
            nguoi_gui='ai',
            noi_dung='Xin chào! Tôi là trợ lý AI của phòng khám. Hãy mô tả triệu chứng của bạn để tôi có thể gợi ý bác sĩ phù hợp nhất.'
        )
        
        return JsonResponse({
            'session_id': session_id,
            'message': {
                'id': welcome_message.id,
                'sender': 'ai',
                'content': welcome_message.noi_dung,
                'timestamp': welcome_message.thoi_gian.isoformat()
            }
        })
    
    def send_message(self, user, data):
        """Xử lý tin nhắn từ user"""
        session_id = data.get('session_id')
        message_content = data.get('message', '').strip()
        
        if not message_content:
            return JsonResponse({'error': 'Tin nhắn không được để trống'}, status=400)
        
        try:
            chat_session = ChatSession.objects.get(
                session_id=session_id,
                benh_nhan=user,
                trang_thai='active'
            )
        except ChatSession.DoesNotExist:
            return JsonResponse({'error': 'Phiên chat không tồn tại'}, status=404)
        
        # Lưu tin nhắn của user
        user_message = ChatMessage.objects.create(
            chat_session=chat_session,
            nguoi_gui='user',
            noi_dung=message_content
        )
        
        # Kiểm tra xem có phải yêu cầu xem lịch không (sau khi có cảnh báo)
        schedule_request = self.parse_schedule_request(message_content, chat_session)
        if schedule_request:
            return self.handle_schedule_request(user, chat_session, schedule_request, user_message)
        
        # Kiểm tra xem có phải yêu cầu bác sĩ cụ thể không
        doctor_request = self.parse_doctor_request(message_content)
        if doctor_request:
            return self.handle_specific_doctor_request(user, chat_session, doctor_request, user_message)
        
        # Kiểm tra xem có phải yêu cầu chuyên khoa khác không
        if self.is_specialty_request(message_content):
            return self.handle_specialty_request(user, chat_session, message_content, user_message)
        
        # Phân tích triệu chứng với AI (lần đầu)
        openai_service = OpenAIService()
        analysis_result = openai_service.analyze_symptoms(message_content)
        
        # Kiểm tra xem input có hợp lệ không
        if not analysis_result.get('is_valid', True):
            # Input không hợp lệ - yêu cầu mô tả lại
            error_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=f"❌ {analysis_result.get('message', 'Vui lòng mô tả triệu chứng cụ thể hơn.')}\n\n💡 **Ví dụ triệu chứng hợp lệ:**\n• Đau đầu kéo dài 3 ngày\n• Sốt cao, ho có đờm\n• Đau bụng, buồn nôn\n• Ngứa da, nổi mẩn đỏ"
            )
            
            return JsonResponse({
                'user_message': {
                    'id': user_message.id,
                    'sender': 'user',
                    'content': user_message.noi_dung,
                    'timestamp': user_message.thoi_gian.isoformat()
                },
                'ai_message': {
                    'id': error_message.id,
                    'sender': 'ai',
                    'content': error_message.noi_dung,
                    'timestamp': error_message.thoi_gian.isoformat()
                }
            })
        
        # Lưu kết quả phân tích
        try:
            chuyen_khoa = ChuyenKhoa.objects.get(ten=analysis_result['chuyen_khoa_de_xuat'])
        except ChuyenKhoa.DoesNotExist:
            chuyen_khoa = ChuyenKhoa.objects.first()  # Fallback
        
        analysis = TrieuChungAnalysis.objects.create(
            chat_session=chat_session,
            trieu_chung_goc=message_content,
            chuyen_khoa_de_xuat=chuyen_khoa,
            do_tin_cay=analysis_result['do_tin_cay'],
            phan_tich_chi_tiet=analysis_result['phan_tich']
        )
        
        # Gợi ý bác sĩ
        doctor_service = DoctorRecommendationService()
        recommended_doctors = doctor_service.get_top_doctors(chuyen_khoa.ten)
        
        # Lưu gợi ý bác sĩ
        for rec in recommended_doctors:
            BacSiRecommendation.objects.create(
                analysis=analysis,
                bac_si=rec['doctor'],
                thu_tu_uu_tien=rec['priority'],
                ly_do_goi_y=rec['reason'],
                rating_score=rec['rating_score']
            )
        
        # Tạo response message từ AI
        ai_response = self.create_ai_response(analysis, recommended_doctors)
        
        ai_message = ChatMessage.objects.create(
            chat_session=chat_session,
            nguoi_gui='ai',
            noi_dung=ai_response['text'],
            metadata=ai_response['data']
        )
        
        return JsonResponse({
            'user_message': {
                'id': user_message.id,
                'sender': 'user',
                'content': user_message.noi_dung,
                'timestamp': user_message.thoi_gian.isoformat()
            },
            'ai_message': {
                'id': ai_message.id,
                'sender': 'ai',
                'content': ai_message.noi_dung,
                'timestamp': ai_message.thoi_gian.isoformat(),
                'data': ai_message.metadata
            }
        })
    
    def parse_doctor_request(self, message):
        """Phân tích xem có yêu cầu bác sĩ cụ thể không"""
        import re
        
        # Các pattern để nhận diện yêu cầu bác sĩ
        patterns = [
            r'(?:muốn gặp|muốn đặt|đặt lịch|chọn|khám với)\s*(?:bs\.?|bác sĩ|doctor)?\s*(?:bs\.?|bác sĩ)?\s*([^?!.]+)',
            r'(?:bs\.?|bác sĩ)\s*([^?!.]+)',
            r'([a-zA-ZÀ-ỹ\s]+)\s*(?:được không|có được không|khác được không)'
        ]
        
        message_lower = message.lower()
        
        for pattern in patterns:
            match = re.search(pattern, message_lower, re.IGNORECASE)
            if match:
                doctor_name = match.group(1).strip()
                # Loại bỏ các từ không cần thiết
                doctor_name = re.sub(r'\b(?:được không|có được không|khác được không|thì|là|có|không)\b', '', doctor_name).strip()
                if len(doctor_name) > 2:  # Tên phải có ít nhất 3 ký tự
                    return doctor_name
        
        return None
    
    def parse_schedule_request(self, message, chat_session):
        """Phân tích xem có yêu cầu xem lịch không"""
        import re
        
        message_lower = message.lower()
        
        # Các từ khóa yêu cầu xem lịch
        schedule_keywords = [
            'xem lịch', 'hiện lịch', 'hiển thị lịch', 'lịch trống', 'lịch rảnh',
            'thời gian rảnh', 'thời gian trống', 'giờ rảnh', 'giờ trống',
            'đặt lịch', 'book lịch', 'có lịch nào'
        ]
        
        # Kiểm tra có từ khóa không
        has_schedule_keyword = any(keyword in message_lower for keyword in schedule_keywords)
        
        if not has_schedule_keyword:
            return None
        
        # Lấy tin nhắn gần nhất từ AI có metadata warning
        recent_messages = ChatMessage.objects.filter(
            chat_session=chat_session,
            nguoi_gui='ai'
        ).order_by('-thoi_gian')[:5]
        
        for msg in recent_messages:
            if msg.metadata and msg.metadata.get('warning') and msg.metadata.get('doctor_id'):
                return msg.metadata.get('doctor_id')
        
        return None
    
    def handle_schedule_request(self, user, chat_session, doctor_id, user_message):
        """Xử lý yêu cầu xem lịch (bỏ qua cảnh báo)"""
        
        try:
            doctor = HoSoBacSi.objects.get(id=doctor_id)
        except HoSoBacSi.DoesNotExist:
            response_text = "❌ Không tìm thấy thông tin bác sĩ. Vui lòng thử lại."
            ai_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=response_text
            )
            
            return JsonResponse({
                'user_message': {
                    'id': user_message.id,
                    'sender': 'user',
                    'content': user_message.noi_dung,
                    'timestamp': user_message.thoi_gian.isoformat()
                },
                'ai_message': {
                    'id': ai_message.id,
                    'sender': 'ai',
                    'content': ai_message.noi_dung,
                    'timestamp': ai_message.thoi_gian.isoformat()
                }
            })
        
        # Xác nhận và lấy lịch trống
        response_text = f"""
✅ **Đã hiểu! Đang tìm lịch trống của BS. {doctor.nguoi_dung.get_full_name()}**

**Thông tin bác sĩ:**
- Chuyên khoa: {doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'Đa khoa'}
- Phí khám: {doctor.phi_kham:,.0f} VNĐ
"""
        
        ai_message = ChatMessage.objects.create(
            chat_session=chat_session,
            nguoi_gui='ai',
            noi_dung=response_text
        )
        
        # Lấy lịch trống
        slots_response = self.get_available_slots(user, chat_session, doctor_id)
        slots_data = json.loads(slots_response.content)
        
        return JsonResponse({
            'user_message': {
                'id': user_message.id,
                'sender': 'user',
                'content': user_message.noi_dung,
                'timestamp': user_message.thoi_gian.isoformat()
            },
            'ai_message': {
                'id': ai_message.id,
                'sender': 'ai',
                'content': ai_message.noi_dung,
                'timestamp': ai_message.thoi_gian.isoformat()
            },
            'slots': slots_data
        })
    
    def handle_specific_doctor_request(self, user, chat_session, doctor_name, user_message):
        """Xử lý yêu cầu bác sĩ cụ thể"""
        
        # Tìm bác sĩ theo tên - thử nhiều cách
        from django.db.models import Q
        
        # Cách 1: Tìm theo first_name hoặc last_name
        doctors = HoSoBacSi.objects.filter(
            Q(nguoi_dung__first_name__icontains=doctor_name) |
            Q(nguoi_dung__last_name__icontains=doctor_name)
        )
        
        # Cách 2: Tìm theo từng phần của tên
        if not doctors.exists():
            name_parts = doctor_name.split()
            if len(name_parts) >= 2:
                # Thử tìm với first_name chứa phần đầu và last_name chứa phần cuối
                doctors = HoSoBacSi.objects.filter(
                    Q(nguoi_dung__first_name__icontains=name_parts[0]) &
                    Q(nguoi_dung__last_name__icontains=name_parts[-1])
                )
                
                # Nếu vẫn không có, thử tìm bất kỳ phần nào
                if not doctors.exists():
                    query = Q()
                    for part in name_parts:
                        if len(part) > 1:  # Bỏ qua các từ quá ngắn
                            query |= Q(nguoi_dung__first_name__icontains=part)
                            query |= Q(nguoi_dung__last_name__icontains=part)
                    doctors = HoSoBacSi.objects.filter(query)
        
        if not doctors:
            # Không tìm thấy bác sĩ
            response_text = f"""
❌ **Không tìm thấy bác sĩ "{doctor_name}"**

Có thể bạn đã nhập sai tên. Vui lòng kiểm tra lại hoặc chọn từ danh sách bác sĩ được đề xuất.
"""
            ai_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=response_text
            )
            
            return JsonResponse({
                'user_message': {
                    'id': user_message.id,
                    'sender': 'user',
                    'content': user_message.noi_dung,
                    'timestamp': user_message.thoi_gian.isoformat()
                },
                'ai_message': {
                    'id': ai_message.id,
                    'sender': 'ai',
                    'content': ai_message.noi_dung,
                    'timestamp': ai_message.thoi_gian.isoformat()
                }
            })
        
        # Lấy bác sĩ đầu tiên nếu có nhiều kết quả
        selected_doctor = doctors.first()
        
        # Lấy phân tích gần nhất để so sánh
        latest_analysis = TrieuChungAnalysis.objects.filter(
            chat_session=chat_session
        ).order_by('-ngay_phan_tich').first()
        
        if not latest_analysis:
            response_text = "⚠️ Vui lòng mô tả triệu chứng trước khi chọn bác sĩ."
            ai_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=response_text
            )
            
            return JsonResponse({
                'user_message': {
                    'id': user_message.id,
                    'sender': 'user',
                    'content': user_message.noi_dung,
                    'timestamp': user_message.thoi_gian.isoformat()
                },
                'ai_message': {
                    'id': ai_message.id,
                    'sender': 'ai',
                    'content': ai_message.noi_dung,
                    'timestamp': ai_message.thoi_gian.isoformat()
                }
            })
        
        # Lấy danh sách bác sĩ được đề xuất
        doctor_service = DoctorRecommendationService()
        recommended_doctors = doctor_service.get_top_doctors(latest_analysis.chuyen_khoa_de_xuat.ten)
        
        # Kiểm tra xem bác sĩ được chọn có trong danh sách đề xuất không
        is_recommended = any(rec['doctor'].id == selected_doctor.id for rec in recommended_doctors)
        
        if is_recommended:
            # Bác sĩ được đề xuất - tiến hành đặt lịch
            response_text = f"""
✅ **BS. {selected_doctor.nguoi_dung.get_full_name()}** là lựa chọn tốt cho triệu chứng của bạn!

**Thông tin bác sĩ:**
- Chuyên khoa: {selected_doctor.chuyen_khoa.ten if selected_doctor.chuyen_khoa else 'Đa khoa'}
- Phí khám: {selected_doctor.phi_kham:,.0f} VNĐ
- Kinh nghiệm: {selected_doctor.bang_cap}

Đang tìm lịch trống gần nhất...
"""
        else:
            # Bác sĩ không được đề xuất - cảnh báo
            response_text = f"""
⚠️ **Cảnh báo: BS. {selected_doctor.nguoi_dung.get_full_name()}**

**So sánh với bác sĩ được đề xuất:**

**Bác sĩ bạn chọn:**
- Tên: BS. {selected_doctor.nguoi_dung.get_full_name()}
- Chuyên khoa: {selected_doctor.chuyen_khoa.ten if selected_doctor.chuyen_khoa else 'Đa khoa'}
- Phí khám: {selected_doctor.phi_kham:,.0f} VNĐ

**Bác sĩ được đề xuất cho triệu chứng của bạn:**
"""
            
            for i, rec in enumerate(recommended_doctors[:3], 1):
                doctor = rec['doctor']
                response_text += f"\n{i}. BS. {doctor.nguoi_dung.get_full_name()} ({doctor.chuyen_khoa.ten}) - {doctor.phi_kham:,.0f} VNĐ"
            
            response_text += f"""

**Rủi ro khi chọn sai chuyên khoa:**
• Có thể không phát hiện đúng nguyên nhân bệnh
• Tốn thời gian và chi phí không cần thiết
• Có thể cần chuyển khoa sau đó

❓ **Bạn có chắc chắn muốn đặt lịch với BS. {selected_doctor.nguoi_dung.get_full_name()} không?**
"""
        
        ai_message = ChatMessage.objects.create(
            chat_session=chat_session,
            nguoi_gui='ai',
            noi_dung=response_text,
            metadata={
                'selected_doctor_id': selected_doctor.id,
                'is_recommended': is_recommended,
                'awaiting_confirmation': not is_recommended,
                'warning': not is_recommended,  # Thêm flag warning để parse_schedule_request nhận diện
                'doctor_id': selected_doctor.id,  # Thêm doctor_id để parse_schedule_request lấy
                'recommended_doctors': [
                    {
                        'id': rec['doctor'].id,
                        'name': rec['doctor'].nguoi_dung.get_full_name(),
                        'specialty': rec['doctor'].chuyen_khoa.ten if rec['doctor'].chuyen_khoa else 'Đa khoa',
                        'fee': float(rec['doctor'].phi_kham),
                        'rating': rec['rating_score']
                    } for rec in recommended_doctors
                ] if not is_recommended else []
            }
        )
        
        response_data = {
            'user_message': {
                'id': user_message.id,
                'sender': 'user',
                'content': user_message.noi_dung,
                'timestamp': user_message.thoi_gian.isoformat()
            },
            'ai_message': {
                'id': ai_message.id,
                'sender': 'ai',
                'content': ai_message.noi_dung,
                'timestamp': ai_message.thoi_gian.isoformat(),
                'data': ai_message.metadata
            }
        }
        
        # Nếu là bác sĩ được đề xuất, tự động lấy lịch trống
        if is_recommended:
            slots_response = self.get_available_slots(user, chat_session, selected_doctor.id)
            if 'slots_available' in slots_response.content.decode():
                slots_data = json.loads(slots_response.content.decode())
                response_data['slots'] = slots_data
        
        return JsonResponse(response_data)
    
    def is_specialty_request(self, message):
        """Kiểm tra xem có phải yêu cầu chuyên khoa khác không"""
        specialty_keywords = [
            'tim mạch', 'nội khoa', 'ngoại khoa', 'tai mũi họng', 'da liễu',
            'mắt', 'răng hàm mặt', 'thần kinh', 'tiêu hóa', 'sản phụ khoa'
        ]
        
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in specialty_keywords)
    
    def handle_specialty_request(self, user, chat_session, message_content, user_message):
        """Xử lý yêu cầu xem bác sĩ chuyên khoa khác"""
        
        # Tìm chuyên khoa được yêu cầu
        specialty_keywords = {
            'tim mạch': 'Tim mạch',
            'nội khoa': 'Nội khoa', 
            'ngoại khoa': 'Ngoại khoa',
            'tai mũi họng': 'Tai mũi họng',
            'da liễu': 'Da liễu',
            'mắt': 'Mắt',
            'răng hàm mặt': 'Răng hàm mặt',
            'thần kinh': 'Thần kinh',
            'tiêu hóa': 'Tiêu hóa',
            'sản phụ khoa': 'Sản phụ khoa'
        }
        
        message_lower = message_content.lower()
        requested_specialty = None
        
        for keyword, specialty_name in specialty_keywords.items():
            if keyword in message_lower:
                requested_specialty = specialty_name
                break
        
        if not requested_specialty:
            # Không tìm thấy chuyên khoa, trả về danh sách
            available_specialties = list(specialty_keywords.values())
            response_text = f"""
🏥 **Các chuyên khoa có sẵn:**

{chr(10).join([f'• {spec}' for spec in available_specialties])}

Vui lòng nhập tên chuyên khoa bạn muốn xem (VD: "Tim mạch")
"""
            ai_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=response_text
            )
            
            return JsonResponse({
                'user_message': {
                    'id': user_message.id,
                    'sender': 'user', 
                    'content': user_message.noi_dung,
                    'timestamp': user_message.thoi_gian.isoformat()
                },
                'ai_message': {
                    'id': ai_message.id,
                    'sender': 'ai',
                    'content': ai_message.noi_dung,
                    'timestamp': ai_message.thoi_gian.isoformat()
                }
            })
        
        # Lấy bác sĩ của chuyên khoa được yêu cầu
        doctor_service = DoctorRecommendationService()
        other_doctors = doctor_service.get_top_doctors(requested_specialty)
        
        if not other_doctors:
            response_text = f"❌ Hiện tại không có bác sĩ {requested_specialty} nào có sẵn."
            ai_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=response_text
            )
            
            return JsonResponse({
                'user_message': {
                    'id': user_message.id,
                    'sender': 'user',
                    'content': user_message.noi_dung, 
                    'timestamp': user_message.thoi_gian.isoformat()
                },
                'ai_message': {
                    'id': ai_message.id,
                    'sender': 'ai',
                    'content': ai_message.noi_dung,
                    'timestamp': ai_message.thoi_gian.isoformat()
                }
            })
        
        # Tạo response với cảnh báo
        response_text = f"""
⚠️ **Lưu ý quan trọng:**

Bạn đang yêu cầu xem bác sĩ **{requested_specialty}** thay vì chuyên khoa được đề xuất ban đầu.

🔍 **Phân tích:**
- Triệu chứng của bạn phù hợp nhất với chuyên khoa khác
- Việc khám sai chuyên khoa có thể:
  • Không phát hiện đúng nguyên nhân
  • Tốn thời gian và chi phí
  • Cần chuyển khoa sau đó

👨‍⚕️ **Bác sĩ {requested_specialty} có sẵn:**
"""
        
        doctors_data = []
        for i, rec in enumerate(other_doctors, 1):
            doctor = rec['doctor']
            response_text += f"\n{i}. **BS. {doctor.nguoi_dung.get_full_name()}**"
            response_text += f"\n   - Phí khám: {doctor.phi_kham:,.0f} VNĐ"
            response_text += f"\n   - Rating: {rec['rating_score']:.1f}/5.0"
            
            doctors_data.append({
                'id': doctor.id,
                'name': doctor.nguoi_dung.get_full_name(),
                'specialty': doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'Đa khoa',
                'fee': float(doctor.phi_kham),
                'rating': rec['rating_score'],
                'priority': rec['priority'],
                'is_recommended': False
            })
        
        response_text += "\n\n❓ **Bạn có chắc chắn muốn đặt lịch với bác sĩ này không?**"
        
        ai_message = ChatMessage.objects.create(
            chat_session=chat_session,
            nguoi_gui='ai',
            noi_dung=response_text,
            metadata={
                'specialty_warning': True,
                'requested_specialty': requested_specialty,
                'other_doctors': doctors_data
            }
        )
        
        return JsonResponse({
            'user_message': {
                'id': user_message.id,
                'sender': 'user',
                'content': user_message.noi_dung,
                'timestamp': user_message.thoi_gian.isoformat()
            },
            'ai_message': {
                'id': ai_message.id,
                'sender': 'ai', 
                'content': ai_message.noi_dung,
                'timestamp': ai_message.thoi_gian.isoformat(),
                'data': ai_message.metadata
            }
        })
    
    def create_ai_response(self, analysis, recommended_doctors):
        """Tạo phản hồi từ AI"""
        phan_tich = analysis.phan_tich_chi_tiet
        
        response_text = f"""
Dựa trên triệu chứng bạn mô tả, tôi phân tích như sau:

🔍 **Phân tích triệu chứng:**
- Triệu chứng chính: {', '.join(phan_tich.get('trieu_chung_chinh', []))}
- Chuyên khoa đề xuất: **{analysis.chuyen_khoa_de_xuat.ten}**
- Độ tin cậy: {analysis.do_tin_cay}%

💡 **Lý do:** {phan_tich.get('ly_do_chon_chuyen_khoa', '')}

👨‍⚕️ **Bác sĩ được đề xuất ({analysis.chuyen_khoa_de_xuat.ten}):**
"""
        
        doctors_data = []
        for i, rec in enumerate(recommended_doctors, 1):
            doctor = rec['doctor']
            response_text += f"\n{i}. **BS. {doctor.nguoi_dung.get_full_name()}**"
            response_text += f"\n   - Chuyên khoa: {doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'Đa khoa'}"
            response_text += f"\n   - Phí khám: {doctor.phi_kham:,.0f} VNĐ"
            response_text += f"\n   - Rating: {rec['rating_score']:.1f}/5.0"
            
            doctors_data.append({
                'id': doctor.id,
                'name': doctor.nguoi_dung.get_full_name(),
                'specialty': doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'Đa khoa',
                'fee': float(doctor.phi_kham),
                'rating': rec['rating_score'],
                'priority': rec['priority'],
                'is_recommended': True
            })
        
        response_text += f"\n\n⚠️ **Lưu ý:** {phan_tich.get('luu_y', '')}"
        response_text += "\n\n🔄 **Muốn xem bác sĩ chuyên khoa khác?** Nhập tên chuyên khoa (VD: Tim mạch, Da liễu, Mắt...)"
        response_text += "\n\n✅ **Hoặc chọn bác sĩ ở trên để đặt lịch**"
        
        return {
            'text': response_text,
            'data': {
                'analysis_id': analysis.id,
                'specialty': analysis.chuyen_khoa_de_xuat.ten,
                'confidence': analysis.do_tin_cay,
                'recommended_doctors': doctors_data,
                'allow_other_specialty': True
            }
        }
    
    def select_doctor(self, user, data):
        """Xử lý khi user chọn bác sĩ"""
        session_id = data.get('session_id')
        doctor_id = data.get('doctor_id')
        analysis_id = data.get('analysis_id')
        
        try:
            chat_session = ChatSession.objects.get(
                session_id=session_id,
                benh_nhan=user,
                trang_thai='active'
            )
            analysis = TrieuChungAnalysis.objects.get(id=analysis_id)
        except (ChatSession.DoesNotExist, TrieuChungAnalysis.DoesNotExist):
            return JsonResponse({'error': 'Dữ liệu không hợp lệ'}, status=404)
        
        # Lấy danh sách bác sĩ được đề xuất
        recommended_doctors = DoctorRecommendationService.get_top_doctors(
            analysis.chuyen_khoa_de_xuat.ten
        )
        
        # Kiểm tra tối ưu
        optimization_check = DoctorRecommendationService.check_doctor_optimization(
            doctor_id, recommended_doctors
        )
        
        if not optimization_check['is_optimal']:
            # Cảnh báo không tối ưu
            warning_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=f"⚠️ {optimization_check['warning']}\n\n{optimization_check['suggestion']}",
                metadata={'warning': True, 'doctor_id': doctor_id}
            )
            
            return JsonResponse({
                'warning': True,
                'message': {
                    'id': warning_message.id,
                    'sender': 'ai',
                    'content': warning_message.noi_dung,
                    'timestamp': warning_message.thoi_gian.isoformat()
                }
            })
        
        # Nếu tối ưu, lấy lịch trống
        return self.get_available_slots(user, chat_session, doctor_id)
    
    def get_available_slots(self, user, chat_session, doctor_id):
        """Lấy lịch trống của bác sĩ"""
        appointment_service = AppointmentService()
        available_slots = appointment_service.get_available_slots(doctor_id)
        
        if not available_slots:
            no_slots_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung='Rất tiếc, bác sĩ này hiện không có lịch trống trong 7 ngày tới. Bạn có muốn chọn bác sĩ khác không?'
            )
            
            return JsonResponse({
                'no_slots': True,
                'message': {
                    'id': no_slots_message.id,
                    'sender': 'ai',
                    'content': no_slots_message.noi_dung,
                    'timestamp': no_slots_message.thoi_gian.isoformat()
                }
            })
        
        # Hiển thị lịch trống
        slots_text = "📅 **Lịch trống gần nhất:**\n\n"
        slots_data = []
        
        for slot in available_slots[:5]:  # Chỉ hiển thị 5 slot đầu
            slots_text += f"• {slot.ngay.strftime('%d/%m/%Y')} - {slot.gio_bat_dau.strftime('%H:%M')} đến {slot.gio_ket_thuc.strftime('%H:%M')}\n"
            slots_data.append({
                'id': slot.id,
                'date': slot.ngay.isoformat(),
                'start_time': slot.gio_bat_dau.strftime('%H:%M'),
                'end_time': slot.gio_ket_thuc.strftime('%H:%M'),
                'display': f"{slot.ngay.strftime('%d/%m/%Y')} {slot.gio_bat_dau.strftime('%H:%M')}"
            })
        
        slots_text += "\nVui lòng chọn thời gian phù hợp để đặt lịch."
        
        slots_message = ChatMessage.objects.create(
            chat_session=chat_session,
            nguoi_gui='ai',
            noi_dung=slots_text,
            metadata={
                'doctor_id': doctor_id,
                'available_slots': slots_data
            }
        )
        
        return JsonResponse({
            'slots_available': True,
            'message': {
                'id': slots_message.id,
                'sender': 'ai',
                'content': slots_message.noi_dung,
                'timestamp': slots_message.thoi_gian.isoformat(),
                'data': slots_message.metadata
            }
        })
    
    def book_appointment(self, user, data):
        """Đặt lịch hẹn"""
        session_id = data.get('session_id')
        doctor_id = data.get('doctor_id')
        slot_id = data.get('slot_id')
        
        try:
            chat_session = ChatSession.objects.get(
                session_id=session_id,
                benh_nhan=user,
                trang_thai='active'
            )
            
            # Lấy triệu chứng từ tin nhắn đầu tiên của user
            symptoms = ChatMessage.objects.filter(
                chat_session=chat_session,
                nguoi_gui='user'
            ).first().noi_dung
            
        except ChatSession.DoesNotExist:
            return JsonResponse({'error': 'Phiên chat không tồn tại'}, status=404)
        
        # Tạo lịch hẹn
        appointment_service = AppointmentService()
        result = appointment_service.create_appointment(
            user, doctor_id, slot_id, symptoms
        )
        
        if result['success']:
            # Đánh dấu chat session hoàn thành
            chat_session.trang_thai = 'completed'
            chat_session.save()
            
            success_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=f"✅ {result['message']}\n\nMã lịch hẹn: #{result['appointment'].id}\nThời gian: {result['appointment'].ngay.strftime('%d/%m/%Y')} {result['appointment'].gio.strftime('%H:%M')}\n\nCảm ơn bạn đã sử dụng dịch vụ!"
            )
            
            return JsonResponse({
                'success': True,
                'appointment_id': result['appointment'].id,
                'message': {
                    'id': success_message.id,
                    'sender': 'ai',
                    'content': success_message.noi_dung,
                    'timestamp': success_message.thoi_gian.isoformat()
                }
            })
        else:
            error_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=f"❌ {result['message']}\n\nVui lòng thử lại hoặc liên hệ trực tiếp với phòng khám."
            )
            
            return JsonResponse({
                'success': False,
                'message': {
                    'id': error_message.id,
                    'sender': 'ai',
                    'content': error_message.noi_dung,
                    'timestamp': error_message.thoi_gian.isoformat()
                }
            })
    
    def get_specialty_doctors(self, user, data):
        """Lấy danh sách bác sĩ theo chuyên khoa"""
        session_id = data.get('session_id')
        specialty = data.get('specialty')
        
        try:
            chat_session = ChatSession.objects.get(
                session_id=session_id,
                benh_nhan=user,
                trang_thai='active'
            )
        except ChatSession.DoesNotExist:
            return JsonResponse({'error': 'Phiên chat không tồn tại'}, status=404)
        
        # Lấy bác sĩ của chuyên khoa được yêu cầu
        doctor_service = DoctorRecommendationService()
        doctors = doctor_service.get_top_doctors(specialty)
        
        if not doctors:
            message_text = f"❌ Hiện tại không có bác sĩ {specialty} nào có sẵn."
            
            ai_message = ChatMessage.objects.create(
                chat_session=chat_session,
                nguoi_gui='ai',
                noi_dung=message_text
            )
            
            return JsonResponse({
                'message': {
                    'id': ai_message.id,
                    'sender': 'ai',
                    'content': ai_message.noi_dung,
                    'timestamp': ai_message.thoi_gian.isoformat()
                },
                'doctors': []
            })
        
        # Kiểm tra xem có phải chuyên khoa được đề xuất không
        latest_analysis = TrieuChungAnalysis.objects.filter(
            chat_session=chat_session
        ).order_by('-ngay_phan_tich').first()
        
        is_recommended_specialty = (
            latest_analysis and 
            latest_analysis.chuyen_khoa_de_xuat.ten == specialty
        )
        
        if is_recommended_specialty:
            message_text = f"✅ **Bác sĩ {specialty} (Được đề xuất):**"
        else:
            message_text = f"""
⚠️ **Cảnh báo: Bác sĩ {specialty}**

Chuyên khoa này không phải là lựa chọn tối ưu cho triệu chứng của bạn.

**Rủi ro khi khám sai chuyên khoa:**
• Có thể không phát hiện đúng nguyên nhân
• Tốn thời gian và chi phí không cần thiết  
• Có thể cần chuyển khoa sau đó

**Bác sĩ {specialty} có sẵn:**
"""
        
        doctors_data = []
        for i, rec in enumerate(doctors, 1):
            doctor = rec['doctor']
            message_text += f"\n{i}. **BS. {doctor.nguoi_dung.get_full_name()}**"
            message_text += f"\n   - Phí khám: {doctor.phi_kham:,.0f} VNĐ"
            message_text += f"\n   - Rating: {rec['rating_score']:.1f}/5.0"
            
            doctors_data.append({
                'id': doctor.id,
                'name': doctor.nguoi_dung.get_full_name(),
                'specialty': doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'Đa khoa',
                'fee': float(doctor.phi_kham),
                'rating': rec['rating_score'],
                'priority': rec['priority'],
                'is_recommended': is_recommended_specialty
            })
        
        if not is_recommended_specialty:
            message_text += "\n\n❓ **Bạn có chắc chắn muốn đặt lịch với bác sĩ này không?**"
        
        ai_message = ChatMessage.objects.create(
            chat_session=chat_session,
            nguoi_gui='ai',
            noi_dung=message_text,
            metadata={
                'specialty_warning': not is_recommended_specialty,
                'requested_specialty': specialty,
                'doctors': doctors_data
            }
        )
        
        return JsonResponse({
            'message': {
                'id': ai_message.id,
                'sender': 'ai',
                'content': ai_message.noi_dung,
                'timestamp': ai_message.thoi_gian.isoformat(),
                'data': ai_message.metadata
            },
            'doctors': doctors_data
        })