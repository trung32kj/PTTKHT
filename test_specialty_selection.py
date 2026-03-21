"""
Test chức năng chọn chuyên khoa khác
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.test import RequestFactory
from accounts.models import HoSoBenhNhan
from ai_chatbox.views import ChatAPIView
import json

def test_specialty_selection():
    print("=" * 70)
    print("TEST: Chọn chuyên khoa khác")
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
        
        # Gửi triệu chứng
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
        
        print(f"✅ Chuyên khoa đề xuất: {data['ai_message']['data']['specialty']}")
        print(f"   Bác sĩ đề xuất:")
        for doc in data['ai_message']['data']['recommended_doctors']:
            print(f"     - BS. {doc['name']} ({doc['specialty']})")
        print()
        
        # Test chọn chuyên khoa khác
        print("BƯỚC 2: User click 'Xem bác sĩ chuyên khoa khác'")
        print("-" * 70)
        print("   Frontend sẽ gọi: showOtherSpecialties()")
        print("   Hiển thị danh sách 10 chuyên khoa")
        print()
        
        # Test chọn Tim mạch
        print("BƯỚC 3: User chọn chuyên khoa 'Tim mạch'")
        print("-" * 70)
        request = factory.post('/ai-chatbox/api/',
            data=json.dumps({
                'action': 'get_specialty_doctors',
                'session_id': session_id,
                'specialty': 'Tim mạch'
            }),
            content_type='application/json'
        )
        request.user = user
        response = view.post(request)
        data = json.loads(response.content)
        
        if response.status_code == 200:
            print(f"✅ API trả về thành công")
            print(f"   AI message: {data['message']['content'][:100]}...")
            
            if data.get('doctors'):
                print(f"\n   Số bác sĩ Tim mạch: {len(data['doctors'])}")
                for doc in data['doctors'][:3]:
                    print(f"     - BS. {doc['name']} ({doc['specialty']}) - {doc['fee']:,.0f} VNĐ")
                    print(f"       is_recommended: {doc.get('is_recommended', False)}")
                
                print(f"\n📋 Frontend sẽ:")
                print(f"   1. Hiển thị tin nhắn cảnh báo")
                print(f"   2. Gọi showWidgetDoctorSelection(doctors)")
                print(f"   3. User có thể click chọn bác sĩ")
                print(f"   4. Nếu chọn → Hiển thị xác nhận (vì không phải chuyên khoa đề xuất)")
            else:
                print(f"   ❌ Không có danh sách bác sĩ")
        else:
            print(f"❌ API lỗi: {data}")
        
        # Cleanup
        from ai_chatbox.models import ChatSession
        ChatSession.objects.filter(session_id=session_id).delete()
        
        print()
        print("=" * 70)
        print("✅ TEST HOÀN TẤT")
        print("=" * 70)
        print()
        print("💡 Để test trên UI:")
        print("   1. Mở chatbox")
        print("   2. Nhập triệu chứng")
        print("   3. Click nút '🔄 Xem bác sĩ chuyên khoa khác'")
        print("   4. Chọn chuyên khoa từ danh sách")
        print("   5. Kiểm tra có hiển thị bác sĩ không")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_specialty_selection()
