#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quan_ly_phong_kham.settings')
sys.path.append('.')
django.setup()

from django.contrib.contenttypes.models import ContentType

def check_content_types():
    print("Checking Django content types:")
    content_types = ContentType.objects.all().order_by('app_label', 'model')
    
    for ct in content_types:
        if ct.app_label in ['accounts', 'tai_khoan', 'ai_chatbox', 'hop_thoai_ai', 'appointments', 'lich_hen', 'medical_records', 'ho_so_benh_an', 'dashboard', 'bang_dieu_khien']:
            print(f"  {ct.app_label}.{ct.model}")
    
    print("\nLooking for old app labels:")
    old_content_types = ContentType.objects.filter(app_label__in=['accounts', 'ai_chatbox', 'appointments', 'medical_records', 'dashboard'])
    if old_content_types.exists():
        print("Found old content types:")
        for ct in old_content_types:
            print(f"  {ct.app_label}.{ct.model} (id: {ct.id})")
    else:
        print("No old content types found")

if __name__ == '__main__':
    check_content_types()