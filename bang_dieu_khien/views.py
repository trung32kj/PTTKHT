from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import date, timedelta
from lich_hen.models import LichHen
from tai_khoan.models import HoSoBenhNhan, HoSoBacSi
import json

@login_required
def bang_dieu_khien(request):
    nguoi_dung = request.user
    context = {}
    hom_nay = date.today()
    
    if hasattr(nguoi_dung, 'ho_so_benh_nhan'):
        context['role'] = 'benh_nhan'
        context['lich_hen_sap_toi'] = LichHen.objects.filter(
            benh_nhan=nguoi_dung.ho_so_benh_nhan,
            ngay__gte=hom_nay,
            trang_thai__in=['pending', 'approved']
        ).order_by('ngay', 'gio')[:5]
        context['tong_lich_hen'] = LichHen.objects.filter(benh_nhan=nguoi_dung.ho_so_benh_nhan).count()
        context['lich_hen_da_kham'] = LichHen.objects.filter(benh_nhan=nguoi_dung.ho_so_benh_nhan, trang_thai='completed').count()
        context['lich_hen_huy'] = LichHen.objects.filter(benh_nhan=nguoi_dung.ho_so_benh_nhan, trang_thai='canceled').count()
        
        # Chart data: Last 7 days appointments
        chart_labels = []
        chart_values = []
        for i in range(6, -1, -1):
            day = hom_nay - timedelta(days=i)
            chart_labels.append(day.strftime('%d/%m'))
            count = LichHen.objects.filter(benh_nhan=nguoi_dung.ho_so_benh_nhan, ngay=day).count()
            chart_values.append(count)
        context['chart_data'] = json.dumps({'labels': chart_labels, 'values': chart_values})
        
    elif hasattr(nguoi_dung, 'ho_so_bac_si'):
        context['role'] = 'bac_si'
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
        
        # Chart data: Last 7 days appointments
        chart_labels = []
        chart_values = []
        for i in range(6, -1, -1):
            day = hom_nay - timedelta(days=i)
            chart_labels.append(day.strftime('%d/%m'))
            count = LichHen.objects.filter(bac_si=nguoi_dung.ho_so_bac_si, ngay=day).count()
            chart_values.append(count)
        context['chart_data'] = json.dumps({'labels': chart_labels, 'values': chart_values})
        
        # Status distribution
        status_counts = LichHen.objects.filter(bac_si=nguoi_dung.ho_so_bac_si).values('trang_thai').annotate(count=Count('id'))
        status_labels = []
        status_values = []
        status_map = {'pending': 'Chờ xác nhận', 'approved': 'Đã xác nhận', 'completed': 'Đã khám', 'canceled': 'Đã hủy'}
        for item in status_counts:
            status_labels.append(status_map.get(item['trang_thai'], item['trang_thai']))
            status_values.append(item['count'])
        context['status_data'] = json.dumps({'labels': status_labels, 'values': status_values})
        
    else:
        context['role'] = 'admin'
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
        
        # Chart data: Last 7 days appointments
        chart_labels = []
        chart_values = []
        for i in range(6, -1, -1):
            day = hom_nay - timedelta(days=i)
            chart_labels.append(day.strftime('%d/%m'))
            count = LichHen.objects.filter(ngay=day).count()
            chart_values.append(count)
        context['chart_data'] = json.dumps({'labels': chart_labels, 'values': chart_values})
        
        # Status distribution
        status_counts = LichHen.objects.values('trang_thai').annotate(count=Count('id'))
        status_labels = []
        status_values = []
        status_map = {'pending': 'Chờ xác nhận', 'approved': 'Đã xác nhận', 'completed': 'Đã khám', 'canceled': 'Đã hủy'}
        for item in status_counts:
            status_labels.append(status_map.get(item['trang_thai'], item['trang_thai']))
            status_values.append(item['count'])
        context['status_data'] = json.dumps({'labels': status_labels, 'values': status_values})
        
        context['so_cho_xac_nhan'] = LichHen.objects.filter(trang_thai='pending').count()
        context['so_da_xac_nhan'] = LichHen.objects.filter(trang_thai='approved').count()
        context['so_da_kham'] = LichHen.objects.filter(trang_thai='completed').count()
        context['so_da_huy'] = LichHen.objects.filter(trang_thai='canceled').count()
    
    return render(request, 'bang_dieu_khien/trang_chu_admin.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)
