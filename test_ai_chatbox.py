#!/usr/bin/env python
"""
Script test AI Chatbox
Chạy script này để kiểm tra các chức năng cơ bản
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import ChuyenKhoa, HoSoBacSi, HoSoBenhNhan
from ai_chatbox.services import OpenAIService, DoctorRecommendationService
from ai_chatbox.models import ChatSession
from datetime import date

def test_ai_service():
    """Test AI service phân tích triệu chứng"""
    print("=== Test AI Service ===")
    
    # Tạo chuyên khoa test nếu chưa có
    chuyen_khoa, created = ChuyenKhoa.objects.get_or_create(
        ten='Nội khoa',
        defaults={'mo_ta': 'Chuyên khoa nội tổng quát'}
    )
    if created:
        print("✓ Tạo chuyên khoa Nội khoa")
    
    # Test phân tích triệu chứng
    ai_service = OpenAIService()
    
    test_symptoms = [
        "Tôi bị đau đầu và sốt",
        "Đau ngực, khó thở",
        "Đau bụng, tiêu chảy",
        "Ho, đau họng"
    ]
    
    for symptom in test_symptoms:
        result = ai_service.analyze_symptoms(symptom)
        print(f"Triệu chứng: {symptom}")
        print(f"Chuyên khoa: {result['chuyen_khoa_de_xuat']}")
        print(f"Độ tin cậy: {result['do_tin_cay']}%")
        print("---")
    
    print("✓ AI Service hoạt động bình thường\n")

def test_doctor_recommendation():
    """Test gợi ý bác sĩ"""
    print("=== Test Doctor Recommendation ===")
    
    # Tạo bác sĩ test nếu chưa có
    user, created = User.objects.get_or_create(
        username='bacsi_test',
        defaults={
            'first_name': 'Nguyễn',
            'last_name': 'Văn A',
            'email': 'bacsi@test.com'
        }
    )
    
    chuyen_khoa = ChuyenKhoa.objects.first()
    
    bac_si, created = HoSoBacSi.objects.get_or_create(
        nguoi_dung=user,
        defaults={
            'chuyen_khoa': chuyen_khoa,
            'bang_cap': 'Bác sĩ đa khoa',
            'so_dien_thoai': '0123456789',
            'phi_kham': 200000
        }
    )
    if created:
        print("✓ Tạo bác sĩ test")
    
    # Test gợi ý
    doctor_service = DoctorRecommendationService()
    recommendations = doctor_service.get_top_doctors('Nội khoa', limit=3)
    
    print(f"Tìm thấy {len(recommendations)} bác sĩ:")
    for rec in recommendations:
        doctor = rec['doctor']
        print(f"- BS. {doctor.nguoi_dung.get_full_name()}")
        print(f"  Chuyên khoa: {doctor.chuyen_khoa.ten if doctor.chuyen_khoa else 'Đa khoa'}")
        print(f"  Phí khám: {doctor.phi_kham:,.0f} VNĐ")
        print(f"  Rating: {rec['rating_score']}/5.0")
    
    print("✓ Doctor Recommendation hoạt động bình thường\n")

def test_chat_session():
    """Test tạo chat session"""
    print("=== Test Chat Session ===")
    
    # Tạo user bệnh nhân test
    user, created = User.objects.get_or_create(
        username='benhnhan_test',
        defaults={
            'first_name': 'Trần',
            'last_name': 'Thị B',
            'email': 'benhnhan@test.com'
        }
    )
    
    benh_nhan, created = HoSoBenhNhan.objects.get_or_create(
        nguoi_dung=user,
        defaults={
            'ngay_sinh': date(1990, 1, 1),
            'gioi_tinh': 'F',
            'so_dien_thoai': '0987654321',
            'dia_chi': 'Hà Nội'
        }
    )
    if created:
        print("✓ Tạo bệnh nhân test")
    
    # Tạo chat session
    session = ChatSession.objects.create(
        benh_nhan=user,
        session_id='test_session_123'
    )
    print(f"✓ Tạo chat session: {session.session_id}")
    
    print("✓ Chat Session hoạt động bình thường\n")

def main():
    """Chạy tất cả test"""
    print("🚀 Bắt đầu test AI Chatbox...\n")
    
    try:
        test_ai_service()
        test_doctor_recommendation()
        test_chat_session()
        
        print("🎉 Tất cả test đều PASS!")
        print("✅ AI Chatbox sẵn sàng hoạt động!")
        
    except Exception as e:
        print(f"❌ Lỗi trong quá trình test: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()