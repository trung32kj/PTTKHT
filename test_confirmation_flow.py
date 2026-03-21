"""
Test confirmation flow: User chọn "không" phải hiển thị lại danh sách
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.test import RequestFactory
from accounts.models import HoSoBenhNhan
from ai_chatbox.views import ChatAPIView
import json

def test_confirmation_no():
    print("=" * 60)
    print("TEST: User chọn 'không' → Hiển thị lại danh sách")
    print("=" * 60)
    
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
        
        # Gửi triệu chứng
        print("BƯỚC 1: Gửi triệu chứng 'đau răng'")
        print("-" * 60)
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
        
        recommended_doctors = data['ai_message']['data']['recommended_doctors']
        print(f"✅ Bác sĩ được đề xuất:")
        for doc in recommended_doctors:
            print(f"   - BS. {doc['name']} ({doc['specialty']})")
        print()
        
        # Yêu cầu bác sĩ không được đề xuất
        print("BƯỚC 2: Yêu cầu BS. Văn A Nguyễn (Tim mạch - không phù hợp)")
        print("-" * 60)
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
        
        if msg_data.get('awaiting_confirmation'):
            print(f"✅ Hệ thống yêu cầu xác nhận")
            print(f"   Selected Doctor ID: {msg_data['selected_doctor_id']}")
            
            # Kiểm tra có trả về danh sách bác sĩ được đề xuất không
            if msg_data.get('recommended_doctors'):
                print(f"\n✅ Có danh sách bác sĩ được đề xuất để so sánh:")
                for doc in msg_data['recommended_doctors']:
                    print(f"   - BS. {doc['name']} ({doc['specialty']}) - {doc['fee']:,.0f} VNĐ")
                
                print(f"\n📋 Frontend sẽ:")
                print(f"   1. Lưu danh sách này vào lastRecommendedDoctors")
                print(f"   2. Hiển thị 2 nút: 'Có' và 'Không'")
                print(f"   3. Khi user click 'Không':")
                print(f"      → Hiển thị tin nhắn 'Đã quay lại...'")
                print(f"      → Gọi showWidgetDoctorSelection(lastRecommendedDoctors)")
                print(f"      → User có thể chọn bác sĩ từ danh sách")
            else:
                print(f"\n❌ KHÔNG có danh sách bác sĩ được đề xuất!")
                print(f"   → Frontend không thể hiển thị lại danh sách")
        else:
            print(f"❌ Không yêu cầu xác nhận (lỗi)")
        
        # Cleanup
        from ai_chatbox.models import ChatSession
        ChatSession.objects.filter(session_id=session_id).delete()
        
        print(f"\n" + "=" * 60)
        print(f"✅ TEST HOÀN TẤT")
        print(f"=" * 60)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_confirmation_no()
