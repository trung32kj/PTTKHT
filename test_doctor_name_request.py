"""
Test script for doctor name request functionality
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from ai_chatbox.views import ChatAPIView
from django.contrib.auth.models import User
from accounts.models import HoSoBacSi, HoSoBenhNhan
from ai_chatbox.models import ChatSession
import json

def test_parse_doctor_request():
    """Test parsing doctor name from message"""
    view = ChatAPIView()
    
    test_cases = [
        ("muốn đặt BS. Ánh Lê Thị Ngọc", "ánh lê thị ngọc"),
        ("đặt lịch bác sĩ Nguyễn Văn A", "nguyễn văn a"),
        ("khám với BS Trần Thị B", "trần thị b"),
        ("bác sĩ Hoàng Văn C được không", "hoàng văn c"),
        ("Lê Thị D khác được không", "lê thị d"),
    ]
    
    print("=" * 60)
    print("TEST: Parse Doctor Request")
    print("=" * 60)
    
    for message, expected in test_cases:
        result = view.parse_doctor_request(message)
        status = "✅" if result and expected in result.lower() else "❌"
        print(f"{status} Input: '{message}'")
        print(f"   Expected: '{expected}'")
        print(f"   Got: '{result}'")
        print()

def test_doctor_search():
    """Test searching for doctors by name"""
    print("=" * 60)
    print("TEST: Doctor Search")
    print("=" * 60)
    
    # Lấy một số bác sĩ mẫu
    doctors = HoSoBacSi.objects.all()[:5]
    
    if not doctors:
        print("❌ Không có bác sĩ nào trong database")
        return
    
    print(f"✅ Tìm thấy {doctors.count()} bác sĩ:")
    for doctor in doctors:
        full_name = doctor.nguoi_dung.get_full_name()
        first_name = doctor.nguoi_dung.first_name
        last_name = doctor.nguoi_dung.last_name
        specialty = doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'Đa khoa'
        
        print(f"\n  BS. {full_name}")
        print(f"  - First name: {first_name}")
        print(f"  - Last name: {last_name}")
        print(f"  - Chuyên khoa: {specialty}")
        print(f"  - Phí khám: {doctor.phi_kham:,.0f} VNĐ")
        
        # Test tìm kiếm
        search_results = HoSoBacSi.objects.filter(
            nguoi_dung__first_name__icontains=first_name
        ) | HoSoBacSi.objects.filter(
            nguoi_dung__last_name__icontains=last_name
        )
        
        print(f"  - Tìm thấy {search_results.count()} kết quả khi search")

def test_full_flow():
    """Test complete flow with a real user"""
    print("\n" + "=" * 60)
    print("TEST: Complete Flow")
    print("=" * 60)
    
    # Tìm user có hồ sơ bệnh nhân
    try:
        benh_nhan = HoSoBenhNhan.objects.first()
        if not benh_nhan:
            print("❌ Không có bệnh nhân nào trong database")
            return
        
        user = benh_nhan.nguoi_dung
        print(f"✅ Sử dụng user: {user.username}")
        
        # Tạo chat session
        session = ChatSession.objects.create(
            benh_nhan=user,
            session_id='test-session-123'
        )
        print(f"✅ Tạo chat session: {session.session_id}")
        
        # Test parse doctor request
        view = ChatAPIView()
        doctor_name = view.parse_doctor_request("muốn đặt BS. Ánh Lê Thị Ngọc")
        print(f"✅ Parse doctor name: '{doctor_name}'")
        
        # Tìm bác sĩ với logic cải tiến
        if doctor_name:
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
            
            if doctors.exists():
                doctor = doctors.first()
                print(f"✅ Tìm thấy bác sĩ: BS. {doctor.nguoi_dung.get_full_name()}")
                print(f"   - Chuyên khoa: {doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'Đa khoa'}")
                print(f"   - Tìm thấy {doctors.count()} kết quả")
            else:
                print(f"❌ Không tìm thấy bác sĩ với tên: {doctor_name}")
        
        # Cleanup
        session.delete()
        print("✅ Đã xóa test session")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    print("\n🧪 TESTING DOCTOR NAME REQUEST FUNCTIONALITY\n")
    
    test_parse_doctor_request()
    test_doctor_search()
    test_full_flow()
    
    print("\n" + "=" * 60)
    print("✅ TESTS COMPLETED")
    print("=" * 60)
