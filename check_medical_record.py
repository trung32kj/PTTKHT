#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from medical_records.models import HoSoBenhAn, ToaThuoc, Thuoc
from appointments.models import LichHen
from accounts.models import HoSoBacSi, HoSoBenhNhan

def main():
    print("=== KIỂM TRA BỆNH ÁN MẪU ===\n")
    
    # Kiểm tra bệnh án
    benh_an_list = HoSoBenhAn.objects.all()
    print(f"Tổng số bệnh án: {benh_an_list.count()}")
    
    if benh_an_list.exists():
        benh_an = benh_an_list.first()
        print(f"\n📋 THÔNG TIN BỆNH ÁN:")
        print(f"- Bác sĩ: {benh_an.lich_hen.bac_si.nguoi_dung.get_full_name()}")
        print(f"- Chuyên khoa: {benh_an.lich_hen.bac_si.chuyen_khoa.ten}")
        print(f"- Bệnh nhân: {benh_an.lich_hen.benh_nhan.nguoi_dung.get_full_name()}")
        print(f"- Ngày khám: {benh_an.lich_hen.ngay}")
        print(f"- Giờ khám: {benh_an.lich_hen.gio}")
        print(f"- Trạng thái: {benh_an.lich_hen.get_trang_thai_display()}")
        
        print(f"\n🩺 CHẨN ĐOÁN:")
        print(benh_an.chan_doan[:200] + "..." if len(benh_an.chan_doan) > 200 else benh_an.chan_doan)
        
        print(f"\n📝 GHI CHÚ:")
        print(benh_an.ghi_chu[:200] + "..." if len(benh_an.ghi_chu) > 200 else benh_an.ghi_chu)
        
        # Kiểm tra toa thuốc
        toa_thuoc_list = benh_an.toa_thuoc.all()
        print(f"\n💊 TOA THUỐC ({toa_thuoc_list.count()} loại thuốc):")
        for i, toa in enumerate(toa_thuoc_list, 1):
            print(f"{i}. {toa.thuoc.ten_thuoc}")
            print(f"   - Số lượng: {toa.so_luong} {toa.thuoc.don_vi}")
            print(f"   - Cách dùng: {toa.ghi_chu}")
            print()
    else:
        print("❌ Không tìm thấy bệnh án nào!")
    
    # Thống kê tổng quan
    print("=== THỐNG KÊ TỔNG QUAN ===")
    print(f"- Tổng số bác sĩ: {HoSoBacSi.objects.count()}")
    print(f"- Tổng số bệnh nhân: {HoSoBenhNhan.objects.count()}")
    print(f"- Tổng số lịch hẹn: {LichHen.objects.count()}")
    print(f"- Tổng số bệnh án: {HoSoBenhAn.objects.count()}")
    print(f"- Tổng số loại thuốc: {Thuoc.objects.count()}")
    print(f"- Tổng số toa thuốc: {ToaThuoc.objects.count()}")

if __name__ == "__main__":
    main()