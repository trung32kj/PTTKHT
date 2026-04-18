#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quan_ly_phong_kham.settings')
sys.path.append('.')
django.setup()

from tai_khoan.models import HoSoBenhNhan, HoSoBacSi, ChuyenKhoa

def check_model_meta():
    print("Checking model metadata:")
    print(f"HoSoBenhNhan._meta.db_table: {HoSoBenhNhan._meta.db_table}")
    print(f"HoSoBacSi._meta.db_table: {HoSoBacSi._meta.db_table}")
    print(f"ChuyenKhoa._meta.db_table: {ChuyenKhoa._meta.db_table}")
    
    print(f"\nHoSoBenhNhan._meta.app_label: {HoSoBenhNhan._meta.app_label}")
    print(f"HoSoBacSi._meta.app_label: {HoSoBacSi._meta.app_label}")
    print(f"ChuyenKhoa._meta.app_label: {ChuyenKhoa._meta.app_label}")

if __name__ == '__main__':
    check_model_meta()