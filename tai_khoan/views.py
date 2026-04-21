from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import HoSoBenhNhan, HoSoBacSi, ChuyenKhoa

def dang_ky_benh_nhan(request):
    if request.method == 'POST':
        ten_dang_nhap = request.POST.get('username')
        mat_khau = request.POST.get('password')
        ho = request.POST.get('last_name')
        ten = request.POST.get('first_name')
        email = request.POST.get('email')
        ngay_sinh = request.POST.get('date_of_birth')
        gioi_tinh = request.POST.get('gender')
        so_dien_thoai = request.POST.get('phone')
        dia_chi = request.POST.get('address', '')
        
        if User.objects.filter(username=ten_dang_nhap).exists():
            messages.error(request, 'Tên đăng nhập đã tồn tại')
            return render(request, 'tai_khoan/dang_ky_benh_nhan.html')
        
        nguoi_dung = User.objects.create_user(username=ten_dang_nhap, password=mat_khau, email=email, first_name=ten, last_name=ho)
        ho_so = HoSoBenhNhan.objects.create(nguoi_dung=nguoi_dung, ngay_sinh=ngay_sinh, gioi_tinh=gioi_tinh, so_dien_thoai=so_dien_thoai, dia_chi=dia_chi)
        
        if 'anh_dai_dien' in request.FILES:
            ho_so.anh_dai_dien = request.FILES['anh_dai_dien']
            ho_so.save()
        
        messages.success(request, 'Đăng ký thành công! Vui lòng đăng nhập.')
        return redirect('dang_nhap')
    
    return render(request, 'tai_khoan/dang_ky_benh_nhan.html')

def dang_nhap(request):
    if request.method == 'POST':
        ten_dang_nhap = request.POST.get('username')
        mat_khau = request.POST.get('password')
        
        # Rate limiting: kiểm tra số lần đăng nhập sai
        from django.conf import settings
        from time import time
        
        cache_key = f'login_attempts_{ten_dang_nhap}'
        attempts = request.session.get(cache_key, {'count': 0, 'lockout_until': 0})
        
        # Kiểm tra lockout
        if attempts.get('lockout_until', 0) > time():
            remaining = int(attempts['lockout_until'] - time())
            messages.error(request, f'Tài khoản bị tạm khóa. Vui lòng thử lại sau {remaining} giây.')
            return render(request, 'tai_khoan/dang_nhap.html')
        
        nguoi_dung = authenticate(request, username=ten_dang_nhap, password=mat_khau)
        
        if nguoi_dung:
            # Reset attempts khi đăng nhập thành công
            request.session.pop(cache_key, None)
            login(request, nguoi_dung)
            
            # Phân quyền khi đăng nhập
            if hasattr(nguoi_dung, 'ho_so_benh_nhan'):
                messages.success(request, f'Chào mừng bệnh nhân {nguoi_dung.get_full_name()}!')
                return redirect('bang_dieu_khien')
            elif hasattr(nguoi_dung, 'ho_so_bac_si'):
                messages.success(request, f'Chào mừng bác sĩ {nguoi_dung.get_full_name()}!')
                return redirect('bang_dieu_khien')
            else:
                messages.success(request, f'Chào mừng admin {nguoi_dung.get_full_name()}!')
                return redirect('bang_dieu_khien')
        else:
            # Tăng số lần đăng nhập sai
            max_attempts = getattr(settings, 'MAX_LOGIN_ATTEMPTS', 5)
            lockout_duration = getattr(settings, 'LOCKOUT_DURATION', 300)
            
            attempts['count'] = attempts.get('count', 0) + 1
            if attempts['count'] >= max_attempts:
                attempts['lockout_until'] = time() + lockout_duration
                attempts['count'] = 0
                messages.error(request, f'Quá nhiều lần đăng nhập sai! Tài khoản bị tạm khóa {lockout_duration // 60} phút.')
            else:
                remaining = max_attempts - attempts['count']
                messages.error(request, f'Tên đăng nhập hoặc mật khẩu không đúng (còn {remaining} lần thử)')
            
            request.session[cache_key] = attempts
    
    return render(request, 'tai_khoan/dang_nhap.html')

@login_required
def dang_xuat(request):
    logout(request)
    return redirect('dang_nhap')

@login_required
def ho_so(request):
    nguoi_dung = request.user
    context = {'user': nguoi_dung}
    
    if hasattr(nguoi_dung, 'ho_so_benh_nhan'):
        context['profile'] = nguoi_dung.ho_so_benh_nhan
        context['role'] = 'benh_nhan'
    elif hasattr(nguoi_dung, 'ho_so_bac_si'):
        context['profile'] = nguoi_dung.ho_so_bac_si
        context['role'] = 'bac_si'
    else:
        context['role'] = 'admin'
    
    return render(request, 'tai_khoan/ho_so_ca_nhan.html', context)

@login_required
def quan_ly_bac_si(request):
    # Chỉ admin (is_staff=True) mới có quyền truy cập
    if not request.user.is_staff or hasattr(request.user, 'ho_so_benh_nhan') or hasattr(request.user, 'ho_so_bac_si'):
        messages.error(request, 'Bạn không có quyền truy cập trang này')
        return redirect('bang_dieu_khien')
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add_new':
            ten_dang_nhap = request.POST.get('username')
            mat_khau = request.POST.get('password')
            ho = request.POST.get('last_name')
            ten = request.POST.get('first_name')
            email = request.POST.get('email')
            chuyen_khoa_id = request.POST.get('chuyen_khoa')
            bang_cap = request.POST.get('bang_cap')
            so_dien_thoai = request.POST.get('so_dien_thoai')
            phi_kham = request.POST.get('phi_kham')
            mo_ta = request.POST.get('mo_ta', '')
            
            if User.objects.filter(username=ten_dang_nhap).exists():
                messages.error(request, 'Tên đăng nhập đã tồn tại')
            else:
                nguoi_dung = User.objects.create_user(
                    username=ten_dang_nhap,
                    password=mat_khau,
                    email=email,
                    first_name=ten,
                    last_name=ho,
                    is_staff=True
                )
                
                chuyen_khoa = ChuyenKhoa.objects.get(id=chuyen_khoa_id)
                ho_so = HoSoBacSi.objects.create(
                    nguoi_dung=nguoi_dung,
                    chuyen_khoa=chuyen_khoa,
                    bang_cap=bang_cap,
                    so_dien_thoai=so_dien_thoai,
                    phi_kham=phi_kham,
                    mo_ta=mo_ta
                )
                
                if 'anh_dai_dien' in request.FILES:
                    ho_so.anh_dai_dien = request.FILES['anh_dai_dien']
                    ho_so.save()
                
                messages.success(request, f'Đã thêm bác sĩ {ten} thành công!')
                return redirect('quan_ly_bac_si')
        
        elif action == 'add_existing':
            user_id = request.POST.get('user_id')
            chuyen_khoa_id = request.POST.get('chuyen_khoa')
            bang_cap = request.POST.get('bang_cap')
            so_dien_thoai = request.POST.get('so_dien_thoai')
            phi_kham = request.POST.get('phi_kham')
            mo_ta = request.POST.get('mo_ta', '')
            
            try:
                nguoi_dung = User.objects.get(id=user_id)
                if hasattr(nguoi_dung, 'ho_so_bac_si'):
                    messages.error(request, 'Tài khoản này đã là bác sĩ')
                else:
                    nguoi_dung.is_staff = True
                    nguoi_dung.save()
                    
                    chuyen_khoa = ChuyenKhoa.objects.get(id=chuyen_khoa_id)
                    ho_so = HoSoBacSi.objects.create(
                        nguoi_dung=nguoi_dung,
                        chuyen_khoa=chuyen_khoa,
                        bang_cap=bang_cap,
                        so_dien_thoai=so_dien_thoai,
                        phi_kham=phi_kham,
                        mo_ta=mo_ta
                    )
                    
                    if 'anh_dai_dien' in request.FILES:
                        ho_so.anh_dai_dien = request.FILES['anh_dai_dien']
                        ho_so.save()
                    
                    messages.success(request, f'Đã thêm {nguoi_dung.get_full_name()} làm bác sĩ!')
                    return redirect('quan_ly_bac_si')
            except User.DoesNotExist:
                messages.error(request, 'Tài khoản không tồn tại')
        
        elif action == 'delete':
            bac_si_id = request.POST.get('bac_si_id')
            try:
                ho_so = HoSoBacSi.objects.get(id=bac_si_id)
                ten = ho_so.nguoi_dung.get_full_name()
                ho_so.delete()
                messages.success(request, f'Đã xóa bác sĩ {ten}')
                return redirect('quan_ly_bac_si')
            except HoSoBacSi.DoesNotExist:
                messages.error(request, 'Bác sĩ không tồn tại')
        
        elif action == 'deactivate':
            bac_si_id = request.POST.get('bac_si_id')
            try:
                ho_so = HoSoBacSi.objects.get(id=bac_si_id)
                ho_so.nguoi_dung.is_active = False
                ho_so.nguoi_dung.save()
                messages.success(request, f'Đã tạm ngưng tài khoản {ho_so.nguoi_dung.get_full_name()}')
                return redirect('quan_ly_bac_si')
            except HoSoBacSi.DoesNotExist:
                messages.error(request, 'Bác sĩ không tồn tại')
        
        elif action == 'activate':
            bac_si_id = request.POST.get('bac_si_id')
            try:
                ho_so = HoSoBacSi.objects.get(id=bac_si_id)
                ho_so.nguoi_dung.is_active = True
                ho_so.nguoi_dung.save()
                messages.success(request, f'Đã kích hoạt tài khoản {ho_so.nguoi_dung.get_full_name()}')
                return redirect('quan_ly_bac_si')
            except HoSoBacSi.DoesNotExist:
                messages.error(request, 'Bác sĩ không tồn tại')
    
    bac_si_list = HoSoBacSi.objects.all()
    chuyen_khoa_list = ChuyenKhoa.objects.all()
    available_users = User.objects.filter(ho_so_benh_nhan__isnull=False, ho_so_bac_si__isnull=True)
    context = {
        'bac_si_list': bac_si_list,
        'chuyen_khoa_list': chuyen_khoa_list,
        'available_users': available_users
    }
    return render(request, 'tai_khoan/quan_ly_bac_si.html', context)

@login_required
def chinh_sua_ho_so(request):
    nguoi_dung = request.user
    
    if hasattr(nguoi_dung, 'ho_so_benh_nhan'):
        ho_so = nguoi_dung.ho_so_benh_nhan
        role = 'benh_nhan'
    elif hasattr(nguoi_dung, 'ho_so_bac_si'):
        ho_so = nguoi_dung.ho_so_bac_si
        role = 'bac_si'
    else:
        messages.error(request, 'Bạn không có hồ sơ để chỉnh sửa')
        return redirect('ho_so')
    
    if request.method == 'POST':
        nguoi_dung.first_name = request.POST.get('first_name', nguoi_dung.first_name)
        nguoi_dung.last_name = request.POST.get('last_name', nguoi_dung.last_name)
        nguoi_dung.email = request.POST.get('email', nguoi_dung.email)
        nguoi_dung.save()
        
        if role == 'benh_nhan':
            ho_so.so_dien_thoai = request.POST.get('so_dien_thoai', ho_so.so_dien_thoai)
            ho_so.dia_chi = request.POST.get('dia_chi', ho_so.dia_chi)
            if 'anh_dai_dien' in request.FILES:
                ho_so.anh_dai_dien = request.FILES['anh_dai_dien']
        else:
            ho_so.so_dien_thoai = request.POST.get('so_dien_thoai', ho_so.so_dien_thoai)
            ho_so.mo_ta = request.POST.get('mo_ta', ho_so.mo_ta)
            if 'anh_dai_dien' in request.FILES:
                ho_so.anh_dai_dien = request.FILES['anh_dai_dien']
        
        ho_so.save()
        messages.success(request, 'Cập nhật hồ sơ thành công!')
        return redirect('ho_so')
    
    context = {'profile': ho_so, 'role': role, 'user': nguoi_dung}
    return render(request, 'tai_khoan/chinh_sua_ho_so.html', context)


def quen_mat_khau(request):
    """Đặt lại mật khẩu khi quên"""
    if request.method == 'POST':
        ten_dang_nhap = request.POST.get('username')
        mat_khau_moi = request.POST.get('new_password')
        xac_nhan = request.POST.get('confirm_password')
        
        if mat_khau_moi != xac_nhan:
            messages.error(request, 'Mật khẩu xác nhận không khớp')
            return render(request, 'tai_khoan/quen_mat_khau.html')
        
        if len(mat_khau_moi) < 6:
            messages.error(request, 'Mật khẩu phải có ít nhất 6 ký tự')
            return render(request, 'tai_khoan/quen_mat_khau.html')
        
        try:
            nguoi_dung = User.objects.get(username=ten_dang_nhap)
            nguoi_dung.set_password(mat_khau_moi)
            nguoi_dung.save()
            messages.success(request, 'Đặt lại mật khẩu thành công! Vui lòng đăng nhập.')
            return redirect('dang_nhap')
        except User.DoesNotExist:
            messages.error(request, 'Tên đăng nhập không tồn tại')
    
    return render(request, 'tai_khoan/quen_mat_khau.html')


@login_required
def doi_mat_khau(request):
    """Đổi mật khẩu cho user đã đăng nhập"""
    if request.method == 'POST':
        mat_khau_cu = request.POST.get('old_password')
        mat_khau_moi = request.POST.get('new_password')
        xac_nhan = request.POST.get('confirm_password')
        
        if not request.user.check_password(mat_khau_cu):
            messages.error(request, 'Mật khẩu hiện tại không đúng')
            return render(request, 'tai_khoan/doi_mat_khau.html')
        
        if mat_khau_moi != xac_nhan:
            messages.error(request, 'Mật khẩu xác nhận không khớp')
            return render(request, 'tai_khoan/doi_mat_khau.html')
        
        if len(mat_khau_moi) < 6:
            messages.error(request, 'Mật khẩu mới phải có ít nhất 6 ký tự')
            return render(request, 'tai_khoan/doi_mat_khau.html')
        
        request.user.set_password(mat_khau_moi)
        request.user.save()
        
        # Đăng nhập lại sau khi đổi mật khẩu
        from django.contrib.auth import update_session_auth_hash
        update_session_auth_hash(request, request.user)
        
        messages.success(request, 'Đổi mật khẩu thành công!')
        return redirect('ho_so')
    
    return render(request, 'tai_khoan/doi_mat_khau.html')


@login_required
def danh_gia_bac_si(request, bac_si_id):
    """Bệnh nhân đánh giá bác sĩ sau khi khám"""
    if not hasattr(request.user, 'ho_so_benh_nhan'):
        messages.error(request, 'Chỉ bệnh nhân mới có thể đánh giá bác sĩ')
        return redirect('bang_dieu_khien')
    
    try:
        bac_si = HoSoBacSi.objects.get(id=bac_si_id)
    except HoSoBacSi.DoesNotExist:
        messages.error(request, 'Bác sĩ không tồn tại')
        return redirect('bang_dieu_khien')
    
    benh_nhan = request.user.ho_so_benh_nhan
    
    # Kiểm tra đã có lịch hẹn completed với bác sĩ này chưa
    from lich_hen.models import LichHen
    da_kham = LichHen.objects.filter(
        benh_nhan=benh_nhan,
        bac_si=bac_si,
        trang_thai='completed'
    ).exists()
    
    if not da_kham:
        messages.error(request, 'Bạn cần hoàn thành lịch khám với bác sĩ trước khi đánh giá')
        return redirect('lich_hen_cua_toi')
    
    from .models import DanhGiaBacSi
    
    # Kiểm tra đã đánh giá chưa
    danh_gia_cu = DanhGiaBacSi.objects.filter(bac_si=bac_si, benh_nhan=benh_nhan).first()
    
    if request.method == 'POST':
        diem_so = int(request.POST.get('diem_so', 5))
        nhan_xet = request.POST.get('nhan_xet', '')
        
        if diem_so < 1 or diem_so > 5:
            diem_so = 5
        
        if danh_gia_cu:
            danh_gia_cu.diem_so = diem_so
            danh_gia_cu.nhan_xet = nhan_xet
            danh_gia_cu.save()
            messages.success(request, 'Cập nhật đánh giá thành công!')
        else:
            DanhGiaBacSi.objects.create(
                bac_si=bac_si,
                benh_nhan=benh_nhan,
                diem_so=diem_so,
                nhan_xet=nhan_xet
            )
            messages.success(request, 'Đánh giá bác sĩ thành công!')
        
        return redirect('lich_hen_cua_toi')
    
    context = {
        'bac_si': bac_si,
        'danh_gia_cu': danh_gia_cu,
    }
    return render(request, 'tai_khoan/danh_gia_bac_si.html', context)
