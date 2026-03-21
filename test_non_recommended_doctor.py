"""
Test yêu cầu bác sĩ không được đề xuất
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

def test_non_recommended():
    print("=" * 60)
    print("TEST: Yêu cầu bác sĩ KHÔNG được đề xuất")
    print("=" * 60)
    
    try:
        benh_nhan = HoSoBenhNhan.objects.first()
        user = benh_nhan.nguoi_dung
        print(f"✅ User: {user.username}\n")
        
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
        
        # Gửi triệu chứng đau răng
        print("BƯỚC 1: Triệu chứng đau răng")
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
        
        print(f"Chuyên khoa đề xuất: {data['ai_message']['data'].get('specialty')}")
        print(f"Bác sĩ đề xuất:")
        for doc in data['ai_message']['data']['recommended_doctors']:
            print(f"  - BS. {doc['name']} ({doc['specialty']})")
        print()
        
        # Yêu cầu bác sĩ Tim mạch (không phù hợp với đau răng)
        print("BƯỚC 2: Yêu cầu BS. Văn A Nguyễn (Tim mạch)")
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
        
        print(f"\nAI Response:")
        print("-" * 60)
        print(data['ai_message']['content'][:400])
        print("...")
        print("-" * 60)
        
        if data['ai_message'].get('data'):
            msg_data = data['ai_message']['data']
            
            if msg_data.get('awaiting_confirmation'):
                print(f"\n✅ Hệ thống yêu cầu xác nhận")
                print(f"   Selected Doctor ID: {msg_data['selected_doctor_id']}")
                print(f"   Is Recommended: {msg_data.get('is_recommended', False)}")
                
                if msg_data.get('recommended_doctors'):
                    print(f"\n   Bác sĩ được đề xuất để so sánh:")
                    for doc in msg_data['recommended_doctors']:
                        print(f"     - BS. {doc['name']} ({doc['specialty']}) - {doc['fee']:,.0f} VNĐ")
            else:
                print(f"\n❌ Không yêu cầu xác nhận (lỗi)")
        
        # Cleanup
        from ai_chatbox.models import ChatSession
        ChatSession.objects.filter(session_id=session_id).delete()
        print(f"\n✅ Test hoàn tất")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_non_recommended()
