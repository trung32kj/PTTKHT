#!/usr/bin/env python
"""
Tạo dữ liệu mẫu cho hệ thống phòng khám - Phiên bản cập nhật
"""

import os
import sys
import random
from datetime import datetime, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quan_ly_phong_kham.settings')

import django
django.setup()

from django.contrib.auth.models import User
from tai_khoan.models import ChuyenKhoa, HoSoBacSi, HoSoBenhNhan
from lich_hen.models import LichLamViec
from ho_so_benh_an.models import Thuoc

def xoa_du_lieu_cu():
    """Xóa dữ liệu cũ"""
    
    print("🗑️  XÓA DỮ LIỆU CŨ...")
    
    # Xóa theo thứ tự để tránh lỗi foreign key
    from ho_so_benh_an.models import ToaThuoc, HoSoBenhAn
    from lich_hen.models import LichHen
    from tai_khoan.models import DanhGiaBacSi
    
    ToaThuoc.objects.all().delete()
    HoSoBenhAn.objects.all().delete()
    LichHen.objects.all().delete()
    LichLamViec.objects.all().delete()
    DanhGiaBacSi.objects.all().delete()
    HoSoBacSi.objects.all().delete()
    HoSoBenhNhan.objects.all().delete()
    Thuoc.objects.all().delete()
    ChuyenKhoa.objects.all().delete()
    
    # Xóa user trừ admin
    User.objects.exclude(username='admin').delete()
    
    print("   ✅ Đã xóa dữ liệu cũ")

def tao_admin():
    """Tạo tài khoản admin"""
    
    print("👑 TẠO ADMIN...")
    
    admin, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@phongkham.com',
            'first_name': 'Admin',
            'last_name': 'System',
            'is_staff': True,
            'is_superuser': True,
            'is_active': True
        }
    )
    
    admin.set_password('admin123')
    admin.save()
    
    if created:
        print("   ✅ Tạo admin: admin/admin123")
    else:
        print("   🔄 Reset admin password: admin123")

def tao_chuyen_khoa():
    """Tạo 15 chuyên khoa"""
    
    chuyen_khoa_list = [
        'Nội khoa',
        'Ngoại khoa', 
        'Tim mạch',
        'Da liễu',
        'Tai mũi họng',
        'Mắt',
        'Răng hàm mặt',
        'Thần kinh',
        'Tiêu hóa',
        'Sản phụ khoa',
        'Nhi khoa',
        'Chấn thương chỉnh hình',
        'Ung bướu',
        'Tâm thần',
        'Phục hồi chức năng'
    ]
    
    print("🏥 TẠO 15 CHUYÊN KHOA...")
    
    for ten in chuyen_khoa_list:
        chuyen_khoa, created = ChuyenKhoa.objects.get_or_create(
            ten=ten,
            defaults={'mo_ta': f'Chuyên khoa {ten}'}
        )
        if created:
            print(f"   ✅ {ten}")

def tao_bac_si():
    """Tạo 34 bác sĩ - mỗi chuyên khoa có 2-3 bác sĩ"""
    
    bac_si_list = [
        # Nội khoa (3 bác sĩ)
        ('bs_nguyenvan', 'Nguyễn', 'Văn An', 'Nội khoa', 'bs_nguyenvan@clinic.com'),
        ('bs_tranvan', 'Trần', 'Văn Bình', 'Nội khoa', 'bs_tranvan@clinic.com'),
        ('bs_lethi', 'Lê', 'Thị Cúc', 'Nội khoa', 'bs_lethi@clinic.com'),
        
        # Tim mạch (2 bác sĩ)
        ('bs_phamvan', 'Phạm', 'Văn Đức', 'Tim mạch', 'bs_phamvan@clinic.com'),
        ('bs_hoangthi', 'Hoàng', 'Thị Em', 'Tim mạch', 'bs_hoangthi@clinic.com'),
        
        # Ngoại khoa (3 bác sĩ)
        ('bs_vuvan', 'Vũ', 'Văn Phúc', 'Ngoại khoa', 'bs_vuvan@clinic.com'),
        ('bs_dangthi', 'Đặng', 'Thị Giang', 'Ngoại khoa', 'bs_dangthi@clinic.com'),
        ('bs_buivan', 'Bùi', 'Văn Hải', 'Ngoại khoa', 'bs_buivan@clinic.com'),
        
        # Da liễu (2 bác sĩ)
        ('bs_ngothi', 'Ngô', 'Thị Lan', 'Da liễu', 'bs_ngothi@clinic.com'),
        ('bs_lyvan', 'Lý', 'Văn Minh', 'Da liễu', 'bs_lyvan@clinic.com'),
        
        # Tai mũi họng (2 bác sĩ)
        ('bs_doivan', 'Đỗ', 'Văn Nam', 'Tai mũi họng', 'bs_doivan@clinic.com'),
        ('bs_vothi', 'Võ', 'Thị Oanh', 'Tai mũi họng', 'bs_vothi@clinic.com'),
        
        # Mắt (2 bác sĩ)
        ('bs_maithi', 'Mai', 'Thị Phương', 'Mắt', 'bs_maithi@clinic.com'),
        ('bs_caovan', 'Cao', 'Văn Quang', 'Mắt', 'bs_caovan@clinic.com'),
        
        # Răng hàm mặt (3 bác sĩ)
        ('bs_dinhvan', 'Đinh', 'Văn Rồng', 'Răng hàm mặt', 'bs_dinhvan@clinic.com'),
        ('bs_tranthi', 'Trần', 'Thị Sương', 'Răng hàm mặt', 'bs_tranthi@clinic.com'),
        ('bs_levan', 'Lê', 'Văn Tài', 'Răng hàm mặt', 'bs_levan@clinic.com'),
        
        # Thần kinh (2 bác sĩ)
        ('bs_phamthi', 'Phạm', 'Thị Uyên', 'Thần kinh', 'bs_phamthi@clinic.com'),
        ('bs_hoangvan', 'Hoàng', 'Văn Việt', 'Thần kinh', 'bs_hoangvan@clinic.com'),
        
        # Tiêu hóa (2 bác sĩ)
        ('bs_vuthi', 'Vũ', 'Thị Xuân', 'Tiêu hóa', 'bs_vuthi@clinic.com'),
        ('bs_dangvan', 'Đặng', 'Văn Yên', 'Tiêu hóa', 'bs_dangvan@clinic.com'),
        
        # Sản phụ khoa (3 bác sĩ)
        ('bs_buithi', 'Bùi', 'Thị Zung', 'Sản phụ khoa', 'bs_buithi@clinic.com'),
        ('bs_ngovan', 'Ngô', 'Văn An2', 'Sản phụ khoa', 'bs_ngovan@clinic.com'),
        ('bs_lythi', 'Lý', 'Thị Bình2', 'Sản phụ khoa', 'bs_lythi@clinic.com'),
        
        # Nhi khoa (2 bác sĩ)
        ('bs_doithi', 'Đỗ', 'Thị Cường2', 'Nhi khoa', 'bs_doithi@clinic.com'),
        ('bs_voivan', 'Võ', 'Văn Dũng2', 'Nhi khoa', 'bs_voivan@clinic.com'),
        
        # Chấn thương chỉnh hình (2 bác sĩ)
        ('bs_maivan', 'Mai', 'Văn Em2', 'Chấn thương chỉnh hình', 'bs_maivan@clinic.com'),
        ('bs_caothi', 'Cao', 'Thị Phúc2', 'Chấn thương chỉnh hình', 'bs_caothi@clinic.com'),
        
        # Ung bướu (2 bác sĩ)
        ('bs_dinhvan2', 'Đinh', 'Văn Giang2', 'Ung bướu', 'bs_dinhvan2@clinic.com'),
        ('bs_tranthi2', 'Trần', 'Thị Hoa2', 'Ung bướu', 'bs_tranthi2@clinic.com'),
        
        # Tâm thần (2 bác sĩ)
        ('bs_levan2', 'Lê', 'Văn Lan2', 'Tâm thần', 'bs_levan2@clinic.com'),
        ('bs_phamthi2', 'Phạm', 'Thị Minh2', 'Tâm thần', 'bs_phamthi2@clinic.com'),
        
        # Phục hồi chức năng (2 bác sĩ)
        ('bs_hoangvan2', 'Hoàng', 'Văn Nam2', 'Phục hồi chức năng', 'bs_hoangvan2@clinic.com'),
        ('bs_vuthi2', 'Vũ', 'Thị Oanh2', 'Phục hồi chức năng', 'bs_vuthi2@clinic.com'),
    ]
    
    print("👨‍⚕️ TẠO 34 BÁC SĨ...")
    
    for i, (username, ho, ten, chuyen_khoa_ten, email) in enumerate(bac_si_list):
        # Tạo User
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'first_name': ten,
                'last_name': ho,
                'is_staff': True,
                'is_active': True
            }
        )
        
        if created:
            user.set_password('123456')
            user.save()
        
        # Lấy chuyên khoa
        try:
            chuyen_khoa = ChuyenKhoa.objects.get(ten=chuyen_khoa_ten)
        except ChuyenKhoa.DoesNotExist:
            continue
        
        # Tạo hồ sơ bác sĩ với ảnh đại diện
        anh_file = f"bac_si/bacsi_{username.replace('bs_', '')}.jpg"
        
        ho_so, created = HoSoBacSi.objects.get_or_create(
            nguoi_dung=user,
            defaults={
                'chuyen_khoa': chuyen_khoa,
                'bang_cap': f'Bác sĩ chuyên khoa {chuyen_khoa_ten}',
                'so_dien_thoai': f'0{random.randint(900000000, 999999999)}',
                'mo_ta': f'Bác sĩ {ho} {ten} có {random.randint(3, 20)} năm kinh nghiệm trong lĩnh vực {chuyen_khoa_ten}.',
                'phi_kham': random.randint(150000, 500000),
                'anh_dai_dien': anh_file
            }
        )
        
        if created:
            print(f"   ✅ BS. {ho} {ten} - {chuyen_khoa_ten}")

def tao_benh_nhan():
    """Tạo 10 bệnh nhân"""
    
    benh_nhan_list = [
        ('bn_nguyenthi', 'Nguyễn', 'Thị Hoa', 'F', 'bn_nguyenthi@patient.com'),
        ('bn_tranvan', 'Trần', 'Văn Nam', 'M', 'bn_tranvan@patient.com'),
        ('bn_lethi', 'Lê', 'Thị Mai', 'F', 'bn_lethi@patient.com'),
        ('bn_phamvan', 'Phạm', 'Văn Đức', 'M', 'bn_phamvan@patient.com'),
        ('bn_hoangthi', 'Hoàng', 'Thị Linh', 'F', 'bn_hoangthi@patient.com'),
        ('bn_vuvan', 'Vũ', 'Văn Tùng', 'M', 'bn_vuvan@patient.com'),
        ('bn_dangthi', 'Đặng', 'Thị Yến', 'F', 'bn_dangthi@patient.com'),
        ('bn_buivan', 'Bùi', 'Văn Khoa', 'M', 'bn_buivan@patient.com'),
        ('bn_ngothi', 'Ngô', 'Thị Lan', 'F', 'bn_ngothi@patient.com'),
        ('bn_lyvan', 'Lý', 'Văn Minh', 'M', 'bn_lyvan@patient.com'),
    ]
    
    print("🏥 TẠO 10 BỆNH NHÂN...")
    
    for i, (username, ho, ten, gioi_tinh, email) in enumerate(benh_nhan_list):
        # Tạo User
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'first_name': ten,
                'last_name': ho,
                'is_active': True
            }
        )
        
        if created:
            user.set_password('123456')
            user.save()
        
        # Tạo hồ sơ bệnh nhân với ảnh đại diện
        anh_file = f"benh_nhan/benhnhan_{username.replace('bn_', '')}.jpg"
        
        ho_so, created = HoSoBenhNhan.objects.get_or_create(
            nguoi_dung=user,
            defaults={
                'so_dien_thoai': f'0{random.randint(900000000, 999999999)}',
                'dia_chi': f'Địa chỉ {ho} {ten}',
                'ngay_sinh': datetime.now().date() - timedelta(days=random.randint(6570, 25550)),  # 18-70 tuổi
                'gioi_tinh': gioi_tinh,
                'anh_dai_dien': anh_file
            }
        )
        
        if created:
            print(f"   ✅ {ho} {ten}")

def tao_thuoc():
    """Tạo 15 loại thuốc"""
    
    thuoc_list = [
        ('Paracetamol 500mg', 'viên'),
        ('Amoxicillin 500mg', 'viên'),
        ('Ibuprofen 400mg', 'viên'),
        ('Omeprazole 20mg', 'viên'),
        ('Cetirizine 10mg', 'viên'),
        ('Metformin 500mg', 'viên'),
        ('Amlodipine 5mg', 'viên'),
        ('Atorvastatin 20mg', 'viên'),
        ('Losartan 50mg', 'viên'),
        ('Aspirin 100mg', 'viên'),
        ('Vitamin D3 1000IU', 'viên'),
        ('Calcium 500mg', 'viên'),
        ('Dexamethasone 0.5mg', 'viên'),
        ('Furosemide 40mg', 'viên'),
        ('Simvastatin 20mg', 'viên'),
    ]
    
    print("💊 TẠO 15 LOẠI THUỐC...")
    
    for ten, don_vi in thuoc_list:
        thuoc, created = Thuoc.objects.get_or_create(
            ten_thuoc=ten,
            defaults={'don_vi': don_vi}
        )
        
        if created:
            print(f"   ✅ {ten}")

def tao_lich_lam_viec():
    """Tạo lịch làm việc cho 34 bác sĩ trong 30 ngày tới"""
    
    print("📅 TẠO LỊCH LÀM VIỆC...")
    
    bac_si_list = HoSoBacSi.objects.all()
    
    # Tạo lịch cho 30 ngày tới
    for i in range(30):
        ngay = datetime.now().date() + timedelta(days=i)
        
        for bac_si in bac_si_list:
            # Mỗi bác sĩ làm việc 5/7 ngày trong tuần
            if random.random() < 0.7:  # 70% khả năng làm việc
                
                # Ca sáng
                if random.random() < 0.8:  # 80% có ca sáng
                    lich, created = LichLamViec.objects.get_or_create(
                        bac_si=bac_si,
                        ngay=ngay,
                        gio_bat_dau='08:00',
                        gio_ket_thuc='12:00',
                        defaults={'con_trong': True}
                    )
                
                # Ca chiều
                if random.random() < 0.6:  # 60% có ca chiều
                    lich, created = LichLamViec.objects.get_or_create(
                        bac_si=bac_si,
                        ngay=ngay,
                        gio_bat_dau='14:00',
                        gio_ket_thuc='18:00',
                        defaults={'con_trong': True}
                    )
    
    total_lich = LichLamViec.objects.count()
    print(f"   ✅ Tạo {total_lich} lịch làm việc")

def main():
    """Chạy tất cả"""
    
    print("🚀 TẠO DỮ LIỆU MẪU - PHIÊN BẢN CẬP NHẬT")
    print("=" * 60)
    
    try:
        xoa_du_lieu_cu()
        tao_admin()
        tao_chuyen_khoa()
        tao_bac_si()
        tao_benh_nhan()
        tao_thuoc()
        tao_lich_lam_viec()
        
        print("\n" + "=" * 60)
        print("✅ TẠO DỮ LIỆU THÀNH CÔNG!")
        
        # Thống kê
        print(f"📊 Thống kê:")
        print(f"   - Chuyên khoa: {ChuyenKhoa.objects.count()}")
        print(f"   - Bác sĩ: {HoSoBacSi.objects.count()}")
        print(f"   - Bệnh nhân: {HoSoBenhNhan.objects.count()}")
        print(f"   - Thuốc: {Thuoc.objects.count()}")
        print(f"   - Lịch làm việc: {LichLamViec.objects.count()}")
        
        print(f"\n📋 Tài khoản:")
        print(f"   - Admin: admin/admin123")
        print(f"   - Bác sĩ: bs_nguyenvan/123456 (và 33 bác sĩ khác)")
        print(f"   - Bệnh nhân: bn_nguyenthi/123456 (và 9 bệnh nhân khác)")
        
        print(f"\n🌐 Truy cập: http://127.0.0.1:8000/")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()