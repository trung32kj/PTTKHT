from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import date
from appointments.models import LichHen
from accounts.models import HoSoBenhNhan, HoSoBacSi

@login_required
def bang_dieu_khien(request):
    nguoi_dung = request.user
    context = {}
    
    if hasattr(nguoi_dung, 'ho_so_benh_nhan'):
        context['role'] = 'benh_nhan'
        context['lich_hen_sap_toi'] = LichHen.objects.filter(
            benh_nhan=nguoi_dung.ho_so_benh_nhan,
            ngay__gte=date.today(),
            trang_thai__in=['pending', 'approved']
        ).order_by('ngay', 'gio')[:5]
        context['tong_lich_hen'] = LichHen.objects.filter(benh_nhan=nguoi_dung.ho_so_benh_nhan).count()
        context['lich_hen_da_kham'] = LichHen.objects.filter(benh_nhan=nguoi_dung.ho_so_benh_nhan, trang_thai='completed').count()
        
    elif hasattr(nguoi_dung, 'ho_so_bac_si'):
        context['role'] = 'bac_si'
        hom_nay = date.today()
        context['lich_hen_hom_nay'] = LichHen.objects.filter(
            bac_si=nguoi_dung.ho_so_bac_si,
            ngay=hom_nay
        ).order_by('gio')
        context['lich_hen_cho_xac_nhan'] = LichHen.objects.filter(
            bac_si=nguoi_dung.ho_so_bac_si,
            trang_thai='pending'
        ).count()
        context['tong_benh_nhan'] = LichHen.objects.filter(
            bac_si=nguoi_dung.ho_so_bac_si
        ).values('benh_nhan').distinct().count()
        
        thang_dau = hom_nay.replace(day=1)
        context['lich_hen_thang_nay'] = LichHen.objects.filter(
            bac_si=nguoi_dung.ho_so_bac_si,
            ngay__gte=thang_dau,
            ngay__lte=hom_nay
        ).count()
        
    else:
        context['role'] = 'admin'
        hom_nay = date.today()
        thang_dau = hom_nay.replace(day=1)
        
        context['tong_benh_nhan'] = HoSoBenhNhan.objects.count()
        context['tong_bac_si'] = HoSoBacSi.objects.count()
        context['lich_hen_hom_nay'] = LichHen.objects.filter(ngay=hom_nay).count()
        context['lich_hen_thang_nay'] = LichHen.objects.filter(
            ngay__gte=thang_dau,
            ngay__lte=hom_nay
        ).count()
        
        context['top_bac_si'] = HoSoBacSi.objects.annotate(
            so_lich_hen=Count('lich_hen')
        ).order_by('-so_lich_hen')[:5]
        
        context['so_cho_xac_nhan'] = LichHen.objects.filter(trang_thai='pending').count()
        context['so_da_xac_nhan'] = LichHen.objects.filter(trang_thai='approved').count()
        context['so_da_kham'] = LichHen.objects.filter(trang_thai='completed').count()
        context['so_da_huy'] = LichHen.objects.filter(trang_thai='canceled').count()
    
    return render(request, 'dashboard/bang_dieu_khien.html', context)
