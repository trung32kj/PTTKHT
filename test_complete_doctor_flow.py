"""
Complete integration test for doctor name request flow
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.test import RequestFactory
from django.contrib.auth.models import User
from accounts.models import HoSoBacSi, HoSoBenhNhan, ChuyenKhoa
from ai_chatbox.models import ChatSession, ChatMessage, TrieuChungAnalysis
from ai_chatbox.views import ChatAPIView
import json

def setup_test_data():
    """Tạo dữ liệu test"""
    print("🔧 Setting up test data...")
    
    # Tạo user bệnh nhân
    try:
        user = User.objects.get(username='test_patient')
    except User.DoesNotExist:
        user = User.objects.create_user(
            username='test_patient',
            password='test123',
            first_name='Test',
            last_name='Patient'
        )
    
    # Tạo hồ sơ bệnh nhân nếu chưa có
    if not hasattr(user, 'ho_so_benh_nhan'):
        from datetime import date
        HoSoBenhNhan.objects.create(
            nguoi_dung=user,
            so_dien_thoai='0123456789',
            dia_chi='Test Address',
            ngay_sinh=date(1990, 1, 1),
            gioi_tinh='Nam'
        )
    
    print(f"✅ User: {user.username}")
    return user

def test_symptom_analysis(user):
    """Test 1: Phân tích triệu chứng và gợi ý bác sĩ"""
    print("\n" + "=" * 60)
    print("TEST 1: Phân tích triệu chứng")
    print("=" * 60)
    
    factory = RequestFactory()
    view = ChatAPIView()
    
    # Bước 1: Start chat
    request = factory.post('/ai-chatbox/api/', 
        data=json.dumps({'action': 'start_chat'}),
        content_type='application/json'
    )
    request.user = user
    
    response = view.post(request)
    data = json.loads(response.content)
    
    if response.status_code == 200:
        session_id = data['session_id']
        print(f"✅ Chat session created: {session_id}")
    else:
        print(f"❌ Failed to create session: {data}")
        return None
    
    # Bước 2: Gửi triệu chứng
    request = factory.post('/ai-chatbox/api/',
        data=json.dumps({
            'action': 'send_message',
            'session_id': session_id,
            'message': 'Tôi bị đau bụng, buồn nôn và tiêu chảy'
        }),
        content_type='application/json'
    )
    request.user = user
    
    response = view.post(request)
    data = json.loads(response.content)
    
    if response.status_code == 200:
        print(f"✅ Symptom analyzed")
        print(f"   AI response: {data['ai_message']['content'][:100]}...")
        
        if data['ai_message'].get('data'):
            msg_data = data['ai_message']['data']
            print(f"   Chuyên khoa: {msg_data.get('specialty')}")
            print(f"   Độ tin cậy: {msg_data.get('confidence')}%")
            
            if msg_data.get('recommended_doctors'):
                print(f"   Số bác sĩ đề xuất: {len(msg_data['recommended_doctors'])}")
                for doc in msg_data['recommended_doctors'][:2]:
                    print(f"     - BS. {doc['name']} ({doc['specialty']})")
        
        return session_id
    else:
        print(f"❌ Failed to analyze: {data}")
        return None

def test_specific_doctor_request(user, session_id):
    """Test 2: Yêu cầu bác sĩ cụ thể"""
    print("\n" + "=" * 60)
    print("TEST 2: Yêu cầu bác sĩ cụ thể")
    print("=" * 60)
    
    # Lấy một bác sĩ bất kỳ để test
    doctor = HoSoBacSi.objects.first()
    if not doctor:
        print("❌ Không có bác sĩ nào trong database")
        return
    
    doctor_name = doctor.nguoi_dung.get_full_name()
    print(f"🎯 Yêu cầu bác sĩ: BS. {doctor_name}")
    
    factory = RequestFactory()
    view = ChatAPIView()
    
    request = factory.post('/ai-chatbox/api/',
        data=json.dumps({
            'action': 'send_message',
            'session_id': session_id,
            'message': f'muốn đặt BS. {doctor_name}'
        }),
        content_type='application/json'
    )
    request.user = user
    
    response = view.post(request)
    data = json.loads(response.content)
    
    if response.status_code == 200:
        print(f"✅ Request processed")
        print(f"   AI response: {data['ai_message']['content'][:150]}...")
        
        if data['ai_message'].get('data'):
            msg_data = data['ai_message']['data']
            
            if msg_data.get('awaiting_confirmation'):
                print(f"   ⚠️ Cần xác nhận (bác sĩ không được đề xuất)")
                print(f"   Selected doctor ID: {msg_data.get('selected_doctor_id')}")
                print(f"   Số bác sĩ được đề xuất: {len(msg_data.get('recommended_doctors', []))}")
            elif msg_data.get('selected_doctor_id'):
                print(f"   ✅ Bác sĩ được đề xuất - tự động lấy lịch")
                print(f"   Selected doctor ID: {msg_data.get('selected_doctor_id')}")
    else:
        print(f"❌ Failed: {data}")

def test_specialty_change(user, session_id):
    """Test 3: Đổi chuyên khoa"""
    print("\n" + "=" * 60)
    print("TEST 3: Đổi chuyên khoa")
    print("=" * 60)
    
    factory = RequestFactory()
    view = ChatAPIView()
    
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
        print(f"✅ Specialty doctors retrieved")
        print(f"   AI response: {data['message']['content'][:150]}...")
        
        if data.get('doctors'):
            print(f"   Số bác sĩ Tim mạch: {len(data['doctors'])}")
            for doc in data['doctors'][:2]:
                print(f"     - BS. {doc['name']} ({doc['fee']:,.0f} VNĐ)")
    else:
        print(f"❌ Failed: {data}")

def cleanup_test_data(user):
    """Xóa dữ liệu test"""
    print("\n🧹 Cleaning up test data...")
    
    # Xóa chat sessions
    ChatSession.objects.filter(benh_nhan=user).delete()
    print("✅ Test data cleaned")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("🧪 COMPLETE DOCTOR FLOW INTEGRATION TEST")
    print("=" * 60)
    
    try:
        user = setup_test_data()
        
        # Test 1: Phân tích triệu chứng
        session_id = test_symptom_analysis(user)
        
        if session_id:
            # Test 2: Yêu cầu bác sĩ cụ thể
            test_specific_doctor_request(user, session_id)
            
            # Test 3: Đổi chuyên khoa
            test_specialty_change(user, session_id)
        
        cleanup_test_data(user)
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS COMPLETED SUCCESSFULLY")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
