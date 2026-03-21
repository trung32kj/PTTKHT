"""
Test full flow với BS. Cao Thị Linh
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.test import RequestFactory
from django.contrib.auth.models import User
from accounts.models import HoSoBenhNhan
from ai_chatbox.views import ChatAPIView
import json

def test_full_flow():
    print("=" * 60)
    print("TEST FULL FLOW: BS. Cao Thị Linh")
    print("=" * 60)
    
    # Lấy user bệnh nhân
    try:
        benh_nhan = HoSoBenhNhan.objects.first()
        if not benh_nhan:
            print("❌ Không có bệnh nhân")
            return
        
        user = benh_nhan.nguoi_dung
        print(f"✅ User: {user.username}\n")
        
        factory = RequestFactory()
        view = ChatAPIView()
        
        # Bước 1: Start chat
        print("BƯỚC 1: Khởi tạo chat")
        print("-" * 60)
        request = factory.post('/ai-chatbox/api/', 
            data=json.dumps({'action': 'start_chat'}),
            content_type='application/json'
        )
        request.user = user
        
        response = view.post(request)
        data = json.loads(response.content)
        
        if response.status_code != 200:
            print(f"❌ Failed: {data}")
            return
        
        session_id = data['session_id']
        print(f"✅ Session ID: {session_id}\n")
        
        # Bước 2: Gửi triệu chứng
        print("BƯỚC 2: Gửi triệu chứng")
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
        
        if response.status_code != 200:
            print(f"❌ Failed: {data}")
            return
        
        print(f"✅ AI phân tích triệu chứng")
        if data['ai_message'].get('data'):
            msg_data = data['ai_message']['data']
            print(f"   Chuyên khoa: {msg_data.get('specialty')}")
            print(f"   Độ tin cậy: {msg_data.get('confidence')}%")
            
            if msg_data.get('recommended_doctors'):
                print(f"   Bác sĩ đề xuất:")
                for doc in msg_data['recommended_doctors']:
                    print(f"     - BS. {doc['name']} ({doc['specialty']})")
        print()
        
        # Bước 3: Yêu cầu BS. Cao Thị Linh
        print("BƯỚC 3: Yêu cầu BS. Cao Thị Linh")
        print("-" * 60)
        request = factory.post('/ai-chatbox/api/',
            data=json.dumps({
                'action': 'send_message',
                'session_id': session_id,
                'message': 'tôi muốn gặp bác sĩ BS. Cao Thị Linh'
            }),
            content_type='application/json'
        )
        request.user = user
        
        response = view.post(request)
        data = json.loads(response.content)
        
        if response.status_code != 200:
            print(f"❌ Failed: {data}")
            return
        
        print(f"✅ Xử lý yêu cầu bác sĩ")
        print(f"\nAI Response:")
        print("-" * 60)
        print(data['ai_message']['content'][:500])
        print("-" * 60)
        
        if data['ai_message'].get('data'):
            msg_data = data['ai_message']['data']
            
            if msg_data.get('selected_doctor_id'):
                print(f"\n✅ Selected Doctor ID: {msg_data['selected_doctor_id']}")
            
            if msg_data.get('awaiting_confirmation'):
                print(f"⚠️ Cần xác nhận (bác sĩ không được đề xuất)")
                
                if msg_data.get('recommended_doctors'):
                    print(f"\nBác sĩ được đề xuất:")
                    for doc in msg_data['recommended_doctors']:
                        print(f"  - BS. {doc['name']} ({doc['specialty']})")
            else:
                print(f"✅ Bác sĩ được đề xuất - tự động lấy lịch")
        
        # Cleanup
        from ai_chatbox.models import ChatSession
        ChatSession.objects.filter(session_id=session_id).delete()
        print(f"\n✅ Đã xóa test session")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_full_flow()
