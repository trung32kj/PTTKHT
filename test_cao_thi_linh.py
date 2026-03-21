"""
Test specific case: BS. Cao Thị Linh
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from ai_chatbox.views import ChatAPIView
from accounts.models import HoSoBacSi
from django.db.models import Q

def test_parse():
    """Test parse tên bác sĩ"""
    view = ChatAPIView()
    
    messages = [
        "tôi muốn gặp bác sĩ BS. Cao Thị Linh",
        "muốn đặt BS. Cao Thị Linh",
        "Cao Thị Linh được không",
    ]
    
    print("=" * 60)
    print("TEST PARSE: BS. Cao Thị Linh")
    print("=" * 60)
    
    for msg in messages:
        result = view.parse_doctor_request(msg)
        print(f"Input: '{msg}'")
        print(f"Parsed: '{result}'")
        print()

def test_search():
    """Test tìm bác sĩ"""
    print("=" * 60)
    print("TEST SEARCH: BS. Cao Thị Linh")
    print("=" * 60)
    
    # Kiểm tra bác sĩ có trong database không
    all_doctors = HoSoBacSi.objects.all()
    print(f"Tổng số bác sĩ: {all_doctors.count()}")
    
    # Tìm bác sĩ có tên Cao
    cao_doctors = HoSoBacSi.objects.filter(
        Q(nguoi_dung__first_name__icontains='cao') |
        Q(nguoi_dung__last_name__icontains='cao')
    )
    
    print(f"\nBác sĩ có tên 'Cao': {cao_doctors.count()}")
    for doc in cao_doctors:
        print(f"  - {doc.nguoi_dung.get_full_name()}")
        print(f"    First: {doc.nguoi_dung.first_name}")
        print(f"    Last: {doc.nguoi_dung.last_name}")
    
    # Tìm bác sĩ có tên Linh
    linh_doctors = HoSoBacSi.objects.filter(
        Q(nguoi_dung__first_name__icontains='linh') |
        Q(nguoi_dung__last_name__icontains='linh')
    )
    
    print(f"\nBác sĩ có tên 'Linh': {linh_doctors.count()}")
    for doc in linh_doctors:
        print(f"  - {doc.nguoi_dung.get_full_name()}")
        print(f"    First: {doc.nguoi_dung.first_name}")
        print(f"    Last: {doc.nguoi_dung.last_name}")
    
    # Tìm bác sĩ Cao Thị Linh
    print("\n" + "=" * 60)
    print("Tìm kiếm: 'cao thị linh'")
    print("=" * 60)
    
    doctor_name = "cao thị linh"
    
    # Cách 1: Tìm theo first_name hoặc last_name
    doctors = HoSoBacSi.objects.filter(
        Q(nguoi_dung__first_name__icontains=doctor_name) |
        Q(nguoi_dung__last_name__icontains=doctor_name)
    )
    
    print(f"Cách 1 (full name): {doctors.count()} kết quả")
    
    # Cách 2: Tìm theo từng phần
    if not doctors.exists():
        name_parts = doctor_name.split()
        print(f"Name parts: {name_parts}")
        
        # Thử tìm với first_name chứa phần đầu và last_name chứa phần cuối
        doctors = HoSoBacSi.objects.filter(
            Q(nguoi_dung__first_name__icontains=name_parts[0]) &
            Q(nguoi_dung__last_name__icontains=name_parts[-1])
        )
        
        print(f"Cách 2 (first + last): {doctors.count()} kết quả")
        
        # Nếu vẫn không có, thử tìm bất kỳ phần nào
        if not doctors.exists():
            query = Q()
            for part in name_parts:
                if len(part) > 1:
                    query |= Q(nguoi_dung__first_name__icontains=part)
                    query |= Q(nguoi_dung__last_name__icontains=part)
            doctors = HoSoBacSi.objects.filter(query)
            
            print(f"Cách 3 (any part): {doctors.count()} kết quả")
    
    if doctors.exists():
        print(f"\n✅ Tìm thấy {doctors.count()} bác sĩ:")
        for doc in doctors[:5]:
            print(f"  - {doc.nguoi_dung.get_full_name()}")
            print(f"    First: '{doc.nguoi_dung.first_name}'")
            print(f"    Last: '{doc.nguoi_dung.last_name}'")
            print(f"    Chuyên khoa: {doc.chuyen_khoa.ten if doc.chuyen_khoa else 'Đa khoa'}")
    else:
        print("\n❌ Không tìm thấy bác sĩ")

if __name__ == '__main__':
    test_parse()
    test_search()
