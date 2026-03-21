# 📋 Cấu Trúc File Theo Từng Đối Tượng

## 🏥 Hệ Thống Quản Lý Phòng Khám

Tài liệu này mô tả các file và chức năng được sử dụng bởi từng đối tượng trong hệ thống.

---

## 👤 1. BỆNH NHÂN (Patient)

### 📁 Backend Files

#### `accounts/models.py`
- **Model:** `HoSoBenhNhan`
  - Lưu thông tin cá nhân: ngày sinh, giới tính, số điện thoại, địa chỉ, ảnh đại diện
  - Liên kết với `User` (Django built-in)

#### `accounts/views.py`
- **`dang_ky_benh_nhan()`** - Đăng ký tài khoản bệnh nhân
- **`dang_nhap()`** - Đăng nhập
- **`dang_xuat()`** - Đăng xuất
- **`ho_so()`** - Xem hồ sơ cá nhân
- **`chinh_sua_ho_so()`** - Chỉnh sửa thông tin cá nhân

#### `appointments/views.py`
- **`danh_sach_bac_si()`** - Xem danh sách bác sĩ (chỉ bác sĩ hoạt động)
- **`lich_lam_viec_bac_si()`** - Xem lịch làm việc của bác sĩ
- **`dat_lich_kham()`** - Đặt lịch khám
- **`lich_hen_cua_toi()`** - Xem lịch hẹn của mình
- **`huy_lich_hen()`** - Hủy lịch hẹn

#### `medical_records/views.py`
- **`lich_su_kham_benh()`** - Xem lịch sử khám bệnh
- **`xem_ho_so_benh_an()`** - Xem chi tiết hồ sơ bệnh án

#### `dashboard/views.py`
- **`bang_dieu_khien()`** - Dashboard bệnh nhân
  - Hiển thị: lịch hẹn sắp tới, tổng lịch hẹn, lịch hẹn đã khám

### 🎨 Frontend Files

| File | Chức Năng |
|------|----------|
| `templates/accounts/dang_ky_benh_nhan.html` | Form đăng ký bệnh nhân |
| `templates/accounts/dang_nhap.html` | Form đăng nhập |
| `templates/accounts/ho_so.html` | Xem hồ sơ cá nhân |
| `templates/accounts/chinh_sua_ho_so.html` | Chỉnh sửa hồ sơ |
| `templates/appointments/danh_sach_bac_si.html` | Danh sách bác sĩ |
| `templates/appointments/lich_lam_viec_bac_si.html` | Lịch làm việc bác sĩ |
| `templates/appointments/dat_lich_kham.html` | Form đặt lịch |
| `templates/appointments/lich_hen_cua_toi.html` | Lịch hẹn của bệnh nhân |
| `templates/medical_records/lich_su_kham_benh.html` | Lịch sử khám bệnh |
| `templates/medical_records/xem_ho_so_benh_an.html` | Chi tiết hồ sơ bệnh án |
| `templates/dashboard/bang_dieu_khien.html` | Dashboard bệnh nhân (hiển thị lịch hẹn sắp tới) |

### 🔐 Quyền Hạn
- ✅ Đăng ký, đăng nhập, đăng xuất
- ✅ Xem/chỉnh sửa hồ sơ cá nhân
- ✅ Xem danh sách bác sĩ hoạt động
- ✅ Đặt lịch khám
- ✅ Hủy lịch hẹn
- ✅ Xem lịch sử khám bệnh
- ❌ Không thể quản lý bác sĩ
- ❌ Không thể tạo hồ sơ bệnh án

---

## 👨‍⚕️ 2. BÁC SĨ (Doctor)

### 📁 Backend Files

#### `accounts/models.py`
- **Model:** `HoSoBacSi`
  - Lưu thông tin: chuyên khoa, bằng cấp, số điện thoại, phí khám, mô tả, ảnh đại diện
  - Liên kết với `User` (Django built-in)

#### `accounts/views.py`
- **`dang_nhap()`** - Đăng nhập
- **`dang_xuat()`** - Đăng xuất
- **`ho_so()`** - Xem hồ sơ cá nhân
- **`chinh_sua_ho_so()`** - Chỉnh sửa thông tin cá nhân

#### `appointments/views.py`
- **`lich_hen_cua_toi()`** - Xem lịch hẹn của bác sĩ
- **`xac_nhan_lich_hen()`** - Xác nhận lịch hẹn

#### `medical_records/views.py`
- **`tao_ho_so_benh_an()`** - Tạo hồ sơ bệnh án sau khi khám
- **`lich_su_kham_benh()`** - Xem lịch sử khám bệnh
- **`xem_ho_so_benh_an()`** - Xem chi tiết hồ sơ bệnh án

#### `dashboard/views.py`
- **`bang_dieu_khien()`** - Dashboard bác sĩ
  - Hiển thị: lịch hẹn hôm nay, lịch hẹn chờ xác nhận, tổng bệnh nhân, lịch hẹn tháng này

### 🎨 Frontend Files

| File | Chức Năng |
|------|----------|
| `templates/accounts/dang_nhap.html` | Form đăng nhập |
| `templates/accounts/ho_so.html` | Xem hồ sơ cá nhân |
| `templates/accounts/chinh_sua_ho_so.html` | Chỉnh sửa hồ sơ |
| `templates/appointments/lich_hen_cua_toi.html` | Lịch hẹn của bác sĩ |
| `templates/medical_records/tao_ho_so_benh_an.html` | Form tạo hồ sơ bệnh án |
| `templates/medical_records/lich_su_kham_benh.html` | Lịch sử khám bệnh |
| `templates/medical_records/xem_ho_so_benh_an.html` | Chi tiết hồ sơ bệnh án |
| `templates/dashboard/bang_dieu_khien.html` | Dashboard bác sĩ |

### 🔐 Quyền Hạn
- ✅ Đăng nhập, đăng xuất
- ✅ Xem/chỉnh sửa hồ sơ cá nhân
- ✅ Xem lịch hẹn của mình
- ✅ Xác nhận lịch hẹn
- ✅ Tạo hồ sơ bệnh án
- ✅ Xem lịch sử khám bệnh
- ❌ Không thể quản lý bác sĩ khác
- ❌ Không thể xem hồ sơ bệnh nhân khác

---

## 👨‍💼 3. ADMIN (Administrator)

### 📁 Backend Files

#### `accounts/models.py`
- **Model:** `ChuyenKhoa`
  - Lưu danh sách chuyên khoa

#### `accounts/views.py`
- **`quan_ly_bac_si()`** - Quản lý bác sĩ
  - Thêm bác sĩ mới
  - Thêm bác sĩ từ tài khoản có sẵn
  - Xóa bác sĩ
  - Tạm ngưng/kích hoạt bác sĩ

#### `dashboard/views.py`
- **`bang_dieu_khien()`** - Dashboard admin
  - Hiển thị: tổng bệnh nhân, tổng bác sĩ, lịch hẹn hôm nay, lịch hẹn tháng này
  - Top 5 bác sĩ có nhiều lịch hẹn nhất
  - Thống kê lịch hẹn theo trạng thái

### 🎨 Frontend Files

| File | Chức Năng |
|------|----------|
| `templates/accounts/quan_ly_bac_si.html` | Quản lý bác sĩ (thêm, xóa, tạm ngưng, kích hoạt) |
| `templates/dashboard/bang_dieu_khien.html` | Dashboard admin |

### 🔐 Quyền Hạn
- ✅ Quản lý bác sĩ (thêm, xóa, tạm ngưng, kích hoạt)
- ✅ Xem thống kê toàn hệ thống
- ✅ Xem danh sách bệnh nhân
- ✅ Xem danh sách bác sĩ
- ✅ Xem tất cả lịch hẹn
- ❌ Không thể xem chi tiết hồ sơ bệnh nhân (ngoài admin)

---

## 📊 4. MODELS (Dữ Liệu)

### `accounts/models.py`
```
ChuyenKhoa
├── ten (CharField)
└── mo_ta (TextField)

HoSoBenhNhan
├── nguoi_dung (OneToOneField → User)
├── ngay_sinh (DateField)
├── gioi_tinh (CharField)
├── so_dien_thoai (CharField)
├── dia_chi (TextField)
└── anh_dai_dien (ImageField)

HoSoBacSi
├── nguoi_dung (OneToOneField → User)
├── chuyen_khoa (ForeignKey → ChuyenKhoa)
├── mo_ta (TextField)
├── bang_cap (CharField)
├── so_dien_thoai (CharField)
├── phi_kham (DecimalField)
└── anh_dai_dien (ImageField)
```

### `appointments/models.py`
```
LichHen
├── benh_nhan (ForeignKey → HoSoBenhNhan)
├── bac_si (ForeignKey → HoSoBacSi)
├── lich_lam_viec (ForeignKey → LichLamViec)
├── ngay (DateField)
├── gio (TimeField)
├── trieu_chung (TextField)
└── trang_thai (CharField: pending, approved, completed, canceled)

LichLamViec
├── bac_si (ForeignKey → HoSoBacSi)
├── ngay (DateField)
├── gio_bat_dau (TimeField)
├── gio_ket_thuc (TimeField)
└── con_trong (BooleanField)
```

### `medical_records/models.py`
```
HoSoBenhAn
├── lich_hen (OneToOneField → LichHen)
├── chan_doan (TextField)
├── toa_thuoc (TextField)
├── ghi_chu (TextField)
└── ngay_tao (DateTimeField)
```

---

## 🔄 5. LUỒNG CÔNG VIỆC

### 📝 Luồng Đặt Lịch Khám (Bệnh Nhân)
```
1. Bệnh nhân đăng ký tài khoản
   ↓
2. Bệnh nhân đăng nhập
   ↓
3. Xem danh sách bác sĩ hoạt động
   ↓
4. Xem lịch làm việc của bác sĩ
   ↓
5. Đặt lịch khám
   ↓
6. Chờ bác sĩ xác nhận
   ↓
7. Bác sĩ xác nhận lịch
   ↓
8. Bác sĩ tạo hồ sơ bệnh án
   ↓
9. Bệnh nhân xem lịch sử khám bệnh
```

### 👨‍⚕️ Luồng Quản Lý Bác Sĩ (Admin)
```
1. Admin truy cập trang quản lý bác sĩ
   ↓
2. Thêm bác sĩ mới hoặc từ tài khoản có sẵn
   ↓
3. Xem danh sách bác sĩ
   ↓
4. Tạm ngưng/kích hoạt bác sĩ
   ↓
5. Xóa bác sĩ (nếu cần)
```

---

## 🔒 6. KIỂM SOÁT TRUY CẬP

### Bệnh Nhân
- Chỉ xem được bác sĩ **hoạt động** (`is_active=True`)
- Chỉ xem được lịch hẹn của mình
- Chỉ xem được hồ sơ bệnh án của mình

### Bác Sĩ
- Chỉ xem được lịch hẹn của mình
- Chỉ tạo hồ sơ bệnh án cho lịch hẹn của mình
- Chỉ xem được hồ sơ bệnh nhân liên quan đến lịch hẹn của mình

### Admin
- Quản lý toàn bộ bác sĩ
- Xem thống kê toàn hệ thống
- Xem tất cả lịch hẹn

---

## 📱 7. TEMPLATES CHÍNH

### Base Template
- `templates/base.html` - Template chính (navbar, messages, container)

### Accounts
- `templates/accounts/dang_ky_benh_nhan.html` - Đăng ký bệnh nhân
- `templates/accounts/dang_nhap.html` - Đăng nhập
- `templates/accounts/ho_so.html` - Xem hồ sơ
- `templates/accounts/chinh_sua_ho_so.html` - Chỉnh sửa hồ sơ
- `templates/accounts/quan_ly_bac_si.html` - Quản lý bác sĩ (Admin)

### Appointments
- `templates/appointments/danh_sach_bac_si.html` - Danh sách bác sĩ
- `templates/appointments/lich_lam_viec_bac_si.html` - Lịch làm việc
- `templates/appointments/dat_lich_kham.html` - Đặt lịch
- `templates/appointments/lich_hen_cua_toi.html` - Lịch hẹn của tôi

### Medical Records
- `templates/medical_records/tao_ho_so_benh_an.html` - Tạo hồ sơ bệnh án
- `templates/medical_records/lich_su_kham_benh.html` - Lịch sử khám bệnh
- `templates/medical_records/xem_ho_so_benh_an.html` - Xem hồ sơ bệnh án

### Dashboard
- `templates/dashboard/bang_dieu_khien.html` - Dashboard (tuỳ theo role)

---

## 🚀 8. CÁCH SỬ DỤNG

### Cho Bệnh Nhân
1. Truy cập `/accounts/dang_ky_benh_nhan/` để đăng ký
2. Đăng nhập tại `/accounts/dang_nhap/`
3. Xem danh sách bác sĩ tại `/appointments/danh_sach_bac_si/`
4. Đặt lịch khám
5. Xem lịch hẹn tại `/appointments/lich_hen_cua_toi/`

### Cho Bác Sĩ
1. Đăng nhập tại `/accounts/dang_nhap/`
2. Xem lịch hẹn tại `/appointments/lich_hen_cua_toi/`
3. Xác nhận lịch hẹn
4. Tạo hồ sơ bệnh án

### Cho Admin
1. Đăng nhập tại `/accounts/dang_nhap/`
2. Truy cập `/accounts/quan_ly_bac_si/` để quản lý bác sĩ
3. Xem dashboard tại `/dashboard/bang_dieu_khien/`

---

## 📝 Ghi Chú
- Bác sĩ bị tạm ngưng (`is_active=False`) sẽ bị ẩn khỏi danh sách đặt lịch
- Bệnh nhân chỉ có thể xem bác sĩ hoạt động
- Admin có quyền quản lý toàn bộ hệ thống
