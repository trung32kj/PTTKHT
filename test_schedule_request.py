"""
Test yêu cầu xem lịch sau khi có cảnh báo
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.test import RequestFactory
from accounts.models import HoSoBenhNhan
from ai_chatbox.views import ChatAPIView
import json

def test_schedule_request():
    print("=" * 70)
    print("TEST: Yêu cầu xem lịch sau cảnh báo")
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
        
        print(f"✅ Chuyên khoa đề xuất: {data['ai_message']['data']['specialty']}\n")
        
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
        print(f"✅ Hệ thống hiển thị cảnh báo")
        print(f"   awaiting_confirmation: {msg_data.get('awaiting_confirmation')}")
        print(f"   selected_doctor_id: {msg_data.get('selected_doctor_id')}\n")
        
        # BƯỚC 3: User yêu cầu xem lịch
        print("BƯỚC 3: User nhắn 'tôi muốn hiện thời gian rảnh của bác sĩ để đặt lịch'")
        print("-" * 70)
        request = factory.post('/ai-chatbox/api/',
            data=json.dumps({
                'action': 'send_message',
                'session_id': session_id,
                'message': 'tôi muốn hiện thời gian rảnh của bác sĩ để đặt lịch'
            }),
            content_type='application/json'
        )
        request.user = user
        response = view.post(request)
        data = json.loads(response.content)
        
        if response.status_code == 200:
            print(f"✅ Hệ thống xử lý yêu cầu")
            print(f"   AI response: {data['ai_message']['content'][:100]}...")
            
            if data.get('slots'):
                slots_data = data['slots']
                if slots_data.get('slots_available'):
                    print(f"\n✅ Hiển thị lịch trống!")
                    if slots_data['message'].get('data'):
                        slots = slots_data['message']['data'].get('available_slots', [])
                        print(f"   Số lịch trống: {len(slots)}")
                        if slots:
                            print(f"   Lịch đầu tiên: {slots[0]['display']}")
                    
                    print(f"\n📋 Frontend sẽ:")
                    print(f"   1. Hiển thị tin nhắn xác nhận")
                    print(f"   2. Gọi showWidgetSlotSelection(slots)")
                    print(f"   3. User chọn thời gian đặt lịch")
                elif slots_data.get('no_slots'):
                    print(f"\n⚠️ Bác sĩ không có lịch trống")
            else:
                print(f"\n❌ Không có slots trong response")
                print(f"   Response keys: {data.keys()}")
        else:
            print(f"❌ API lỗi: {data}")
        
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
    test_schedule_request()
