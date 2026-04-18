#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quan_ly_phong_kham.settings')
sys.path.append('.')
django.setup()

from django.contrib.auth.models import User
from tai_khoan.models import HoSoBenhNhan, HoSoBacSi

def check_users():
    print("Checking users in database:")
    users = User.objects.all()
    print(f"Total users: {users.count()}")
    
    for user in users:
        print(f"\nUser: {user.username}")
        print(f"  ID: {user.id}")
        print(f"  Name: {user.get_full_name()}")
        print(f"  Email: {user.email}")
        print(f"  Is staff: {user.is_staff}")
        print(f"  Is active: {user.is_active}")
        
        try:
            if hasattr(user, 'ho_so_benh_nhan'):
                profile = user.ho_so_benh_nhan
                print(f"  Patient profile: ✓")
            elif hasattr(user, 'ho_so_bac_si'):
                profile = user.ho_so_bac_si
                print(f"  Doctor profile: ✓ ({profile.chuyen_khoa.ten})")
            else:
                print(f"  Profile: None (admin)")
        except Exception as e:
            print(f"  Profile error: {e}")

if __name__ == '__main__':
    check_users()