#!/usr/bin/env python
"""
Tạo bác sĩ mới và lịch khám cho hệ thống AI Chatbox
"""

import os
import django
from datetime import date, time, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import ChuyenKhoa, HoSoBacSi
from appointments.models import LichLamViec

def create_specialties():
    """Tạo các chuyên khoa"""
    print("=== TẠO CHUYÊN KHOA ===")
    
    specialties = [
        ('Nội khoa', 'Khám và điều trị các bệnh nội khoa tổng quát'),
        ('Tim mạch', 'Chuyên khoa tim mạch, huyết áp, nhịp tim'),
        ('Tai mũi họng', 'Khám và điều trị các bệnh về tai, mũi, họng'),
        ('Da liễu', 'Chuyên khoa da liễu, thẩm mỹ da'),
        ('Mắt', 'Khám và điều trị các bệnh về mắt'),
        ('Răng hàm mặt', 'Nha khoa, răng hàm mặt'),
        ('Thần kinh', 'Chuyên khoa thần kinh, não bộ'),
        ('Tiêu hóa', 'Khám và điều trị các bệnh về tiêu hóa'),
        ('Ngoại khoa', 'Phẫu thuật và các bệnh ngoại khoa'),
        ('Sản phụ khoa', 'Chuyên khoa sản phụ khoa')
    ]
    
    created_specialties = []
    for name, description in specialties:
        specialty, created = ChuyenKhoa.objects.get_or_create(
            ten=name,
            defaults={'mo_ta': description}
        )
        if created:
            print(f"✅ Tạo chuyên khoa: {name}")
        else:
            print(f"✅ Chuyên khoa đã tồn tại: {name}")
        created_specialties.append(specialty)
    
    return created_specialties

def create_doctors(specialties):
    """Tạo bác sĩ cho các chuyên khoa"""
    print("\n=== TẠO BÁC SĨ ===")
    
    doctors_data = [
        # Nội khoa
        ('BS001', 'Nguyễn', 'Văn Hùng', 'Nội khoa', 'Thạc sĩ Y khoa - Nội khoa', 250000),
        ('BS002', 'Trần', 'Thị Lan', 'Nội khoa', 'Tiến sĩ Y khoa - Nội khoa', 300000),
        
        # Tim mạch  
        ('BS003', 'Lê', 'Minh Tuấn', 'Tim mạch', 'Chuyên khoa II Tim mạch', 400000),
        ('BS004', 'Phạm', 'Thị Hoa', 'Tim mạch', 'Thạc sĩ Tim mạch', 350000),
        
        # Tai mũi họng
        ('BS005', 'Hoàng', 'Văn Nam', 'Tai mũi họng', 'Chuyên khoa I TMH', 280000),
        ('BS006', 'Vũ', 'Thị Mai', 'Tai mũi họng', 'Bác sĩ chuyên khoa TMH', 250000),
        
        # Da liễu
        ('BS007', 'Đỗ', 'Minh Đức', 'Da liễu', 'Thạc sĩ Da liễu', 320000),
        ('BS008', 'Bùi', 'Thị Nga', 'Da liễu', 'Bác sĩ Da liễu', 280000),
        
        # Mắt
        ('BS009', 'Đinh', 'Văn Tùng', 'Mắt', 'Chuyên khoa Mắt', 300000),
        ('BS010', 'Lý', 'Thị Hương', 'Mắt', 'Thạc sĩ Nhãn khoa', 350000),
        
        # Răng hàm mặt
        ('BS011', 'Phan', 'Văn Đạt', 'Răng hàm mặt', 'Bác sĩ Nha khoa', 200000),
        ('BS012', 'Cao', 'Thị Linh', 'Răng hàm mặt', 'Thạc sĩ Nha khoa', 250000),
        
        # Thần kinh
        ('BS013', 'Tạ', 'Minh Quang', 'Thần kinh', 'Tiến sĩ Thần kinh', 450000),
        ('BS014', 'Dương', 'Thị Yến', 'Thần kinh', 'Chuyên khoa II Thần kinh', 400000),
        
        # Tiêu hóa
        ('BS015', 'Mạc', 'Văn Hải', 'Tiêu hóa', 'Thạc sĩ Tiêu hóa', 320000),
        ('BS016', 'Từ', 'Thị Thảo', 'Tiêu hóa', 'Bác sĩ Tiêu hóa', 280000),
        
        # Ngoại khoa
        ('BS017', 'Lưu', 'Văn Kiên', 'Ngoại khoa', 'Chuyên khoa I Ngoại', 380000),
        ('BS018', 'Hồ', 'Thị Bích', 'Ngoại khoa', 'Thạc sĩ Ngoại khoa', 350000),
        
        # Sản phụ khoa
        ('BS019', 'Võ', 'Minh Tâm', 'Sản phụ khoa', 'Chuyên khoa II Sản', 400000),
        ('BS020', 'Đặng', 'Thị Xuân', 'Sản phụ khoa', 'Thạc sĩ Sản phụ khoa', 380000),
    ]
    
    created_doctors = []
    specialty_dict = {s.ten: s for s in specialties}
    
    for username, first_name, last_name, specialty_name, degree, fee in doctors_data:
        # Tạo user
        user, created = User.objects.get_or_create(
            username=username.lower(),
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'email': f'{username.lower()}@clinic.com',
                'is_active': True
            }
        )
        
        if created:
            user.set_password('123456')  # Password mặc định
            user.save()
            print(f"✅ Tạo user: {username}")
        
        # Tạo profile bác sĩ
        specialty = specialty_dict.get(specialty_name)
        doctor, created = HoSoBacSi.objects.get_or_create(
            nguoi_dung=user,
            defaults={
                'chuyen_khoa': specialty,
                'bang_cap': degree,
                'so_dien_thoai': f'09{username[2:]}0000',
                'phi_kham': fee,
                'mo_ta': f'Bác sĩ {specialty_name} với {degree}'
            }
        )
        
        if created:
            print(f"✅ Tạo bác sĩ: BS. {first_name} {last_name} - {specialty_name}")
        
        created_doctors.append(doctor)
    
    return created_doctors

def create_schedules(doctors):
    """Tạo lịch làm việc cho bác sĩ"""
    print("\n=== TẠO LỊCH LÀM VIỆC ===")
    
    # Tạo lịch cho 30 ngày tới
    start_date = date.today()
    
    # Khung giờ làm việc
    morning_slots = [
        (time(8, 0), time(8, 30)),
        (time(8, 30), time(9, 0)),
        (time(9, 0), time(9, 30)),
        (time(9, 30), time(10, 0)),
        (time(10, 0), time(10, 30)),
        (time(10, 30), time(11, 0)),
        (time(11, 0), time(11, 30)),
    ]
    
    afternoon_slots = [
        (time(14, 0), time(14, 30)),
        (time(14, 30), time(15, 0)),
        (time(15, 0), time(15, 30)),
        (time(15, 30), time(16, 0)),
        (time(16, 0), time(16, 30)),
        (time(16, 30), time(17, 0)),
        (time(17, 0), time(17, 30)),
    ]
    
    total_created = 0
    
    for doctor in doctors:
        doctor_schedules = 0
        
        for day_offset in range(30):  # 30 ngày tới
            work_date = start_date + timedelta(days=day_offset)
            
            # Bỏ qua chủ nhật
            if work_date.weekday() == 6:
                continue
            
            # Mỗi bác sĩ làm việc 4-5 ngày/tuần
            if day_offset % 7 in [0, 6]:  # Thứ 2 và chủ nhật nghỉ một số bác sĩ
                if hash(doctor.id + day_offset) % 3 == 0:  # 1/3 bác sĩ nghỉ
                    continue
            
            # Tạo lịch buổi sáng
            for start_time, end_time in morning_slots:
                schedule, created = LichLamViec.objects.get_or_create(
                    bac_si=doctor,
                    ngay=work_date,
                    gio_bat_dau=start_time,
                    defaults={
                        'gio_ket_thuc': end_time,
                        'con_trong': True
                    }
                )
                if created:
                    doctor_schedules += 1
            
            # Tạo lịch buổi chiều (không phải tất cả ngày)
            if work_date.weekday() not in [2, 4]:  # Thứ 4 và thứ 6 một số bác sĩ không làm chiều
                for start_time, end_time in afternoon_slots:
                    schedule, created = LichLamViec.objects.get_or_create(
                        bac_si=doctor,
                        ngay=work_date,
                        gio_bat_dau=start_time,
                        defaults={
                            'gio_ket_thuc': end_time,
                            'con_trong': True
                        }
                    )
                    if created:
                        doctor_schedules += 1
        
        total_created += doctor_schedules
        print(f"✅ Tạo {doctor_schedules} lịch cho BS. {doctor.nguoi_dung.get_full_name()}")
    
    print(f"\n✅ Tổng cộng tạo {total_created} lịch làm việc")

def create_sample_ratings(doctors):
    """Tạo đánh giá mẫu cho bác sĩ"""
    print("\n=== TẠO ĐÁNH GIÁ MẪU ===")
    
    from accounts.models import DanhGiaBacSi, HoSoBenhNhan
    import random
    
    # Lấy một số bệnh nhân để tạo đánh giá
    patients = HoSoBenhNhan.objects.all()[:5]
    
    if not patients:
        print("⚠️ Không có bệnh nhân để tạo đánh giá")
        return
    
    ratings_created = 0
    
    for doctor in doctors[:10]:  # Chỉ tạo cho 10 bác sĩ đầu
        for patient in patients:
            # Tạo đánh giá ngẫu nhiên
            rating_score = random.choice([4, 4, 5, 5, 5])  # Bias về điểm cao
            
            comments = [
                "Bác sĩ tận tình, khám rất kỹ",
                "Chuyên môn tốt, giải thích rõ ràng",
                "Thái độ tốt, điều trị hiệu quả",
                "Bác sĩ giỏi, tôi rất hài lòng",
                "Khám chính xác, thuốc hiệu quả"
            ]
            
            rating, created = DanhGiaBacSi.objects.get_or_create(
                bac_si=doctor,
                benh_nhan=patient,
                defaults={
                    'diem_so': rating_score,
                    'nhan_xet': random.choice(comments)
                }
            )
            
            if created:
                ratings_created += 1
    
    print(f"✅ Tạo {ratings_created} đánh giá mẫu")

def main():
    print("🏥 TẠO DỮ LIỆU BÁC SĨ VÀ LỊCH KHÁM")
    print("=" * 50)
    
    # Tạo chuyên khoa
    specialties = create_specialties()
    
    # Tạo bác sĩ
    doctors = create_doctors(specialties)
    
    # Tạo lịch làm việc
    create_schedules(doctors)
    
    # Tạo đánh giá mẫu
    create_sample_ratings(doctors)
    
    print("\n" + "=" * 50)
    print("🎉 HOÀN THÀNH TẠO DỮ LIỆU!")
    print(f"✅ Tạo {len(specialties)} chuyên khoa")
    print(f"✅ Tạo {len(doctors)} bác sĩ")
    print("✅ Tạo lịch làm việc cho 30 ngày tới")
    print("✅ Tạo đánh giá mẫu")
    print("\n🚀 Bây giờ AI Chatbox sẽ có đủ bác sĩ để gợi ý!")
    print("💡 Tất cả bác sĩ có password: 123456")

if __name__ == '__main__':
    main()