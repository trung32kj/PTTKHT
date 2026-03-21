#!/usr/bin/env python
"""
Kiểm tra dữ liệu bác sĩ và lịch khám
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from accounts.models import ChuyenKhoa, HoSoBacSi, DanhGiaBacSi
from appointments.models import LichLamViec
from ai_chatbox.services import DoctorRecommendationService

def check_specialties():
    """Kiểm tra chuyên khoa"""
    print("=== CHUYÊN KHOA ===")
    specialties = ChuyenKhoa.objects.all()
    
    for specialty in specialties:
        doctor_count = HoSoBacSi.objects.filter(chuyen_khoa=specialty).count()
        print(f"✅ {specialty.ten}: {doctor_count} bác sĩ")
    
    print(f"Tổng: {specialties.count()} chuyên khoa")

def check_doctors():
    """Kiểm tra bác sĩ"""
    print("\n=== BÁC SĨ ===")
    doctors = HoSoBacSi.objects.all()
    
    for doctor in doctors[:10]:  # Hiển thị 10 bác sĩ đầu
        schedule_count = LichLamViec.objects.filter(bac_si=doctor, con_trong=True).count()
        rating_count = DanhGiaBacSi.objects.filter(bac_si=doctor).count()
        avg_rating = DanhGiaBacSi.objects.filter(bac_si=doctor).aggregate(
            avg=django.db.models.Avg('diem_so')
        )['avg']
        
        print(f"✅ BS. {doctor.nguoi_dung.get_full_name()}")
        print(f"   - Chuyên khoa: {doctor.chuyen_khoa.ten}")
        print(f"   - Phí khám: {doctor.phi_kham:,.0f} VNĐ")
        print(f"   - Lịch trống: {schedule_count}")
        print(f"   - Đánh giá: {rating_count} ({avg_rating:.1f}/5.0 sao)" if avg_rating else f"   - Đánh giá: {rating_count}")
        print()
    
    print(f"Tổng: {doctors.count()} bác sĩ")

def check_schedules():
    """Kiểm tra lịch làm việc"""
    print("=== LỊCH LÀM VIỆC ===")
    
    total_schedules = LichLamViec.objects.count()
    available_schedules = LichLamViec.objects.filter(con_trong=True).count()
    booked_schedules = LichLamViec.objects.filter(con_trong=False).count()
    
    print(f"✅ Tổng lịch: {total_schedules}")
    print(f"✅ Lịch trống: {available_schedules}")
    print(f"✅ Lịch đã đặt: {booked_schedules}")

def test_ai_recommendations():
    """Test gợi ý bác sĩ từ AI"""
    print("\n=== TEST GỢI Ý BÁC SĨ ===")
    
    test_cases = [
        'Nội khoa',
        'Tim mạch', 
        'Tai mũi họng',
        'Da liễu',
        'Mắt'
    ]
    
    for specialty in test_cases:
        recommendations = DoctorRecommendationService.get_top_doctors(specialty, limit=3)
        print(f"\n🔍 Chuyên khoa: {specialty}")
        
        if recommendations:
            for i, rec in enumerate(recommendations, 1):
                doctor = rec['doctor']
                print(f"  {i}. BS. {doctor.nguoi_dung.get_full_name()}")
                print(f"     - Rating: {rec['rating_score']}/5.0")
                print(f"     - Phí: {doctor.phi_kham:,.0f} VNĐ")
        else:
            print("  ❌ Không tìm thấy bác sĩ")

def main():
    print("📊 KIỂM TRA DỮ LIỆU HỆ THỐNG")
    print("=" * 40)
    
    check_specialties()
    check_doctors()
    check_schedules()
    test_ai_recommendations()
    
    print("\n" + "=" * 40)
    print("✅ Kiểm tra hoàn tất!")
    print("🚀 Hệ thống sẵn sàng cho AI Chatbox!")

if __name__ == '__main__':
    main()