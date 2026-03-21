#!/usr/bin/env python
"""
Kiểm tra user login và profile
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import HoSoBenhNhan, HoSoBacSi
from datetime import date

def check_users():
    """Kiểm tra users trong hệ thống"""
    print("=== KIỂM TRA USERS ===")
    
    users = User.objects.all()
    print(f"Tổng số users: {users.count()}")
    
    for user in users:
        print(f"\nUser: {user.username}")
        print(f"  - Email: {user.email}")
        print(f"  - Active: {user.is_active}")
        
        # Kiểm tra profile bệnh nhân
        try:
            benh_nhan = user.ho_so_benh_nhan
            print(f"  - Là bệnh nhân: ✅")
            print(f"    SĐT: {benh_nhan.so_dien_thoai}")
        except:
            print(f"  - Là bệnh nhân: ❌")
        
        # Kiểm tra profile bác sĩ
        try:
            bac_si = user.ho_so_bac_si
            print(f"  - Là bác sĩ: ✅")
            print(f"    Chuyên khoa: {bac_si.chuyen_khoa}")
        except:
            print(f"  - Là bác sĩ: ❌")

def create_test_patient():
    """Tạo bệnh nhân test"""
    print("\n=== TẠO BỆNH NHÂN TEST ===")
    
    # Tạo user
    user, created = User.objects.get_or_create(
        username='benhnhan_test',
        defaults={
            'first_name': 'Nguyễn',
            'last_name': 'Văn Test',
            'email': 'benhnhan@test.com',
            'is_active': True
        }
    )
    
    if created:
        user.set_password('123456')
        user.save()
        print(f"✅ Tạo user: {user.username}")
    else:
        print(f"✅ User đã tồn tại: {user.username}")
    
    # Tạo profile bệnh nhân
    benh_nhan, created = HoSoBenhNhan.objects.get_or_create(
        nguoi_dung=user,
        defaults={
            'ngay_sinh': date(1990, 1, 1),
            'gioi_tinh': 'M',
            'so_dien_thoai': '0123456789',
            'dia_chi': 'Hà Nội'
        }
    )
    
    if created:
        print(f"✅ Tạo profile bệnh nhân")
    else:
        print(f"✅ Profile bệnh nhân đã tồn tại")
    
    print(f"\n🎯 THÔNG TIN ĐĂNG NHẬP:")
    print(f"Username: {user.username}")
    print(f"Password: 123456")
    print(f"Sau khi đăng nhập, widget AI sẽ hiển thị ở góc dưới phải")

def main():
    print("🔍 KIỂM TRA ĐĂNG NHẬP")
    print("=" * 40)
    
    check_users()
    create_test_patient()
    
    print("\n" + "=" * 40)
    print("✅ Hoàn thành kiểm tra!")

if __name__ == '__main__':
    main()