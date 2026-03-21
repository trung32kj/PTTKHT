#!/usr/bin/env python
"""
Test tính năng đổi bác sĩ và chọn chuyên khoa khác
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
import json

def test_specialty_doctors_api():
    """Test API lấy bác sĩ theo chuyên khoa"""
    print("=== TEST API CHỌN CHUYÊN KHOA ===")
    
    client = Client()
    
    # Tạo và login user
    user, created = User.objects.get_or_create(
        username='test_specialty_user',
        defaults={'email': 'specialty@test.com'}
    )
    client.force_login(user)
    
    # Tạo chat session
    response = client.post(
        reverse('ai_chatbox:chat_api'),
        data=json.dumps({'action': 'start_chat'}),
        content_type='application/json'
    )
    
    if response.status_code == 200:
        session_data = response.json()
        session_id = session_data['session_id']
        print(f"✅ Chat session created: {session_id}")
        
        # Test lấy bác sĩ Tim mạch
        response = client.post(
            reverse('ai_chatbox:chat_api'),
            data=json.dumps({
                'action': 'get_specialty_doctors',
                'session_id': session_id,
                'specialty': 'Tim mạch'
            }),
            content_type='application/json'
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Tim mạch doctors: {len(data.get('doctors', []))} bác sĩ")
            
            if data.get('doctors'):
                for doctor in data['doctors']:
                    print(f"   - {doctor['name']} ({doctor['specialty']}) - {doctor['fee']:,.0f} VNĐ")
        else:
            print(f"❌ Failed to get Tim mạch doctors: {response.content}")
        
        # Test lấy bác sĩ Da liễu
        response = client.post(
            reverse('ai_chatbox:chat_api'),
            data=json.dumps({
                'action': 'get_specialty_doctors',
                'session_id': session_id,
                'specialty': 'Da liễu'
            }),
            content_type='application/json'
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Da liễu doctors: {len(data.get('doctors', []))} bác sĩ")
        else:
            print(f"❌ Failed to get Da liễu doctors: {response.content}")
            
    else:
        print(f"❌ Failed to create chat session: {response.content}")
    
    # Cleanup
    if created:
        user.delete()

def test_doctor_warning_system():
    """Test hệ thống cảnh báo khi chọn bác sĩ không phù hợp"""
    print("\n=== TEST HỆ THỐNG CẢNH BÁO ===")
    
    from ai_chatbox.services import DoctorRecommendationService
    
    # Test với triệu chứng tim mạch nhưng chọn bác sĩ da liễu
    tim_mach_doctors = DoctorRecommendationService.get_top_doctors('Tim mạch')
    da_lieu_doctors = DoctorRecommendationService.get_top_doctors('Da liễu')
    
    if tim_mach_doctors and da_lieu_doctors:
        # Giả sử chọn bác sĩ da liễu cho triệu chứng tim mạch
        selected_doctor_id = da_lieu_doctors[0]['doctor'].id
        
        optimization_check = DoctorRecommendationService.check_doctor_optimization(
            selected_doctor_id, tim_mach_doctors
        )
        
        if not optimization_check['is_optimal']:
            print("✅ Hệ thống cảnh báo hoạt động:")
            print(f"   - Warning: {optimization_check['warning']}")
            print(f"   - Suggestion: {optimization_check['suggestion']}")
        else:
            print("❌ Hệ thống cảnh báo không hoạt động")
    else:
        print("⚠️ Không đủ dữ liệu để test")

def test_all_specialties():
    """Test tất cả chuyên khoa có bác sĩ"""
    print("\n=== TEST TẤT CẢ CHUYÊN KHOA ===")
    
    from ai_chatbox.services import DoctorRecommendationService
    
    specialties = [
        'Nội khoa', 'Tim mạch', 'Tai mũi họng', 'Da liễu', 'Mắt',
        'Răng hàm mặt', 'Thần kinh', 'Tiêu hóa', 'Ngoại khoa', 'Sản phụ khoa'
    ]
    
    total_doctors = 0
    
    for specialty in specialties:
        doctors = DoctorRecommendationService.get_top_doctors(specialty)
        doctor_count = len(doctors)
        total_doctors += doctor_count
        
        status = "✅" if doctor_count > 0 else "❌"
        print(f"{status} {specialty}: {doctor_count} bác sĩ")
        
        if doctors:
            # Hiển thị bác sĩ đầu tiên
            first_doctor = doctors[0]['doctor']
            print(f"   → BS. {first_doctor.nguoi_dung.get_full_name()} - {first_doctor.phi_kham:,.0f} VNĐ")
    
    print(f"\nTổng: {total_doctors} bác sĩ trong {len(specialties)} chuyên khoa")

def main():
    print("🔄 TEST TÍNH NĂNG ĐỔI BÁC SĨ")
    print("=" * 40)
    
    test_specialty_doctors_api()
    test_doctor_warning_system()
    test_all_specialties()
    
    print("\n" + "=" * 40)
    print("✅ Test hoàn tất!")
    print("\n🎯 Tính năng mới:")
    print("• Bệnh nhân có thể xem bác sĩ chuyên khoa khác")
    print("• Hệ thống cảnh báo khi chọn không phù hợp")
    print("• Hiển thị rõ bác sĩ được đề xuất vs không đề xuất")
    print("• Cho phép quay lại danh sách ban đầu")

if __name__ == '__main__':
    main()