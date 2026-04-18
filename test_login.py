#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quan_ly_phong_kham.settings')
sys.path.append('.')
django.setup()

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from tai_khoan.models import HoSoBenhNhan, HoSoBacSi

def test_login():
    print("Testing login process...")
    
    # Test authentication
    try:
        user = authenticate(username='admin', password='admin123')
        if user:
            print(f"✓ Authentication successful for admin")
            print(f"  User ID: {user.id}")
            print(f"  Username: {user.username}")
            print(f"  Is staff: {user.is_staff}")
            print(f"  Is active: {user.is_active}")
            
            # Test profile access
            try:
                if hasattr(user, 'ho_so_benh_nhan'):
                    profile = user.ho_so_benh_nhan
                    print(f"  Has patient profile: {profile}")
                elif hasattr(user, 'ho_so_bac_si'):
                    profile = user.ho_so_bac_si
                    print(f"  Has doctor profile: {profile}")
                else:
                    print(f"  No profile (admin user)")
            except Exception as e:
                print(f"✗ Error accessing profile: {e}")
                
        else:
            print("✗ Authentication failed for admin")
    except Exception as e:
        print(f"✗ Error during authentication: {e}")
    
    # Test a sample patient
    try:
        user = authenticate(username='bn_phamvan', password='123456')
        if user:
            print(f"✓ Authentication successful for bn_phamvan")
            try:
                if hasattr(user, 'ho_so_benh_nhan'):
                    profile = user.ho_so_benh_nhan
                    print(f"  Patient profile: {profile.nguoi_dung.get_full_name()}")
                else:
                    print(f"  No patient profile found")
            except Exception as e:
                print(f"✗ Error accessing patient profile: {e}")
        else:
            print("✗ Authentication failed for bn_phamvan")
    except Exception as e:
        print(f"✗ Error during patient authentication: {e}")

if __name__ == '__main__':
    test_login()