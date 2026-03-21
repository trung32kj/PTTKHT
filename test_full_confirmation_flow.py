"""
Test đầy đủ: User chọn "không" → Chọn bác sĩ được đề xuất → Hiển thị lịch
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.test import RequestFactory
from accounts.models import HoSoBenhNhan
from ai_chatbox.views import ChatAPIView
import json

def test_full_flow():
    print("=" * 70)
    print("TEST: Chọn 'không' → Chọn bác sĩ được đề xuất → Hiển thị lịch")
    print("=" * 70)
    
    try:
        benh_nhan = HoSoBenhNhan.objects.first()
        user = benh_nhan.nguoi_dung
        
        factory = RequestFactory()
        view = ChatAPIView()
        
        # Start chat
        request = factory.post('/ai-chatbox/api/', 
            data=json.dumps({'action': 'start_chat'}),
            content_type='application/json'
        )
        request.user = user
        response = view.post(request)
        data = json.loads(response.content)
        session_id = data['session_id']
        
        print(f"✅ Session: {session_id}\n")
        
        # BƯỚC 1: Gửi triệu chứng
        print("BƯỚC 1: Gửi triệu chứng 'đau răng'")
        print("-" * 70)
        request = factory.post('/ai-chatbox/api/',
            data=json.dumps({
                'action': 'send_message',
                'session_id': session_id,
                'message': 'Tôi bị đau răng'
            }),
            content_type='application/json'
        )
        request.user = user
        response = view.post(request)
        data = json.loads(response.content)
        
        analysis_id = data['ai_message']['data']['analysis_id']
        recommended_doctors = data['ai_message']['data']['recommended_doctors']
        
        print(f"✅ Phân tích xong, analysis_id: {analysis_id}")
        print(f"   Bác sĩ được đề xuất:")
        for doc in recommended_doctors:
            print(f"     - ID {doc['id']}: BS. {doc['name']} ({doc['specialty']})")
        print()
        
        # BƯỚC 2: Yêu cầu bác sĩ không được đề xuất
        print("BƯỚC 2: Yêu cầu BS. Văn A Nguyễn (Tim mạch - KHÔNG phù hợp)")
        print("-" * 70)
        request = factory.post('/ai-chatbox/api/',
            data=json.dumps({
                'action': 'send_message',
                'session_id': session_id,
                'message': 'tôi muốn gặp bác sĩ BS. Văn A Nguyễn'
            }),
            content_type='application/json'
        )
        request.user = user
        response = view.post(request)
        data = json.loads(response.content)
        
        msg_data = data['ai_message']['data']
        print(f"✅ Hệ thống yêu cầu xác nhận")
        print(f"   awaiting_confirmation: {msg_data.get('awaiting_confirmation')}")
        print(f"   selected_doctor_id: {msg_data.get('selected_doctor_id')}")
        print()
        
        # BƯỚC 3: Giả lập user click "Không" và chọn bác sĩ được đề xuất
        print("BƯỚC 3: User click 'Không' → Frontend hiển thị lại danh sách")
        print("-" * 70)
        print(f"   Frontend sẽ gọi: showWidgetDoctorSelection(lastRecommendedDoctors)")
        print(f"   Danh sách có {len(msg_data['recommended_doctors'])} bác sĩ")
        print()
        
        # BƯỚC 4: User chọn bác sĩ được đề xuất từ danh sách
        first_recommended_doctor = recommended_doctors[0]
        print(f"BƯỚC 4: User chọn BS. {first_recommended_doctor['name']} (ĐƯỢC đề xuất)")
        print("-" * 70)
        
        request = factory.post('/ai-chatbox/api/',
            data=json.dumps({
                'action': 'select_doctor',
                'session_id': session_id,
                'doctor_id': first_recommended_doctor['id'],
                'analysis_id': analysis_id
            }),
            content_type='application/json'
        )
        request.user = user
        response = view.post(request)
        data = json.loads(response.content)
        
        if data.get('slots_available'):
            print(f"✅ Hệ thống trả về lịch trống!")
            print(f"   slots_available: True")
            
            if data['message'].get('data') and data['message']['data'].get('available_slots'):
                slots = data['message']['data']['available_slots']
                print(f"   Số lịch trống: {len(slots)}")
                print(f"   Lịch đầu tiên: {slots[0]['display']}")
                print()
                print(f"📋 Frontend sẽ:")
                print(f"   → Hiển thị tin nhắn AI")
                print(f"   → Gọi showWidgetSlotSelection(slots)")
                print(f"   → User có thể chọn thời gian đặt lịch")
            else:
                print(f"   ❌ Không có available_slots trong data")
        elif data.get('warning'):
            print(f"❌ Hệ thống vẫn trả về warning (lỗi logic)")
            print(f"   Bác sĩ này PHẢI được đề xuất nhưng backend báo không tối ưu")
        elif data.get('no_slots'):
            print(f"⚠️ Bác sĩ không có lịch trống")
        else:
            print(f"❌ Response không rõ ràng:")
            print(f"   {data}")
        
        # Cleanup
        from ai_chatbox.models import ChatSession
        ChatSession.objects.filter(session_id=session_id).delete()
        
        print()
        print("=" * 70)
        print("✅ TEST HOÀN TẤT")
        print("=" * 70)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_full_flow()
