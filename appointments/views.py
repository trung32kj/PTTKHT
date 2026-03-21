from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LichHen, LichLamViec
from accounts.models import HoSoBacSi, HoSoBenhNhan
from datetime import date

@login_required
def danh_sach_bac_si(request):
    chuyen_khoa_id = request.GET.get('specialty')
    bac_si_list = HoSoBacSi.objects.filter(nguoi_dung__is_active=True)
    
    if chuyen_khoa_id:
        bac_si_list = bac_si_list.filter(chuyen_khoa_id=chuyen_khoa_id)
    
    from accounts.models import ChuyenKhoa
    chuyen_khoa_list = ChuyenKhoa.objects.all()
    
    return render(request, 'appointments/danh_sach_bac_si.html', {'bac_si_list': bac_si_list, 'chuyen_khoa_list': chuyen_khoa_list})

@login_required
def lich_lam_viec_bac_si(request, bac_si_id):
    bac_si = get_object_or_404(HoSoBacSi, id=bac_si_id, nguoi_dung__is_active=True)
    lich_lam_viec = LichLamViec.objects.filter(bac_si=bac_si, ngay__gte=date.today(), con_trong=True).order_by('ngay', 'gio_bat_dau')
    
    return render(request, 'appointments/lich_lam_viec_bac_si.html', {'bac_si': bac_si, 'lich_lam_viec': lich_lam_viec})

@login_required
def dat_lich_kham(request, lich_lam_viec_id):
    lich_lam_viec = get_object_or_404(LichLamViec, id=lich_lam_viec_id)
    
    # Chỉ bệnh nhân mới có thể đặt lịch khám
    if not hasattr(request.user, 'ho_so_benh_nhan'):
        messages.error(request, 'Chỉ bệnh nhân mới có thể đặt lịch khám')
        return redirect('danh_sach_bac_si')
    
    if request.method == 'POST':
        trieu_chung = request.POST.get('symptoms', '')
        
        lich_hen_ton_tai = LichHen.objects.filter(
            lich_lam_viec=lich_lam_viec,
            trang_thai__in=['pending', 'approved']
        ).exists()
        
        if lich_hen_ton_tai:
            messages.error(request, 'Lịch này đã được đặt')
            return redirect('lich_lam_viec_bac_si', bac_si_id=lich_lam_viec.bac_si.id)
        
        lich_hen = LichHen.objects.create(
            benh_nhan=request.user.ho_so_benh_nhan,
            bac_si=lich_lam_viec.bac_si,
            lich_lam_viec=lich_lam_viec,
            ngay=lich_lam_viec.ngay,
            gio=lich_lam_viec.gio_bat_dau,
            trieu_chung=trieu_chung
        )
        
        lich_lam_viec.con_trong = False
        lich_lam_viec.save()
        
        messages.success(request, 'Đặt lịch thành công! Vui lòng chờ bác sĩ xác nhận.')
        return redirect('lich_hen_cua_toi')
    
    return render(request, 'appointments/dat_lich_kham.html', {'lich_lam_viec': lich_lam_viec})

@login_required
def lich_hen_cua_toi(request):
    if hasattr(request.user, 'ho_so_benh_nhan'):
        lich_hen = LichHen.objects.filter(benh_nhan=request.user.ho_so_benh_nhan).order_by('-ngay', '-gio')
    elif hasattr(request.user, 'ho_so_bac_si'):
        lich_hen = LichHen.objects.filter(bac_si=request.user.ho_so_bac_si).order_by('-ngay', '-gio')
    else:
        lich_hen = LichHen.objects.all().order_by('-ngay', '-gio')
    
    return render(request, 'appointments/lich_hen_cua_toi.html', {'lich_hen': lich_hen})

@login_required
def huy_lich_hen(request, lich_hen_id):
    lich_hen = get_object_or_404(LichHen, id=lich_hen_id)
    
    if hasattr(request.user, 'ho_so_benh_nhan') and lich_hen.benh_nhan != request.user.ho_so_benh_nhan:
        messages.error(request, 'Bạn không có quyền hủy lịch này')
        return redirect('lich_hen_cua_toi')
    
    lich_hen.trang_thai = 'canceled'
    lich_hen.save()
    
    lich_hen.lich_lam_viec.con_trong = True
    lich_hen.lich_lam_viec.save()
    
    messages.success(request, 'Đã hủy lịch hẹn')
    return redirect('lich_hen_cua_toi')

@login_required
def xac_nhan_lich_hen(request, lich_hen_id):
    lich_hen = get_object_or_404(LichHen, id=lich_hen_id)
    
    if not hasattr(request.user, 'ho_so_bac_si') or lich_hen.bac_si != request.user.ho_so_bac_si:
        messages.error(request, 'Bạn không có quyền xác nhận lịch này')
        return redirect('lich_hen_cua_toi')
    
    lich_hen.trang_thai = 'approved'
    lich_hen.save()
    
    messages.success(request, 'Đã xác nhận lịch hẹn')
    return redirect('lich_hen_cua_toi')
@login_required
def dang_ky_lich_lam_viec(request):
    # Chỉ bác sĩ mới có thể đăng ký lịch làm việc
    if not hasattr(request.user, 'ho_so_bac_si'):
        messages.error(request, 'Chỉ bác sĩ mới có thể đăng ký lịch làm việc')
        return redirect('bang_dieu_khien')
    
    if request.method == 'POST':
        ngay = request.POST.get('ngay')
        gio_bat_dau = request.POST.get('gio_bat_dau')
        gio_ket_thuc = request.POST.get('gio_ket_thuc')
        
        # Kiểm tra trùng lịch
        lich_ton_tai = LichLamViec.objects.filter(
            bac_si=request.user.ho_so_bac_si,
            ngay=ngay,
            gio_bat_dau=gio_bat_dau
        ).exists()
        
        if lich_ton_tai:
            messages.error(request, 'Lịch làm việc này đã tồn tại')
        else:
            LichLamViec.objects.create(
                bac_si=request.user.ho_so_bac_si,
                ngay=ngay,
                gio_bat_dau=gio_bat_dau,
                gio_ket_thuc=gio_ket_thuc
            )
            messages.success(request, 'Đã đăng ký lịch làm việc thành công')
            return redirect('lich_lam_viec_cua_toi')
    
    return render(request, 'appointments/dang_ky_lich_lam_viec.html')

@login_required
def lich_lam_viec_cua_toi(request):
    # Chỉ bác sĩ mới có thể xem lịch làm việc của mình
    if not hasattr(request.user, 'ho_so_bac_si'):
        messages.error(request, 'Chỉ bác sĩ mới có thể xem lịch làm việc')
        return redirect('bang_dieu_khien')
    
    lich_lam_viec = LichLamViec.objects.filter(
        bac_si=request.user.ho_so_bac_si,
        ngay__gte=date.today()
    ).order_by('ngay', 'gio_bat_dau')
    
    return render(request, 'appointments/lich_lam_viec_cua_toi.html', {'lich_lam_viec': lich_lam_viec})