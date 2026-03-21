# 🔐 Hệ Thống Quyền Hạn (Permissions)

## 📋 Tổng Quan

Hệ thống quản lý phòng khám sử dụng 3 cấp độ quyền hạn dựa trên Django User model:

| Cấp Độ | Mô Tả | Điều Kiện |
|--------|-------|----------|
| **Admin** | Quản lý toàn bộ hệ thống | `is_staff=True` + không có `ho_so_benh_nhan` + không có `ho_so_bac_si` |
| **Bác Sĩ** | Quản lý lịch hẹn và bệnh án | `is_staff=True` + có `ho_so_bac_si` |
| **Bệnh Nhân** | Đặt lịch và xem hồ sơ | `is_staff=False` + có `ho_so_benh_nhan` |

---

## 🔑 Các Trường Quyền Hạn

### 1. `is_staff` (Boolean)
- **Mục đích:** Xác định người dùng có phải là nhân viên/admin không
- **Giá trị:**
  - `True` → Bác sĩ hoặc Admin
  - `False` → Bệnh nhân

### 2. `is_active` (Boolean)
- **Mục đích:** Xác định tài khoản có hoạt động không
- **Giá trị:**
  - `True` → Tài khoản hoạt động (có thể đăng nhập)
  - `False` → Tài khoản bị tạm ngưng (không thể đăng nhập)
- **Ứng dụng:** Tạm ngưng bác sĩ mà không xóa dữ liệu

### 3. `ho_so_benh_nhan` (OneToOneField)
- **Mục đích:** Xác định người dùng là bệnh nhân
- **Kiểm tra:** `hasattr(user, 'ho_so_benh_nhan')`

### 4. `ho_so_bac_si` (OneToOneField)
- **Mục đích:** Xác định người dùng là bác sĩ
- **Kiểm tra:** `hasattr(user, 'ho_so_bac_si')`

---

## 🛡️ Kiểm Soát Truy Cập (Access Control)

### Backend (Views)

#### 1. Quản Lý Bác Sĩ - `quan_ly_bac_si()`
```python
@login_required
def quan_ly_bac_si(request):
    # Chỉ admin (is_staff=True) mới có quyền truy cập
    if not request.user.is_staff or hasattr(request.user, 'ho_so_benh_nhan') or hasattr(request.user, 'ho_so_bac_si'):
        messages.error(request, 'Bạn không có quyền truy cập trang này')
        return redirect('bang_dieu_khien')
```
**Quyền:** ✅ Admin | ❌ Bác sĩ | ❌ Bệnh nhân

#### 2. Danh Sách Bác Sĩ - `danh_sach_bac_si()`
```python
@login_required
def danh_sach_bac_si(request):
    # Chỉ hiển thị bác sĩ hoạt động (is_active=True)
    bac_si_list = HoSoBacSi.objects.filter(nguoi_dung__is_active=True)
```
**Quyền:** ✅ Bệnh nhân | ✅ Bác sĩ | ✅ Admin
**Lưu ý:** Bác sĩ bị tạm ngưng (`is_active=False`) sẽ bị ẩn

#### 3. Lịch Làm Việc Bác Sĩ - `lich_lam_viec_bac_si()`
```python
@login_required
def lich_lam_viec_bac_si(request, bac_si_id):
    # Chỉ xem lịch của bác sĩ hoạt động
    bac_si = get_object_or_404(HoSoBacSi, id=bac_si_id, nguoi_dung__is_active=True)
```
**Quyền:** ✅ Bệnh nhân | ✅ Bác sĩ | ✅ Admin
**Lưu ý:** Không thể xem lịch của bác sĩ bị tạm ngưng

#### 4. Đặt Lịch Khám - `dat_lich_kham()`
```python
@login_required
def dat_lich_kham(request, lich_lam_viec_id):
    if not hasattr(request.user, 'ho_so_benh_nhan'):
        messages.error(request, 'Chỉ bệnh nhân mới có thể đặt lịch')
        return redirect('danh_sach_bac_si')
```
**Quyền:** ✅ Bệnh nhân | ❌ Bác sĩ | ❌ Admin

#### 5. Xác Nhận Lịch Hẹn - `xac_nhan_lich_hen()`
```python
@login_required
def xac_nhan_lich_hen(request, lich_hen_id):
    if not hasattr(request.user, 'ho_so_bac_si') or lich_hen.bac_si != request.user.ho_so_bac_si:
        messages.error(request, 'Bạn không có quyền xác nhận lịch này')
        return redirect('lich_hen_cua_toi')
```
**Quyền:** ❌ Bệnh nhân | ✅ Bác sĩ (chỉ lịch của mình) | ❌ Admin

#### 6. Tạo Hồ Sơ Bệnh Án - `tao_ho_so_benh_an()`
```python
@login_required
def tao_ho_so_benh_an(request, lich_hen_id):
    if not hasattr(request.user, 'ho_so_bac_si') or lich_hen.bac_si != request.user.ho_so_bac_si:
        messages.error(request, 'Bạn không có quyền tạo hồ sơ này')
        return redirect('lich_hen_cua_toi')
```
**Quyền:** ❌ Bệnh nhân | ✅ Bác sĩ (chỉ lịch của mình) | ❌ Admin

#### 7. Xem Hồ Sơ Bệnh Án - `xem_ho_so_benh_an()`
```python
@login_required
def xem_ho_so_benh_an(request, ho_so_id):
    if hasattr(request.user, 'ho_so_benh_nhan'):
        if ho_so.lich_hen.benh_nhan != request.user.ho_so_benh_nhan:
            messages.error(request, 'Bạn không có quyền xem hồ sơ này')
            return redirect('lich_su_kham_benh')
    elif hasattr(request.user, 'ho_so_bac_si'):
        if ho_so.lich_hen.bac_si != request.user.ho_so_bac_si:
            messages.error(request, 'Bạn không có quyền xem hồ sơ này')
            return redirect('lich_su_kham_benh')
```
**Quyền:** ✅ Bệnh nhân (chỉ hồ sơ của mình) | ✅ Bác sĩ (chỉ hồ sơ bệnh nhân của mình) | ✅ Admin

### Frontend (Templates)

#### `templates/base.html` - Navbar
```html
{% if user.is_authenticated %}
    <a href="{% url 'bang_dieu_khien' %}">Dashboard</a>
    {% if not user.ho_so_benh_nhan and not user.ho_so_bac_si %}
        <!-- Admin menu -->
        <a href="{% url 'danh_sach_bac_si' %}">Bác sĩ</a>
        <a href="{% url 'lich_hen_cua_toi' %}">Lịch hẹn</a>
        <a href="{% url 'lich_su_kham_benh' %}">Hồ sơ</a>
        <a href="{% url 'quan_ly_bac_si' %}">Quản lý bác sĩ</a>
    {% else %}
        <!-- Bệnh nhân/Bác sĩ menu -->
        <a href="{% url 'danh_sach_bac_si' %}">Bác sĩ</a>
        <a href="{% url 'lich_hen_cua_toi' %}">Lịch hẹn</a>
        <a href="{% url 'lich_su_kham_benh' %}">Hồ sơ</a>
    {% endif %}
{% endif %}
```

---

## 📊 Bảng Quyền Hạn Chi Tiết

| Chức Năng | Admin | Bác Sĩ | Bệnh Nhân |
|-----------|-------|--------|----------|
| **Quản lý bác sĩ** | ✅ | ❌ | ❌ |
| Xem danh sách bác sĩ | ✅ | ✅ | ✅ |
| Xem lịch làm việc bác sĩ | ✅ | ✅ | ✅ |
| Đặt lịch khám | ❌ | ❌ | ✅ |
| Xem lịch hẹn của mình | ✅ | ✅ | ✅ |
| Xác nhận lịch hẹn | ❌ | ✅ (của mình) | ❌ |
| Tạo hồ sơ bệnh án | ❌ | ✅ (của mình) | ❌ |
| Xem hồ sơ bệnh án | ✅ | ✅ (của mình) | ✅ (của mình) |
| Xem dashboard | ✅ | ✅ | ✅ |
| Chỉnh sửa hồ sơ cá nhân | ✅ | ✅ | ✅ |

---

## 🔄 Luồng Tạo Tài Khoản & Quyền

### 1. Bệnh Nhân Đăng Ký
```
User.objects.create_user(
    username=...,
    password=...,
    is_staff=False  ← Không phải staff
)
HoSoBenhNhan.objects.create(
    nguoi_dung=user,
    ...
)
```
**Kết quả:** `is_staff=False`, `ho_so_benh_nhan` tồn tại

### 2. Admin Thêm Bác Sĩ Mới
```
User.objects.create_user(
    username=...,
    password=...,
    is_staff=True  ← Là staff
)
HoSoBacSi.objects.create(
    nguoi_dung=user,
    ...
)
```
**Kết quả:** `is_staff=True`, `ho_so_bac_si` tồn tại

### 3. Admin Thêm Bác Sĩ Từ Tài Khoản Có Sẵn
```
user.is_staff = True  ← Nâng cấp thành staff
user.save()
HoSoBacSi.objects.create(
    nguoi_dung=user,
    ...
)
```
**Kết quả:** `is_staff=True`, `ho_so_bac_si` tồn tại

### 4. Admin Tạm Ngưng Bác Sĩ
```
user.is_active = False  ← Tạm ngưng
user.save()
```
**Kết quả:** Bác sĩ không thể đăng nhập, bị ẩn khỏi danh sách

### 5. Admin Kích Hoạt Bác Sĩ
```
user.is_active = True  ← Kích hoạt
user.save()
```
**Kết quả:** Bác sĩ có thể đăng nhập lại, hiển thị trong danh sách

---

## 🚨 Các Lỗi Quyền Hạn Thường Gặp

| Lỗi | Nguyên Nhân | Giải Pháp |
|-----|-----------|----------|
| Bệnh nhân thấy link "Quản lý bác sĩ" | Navbar không kiểm tra quyền | Kiểm tra `not user.ho_so_benh_nhan and not user.ho_so_bac_si` |
| Bệnh nhân có thể truy cập trang quản lý | View không kiểm tra quyền | Thêm kiểm tra `is_staff` và `hasattr()` |
| Bác sĩ bị tạm ngưng vẫn hiển thị | Query không lọc `is_active` | Thêm `.filter(nguoi_dung__is_active=True)` |
| Bệnh nhân xem được hồ sơ của người khác | Không kiểm tra quyền sở hữu | Kiểm tra `ho_so.lich_hen.benh_nhan == user.ho_so_benh_nhan` |

---

## 📝 Ghi Chú Bảo Mật

1. **Luôn kiểm tra quyền ở Backend** - Frontend chỉ là UI, backend phải kiểm tra
2. **Sử dụng `@login_required`** - Đảm bảo người dùng đã đăng nhập
3. **Kiểm tra quyền sở hữu** - Bệnh nhân chỉ xem được dữ liệu của mình
4. **Ẩn UI không cần thiết** - Không hiển thị link/button mà người dùng không có quyền
5. **Ghi log hành động** - Theo dõi các hành động nhạy cảm

---

## 🔗 Tham Khảo

- Django User Model: https://docs.djangoproject.com/en/stable/ref/contrib/auth/
- Django Permissions: https://docs.djangoproject.com/en/stable/topics/auth/
- `@login_required` decorator: https://docs.djangoproject.com/en/stable/topics/auth/default/#the-login-required-decorator
