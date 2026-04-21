from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg
from .models import LichHen, LichLamViec, ThongBao
from tai_khoan.models import HoSoBacSi, HoSoBenhNhan
from datetime import date

@login_required
def danh_sach_bac_si(request):
    chuyen_khoa_id = request.GET.get('specialty')
    bac_si_list = HoSoBacSi.objects.filter(
        nguoi_dung__is_active=True
    ).annotate(
        diem_trung_binh=Avg('danh_gia__diem_so')
    ).order_by('-diem_trung_binh')
    
    if chuyen_khoa_id:
        bac_si_list = bac_si_list.filter(chuyen_khoa_id=chuyen_khoa_id)
    
    from tai_khoan.models import ChuyenKhoa
    chuyen_khoa_list = ChuyenKhoa.objects.all()
    
    # Phân trang: 21 bác sĩ mỗi trang
    paginator = Paginator(bac_si_list, 21)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'lich_hen/danh_sach_bac_si.html', {
        'bac_si_list': page_obj,
        'chuyen_khoa_list': chuyen_khoa_list,
        'page_obj': page_obj,
    })

@login_required
def lich_lam_viec_bac_si(request, bac_si_id):
    bac_si = get_object_or_404(HoSoBacSi, id=bac_si_id, nguoi_dung__is_active=True)
    lich_lam_viec = LichLamViec.objects.filter(bac_si=bac_si, ngay__gte=date.today(), con_trong=True).order_by('ngay', 'gio_bat_dau')
    
    return render(request, 'lich_hen/lich_lam_viec_bac_si.html', {'bac_si': bac_si, 'lich_lam_viec': lich_lam_viec})

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
        
        # Thông báo cho bác sĩ
        ThongBao.objects.create(
            nguoi_nhan=lich_lam_viec.bac_si.nguoi_dung,
            tieu_de='📅 Lịch hẹn mới',
            noi_dung=f'Bệnh nhân {request.user.get_full_name()} đã đặt lịch khám ngày {lich_lam_viec.ngay} lúc {lich_lam_viec.gio_bat_dau}.',
            loai='lich_hen_moi',
            lich_hen=lich_hen
        )
        
        messages.success(request, 'Đặt lịch thành công! Vui lòng chờ bác sĩ xác nhận.')
        return redirect('lich_hen_cua_toi')
    
    return render(request, 'lich_hen/dat_lich_kham.html', {'lich_lam_viec': lich_lam_viec})

@login_required
def lich_hen_cua_toi(request):
    if hasattr(request.user, 'ho_so_benh_nhan'):
        lich_hen = LichHen.objects.filter(benh_nhan=request.user.ho_so_benh_nhan).order_by('-ngay', '-gio')
    elif hasattr(request.user, 'ho_so_bac_si'):
        lich_hen = LichHen.objects.filter(bac_si=request.user.ho_so_bac_si).order_by('-ngay', '-gio')
    else:
        lich_hen = LichHen.objects.all().order_by('-ngay', '-gio')
    
    return render(request, 'lich_hen/lich_hen_cua_toi.html', {'lich_hen': lich_hen})

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
    
    # Thông báo cho bên còn lại
    if hasattr(request.user, 'ho_so_benh_nhan'):
        nguoi_nhan = lich_hen.bac_si.nguoi_dung
        nguoi_huy = f'Bệnh nhân {request.user.get_full_name()}'
    else:
        nguoi_nhan = lich_hen.benh_nhan.nguoi_dung
        nguoi_huy = f'BS. {request.user.get_full_name()}'
    
    ThongBao.objects.create(
        nguoi_nhan=nguoi_nhan,
        tieu_de='❌ Lịch hẹn bị hủy',
        noi_dung=f'{nguoi_huy} đã hủy lịch hẹn ngày {lich_hen.ngay} lúc {lich_hen.gio}.',
        loai='huy',
        lich_hen=lich_hen
    )
    
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
    
    # Thông báo cho bệnh nhân
    ThongBao.objects.create(
        nguoi_nhan=lich_hen.benh_nhan.nguoi_dung,
        tieu_de='✅ Lịch hẹn đã xác nhận',
        noi_dung=f'BS. {request.user.get_full_name()} đã xác nhận lịch hẹn ngày {lich_hen.ngay} lúc {lich_hen.gio}.',
        loai='xac_nhan',
        lich_hen=lich_hen
    )
    
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
    
    return render(request, 'lich_hen/dang_ky_lich_lam_viec.html')

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
    
    return render(request, 'lich_hen/lich_lam_viec_cua_toi.html', {'lich_lam_viec': lich_lam_viec})


@login_required
def doc_thong_bao(request):
    """Đánh dấu tất cả thông báo là đã đọc khi mở dropdown"""
    if request.method == 'POST':
        ThongBao.objects.filter(
            nguoi_nhan=request.user,
            da_doc=False
        ).update(da_doc=True)
        from django.http import JsonResponse
        return JsonResponse({'status': 'ok'})
    from django.http import JsonResponse
    return JsonResponse({'status': 'error'}, status=405)