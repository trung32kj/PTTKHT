# PHÂN TÍCH BÀI TOÁN VÀ THIẾT KẾ KẾ HOẠCH WEB

## Hệ thống Quản lý và Đặt lịch Khám trực tuyến cho Chuỗi Phòng khám Đa khoa

---

## 📋 MỤC LỤC

1. [Tổng quan bài toán](#1-tổng-quan-bài-toán)
2. [Phân tích yêu cầu](#2-phân-tích-yêu-cầu)
3. [Thiết kế kiến trúc hệ thống](#3-thiết-kế-kiến-trúc-hệ-thống)
4. [Thiết kế cơ sở dữ liệu](#4-thiết-kế-cơ-sở-dữ-liệu)
5. [Thiết kế giao diện](#5-thiết-kế-giao-diện)
6. [Kế hoạch triển khai](#6-kế-hoạch-triển-khai)
7. [Đánh giá và kiến nghị](#7-đánh-giá-và-kiến-nghị)

---

## 1. TỔNG QUAN BÀI TOÁN

### 1.1. Bối cảnh

Trong bối cảnh chuyển đổi số mạnh mẽ của ngành y tế Việt Nam, các phòng khám đa khoa đang đối mặt với nhiều thách thức:

- **70%** phòng khám vẫn sử dụng phương pháp quản lý thủ công
- Bệnh nhân phải đến trực tiếp để đặt lịch, tốn thời gian
- Khó khăn trong quản lý hồ sơ bệnh án giấy tờ
- Thiếu công cụ thống kê và báo cáo hiệu quả

### 1.2. Mục tiêu dự án

**Mục tiêu chính:** Xây dựng hệ thống web quản lý phòng khám toàn diện, hỗ trợ đặt lịch khám trực tuyến

**Mục tiêu cụ thể:**
- Số hóa quy trình đặt lịch khám bệnh
- Quản lý hồ sơ bệnh án điện tử
- Tối ưu hóa lịch làm việc của bác sĩ
- Cung cấp dashboard thống kê cho quản lý
- Nâng cao trải nghiệm bệnh nhân

### 1.3. Phạm vi dự án

**Đối tượng sử dụng:**
- Bệnh nhân (Patient)
- Bác sĩ (Doctor)
- Quản trị viên (Admin)

**Chức năng cốt lõi:**
- Quản lý người dùng và phân quyền
- Hệ thống đặt lịch khám trực tuyến
- Quản lý hồ sơ bệnh án điện tử
- Dashboard và báo cáo thống kê


---

## 2. PHÂN TÍCH YÊU CẦU

### 2.1. Phân tích Stakeholders

#### 2.1.1. Bệnh nhân (Patient)

**Đặc điểm:**
- Độ tuổi: 18-70 tuổi
- Trình độ công nghệ: Cơ bản đến trung bình
- Thiết bị: Smartphone, máy tính

**Nhu cầu:**
- Đặt lịch khám nhanh chóng, tiện lợi 24/7
- Xem thông tin bác sĩ chi tiết (chuyên khoa, kinh nghiệm, đánh giá)
- Theo dõi lịch sử khám bệnh cá nhân
- Nhận thông báo nhắc nhở lịch hẹn
- Giao diện đơn giản, dễ sử dụng

**Pain points hiện tại:**
- Phải đến trực tiếp để đặt lịch
- Thời gian chờ đợi lâu
- Khó tra cứu lịch sử khám bệnh
- Dễ quên lịch hẹn

#### 2.1.2. Bác sĩ (Doctor)

**Đặc điểm:**
- Chuyên gia y tế, bận rộn
- Cần công cụ hiệu quả, tiết kiệm thời gian
- Quan tâm đến chất lượng chăm sóc bệnh nhân

**Nhu cầu:**
- Quản lý lịch hẹn tập trung
- Xem thông tin bệnh nhân trước khi khám
- Ghi chép hồ sơ bệnh án nhanh chóng
- Theo dõi thống kê bệnh nhân
- Truy cập lịch sử khám bệnh của bệnh nhân

**Pain points hiện tại:**
- Lịch hẹn không được tổ chức tốt
- Ghi chép thủ công tốn thời gian
- Khó tra cứu hồ sơ bệnh nhân cũ
- Không có thống kê tự động

#### 2.1.3. Quản trị viên (Admin)

**Đặc điểm:**
- Quản lý phòng khám hoặc nhân viên IT
- Cần kiểm soát toàn bộ hệ thống
- Quan tâm đến hiệu quả hoạt động

**Nhu cầu:**
- Quản lý danh sách bác sĩ (thêm, xóa, tạm ngưng)
- Xem báo cáo thống kê tổng thể
- Kiểm soát quyền truy cập
- Giám sát hoạt động hệ thống
- Quản lý chuyên khoa

**Pain points hiện tại:**
- Khó quản lý nhiều bác sĩ
- Thiếu công cụ thống kê
- Không kiểm soát được quyền truy cập
- Khó đánh giá hiệu quả hoạt động

### 2.2. Yêu cầu chức năng chi tiết

#### 2.2.1. Module Quản lý Người dùng

**FR-01: Đăng ký bệnh nhân**
- **Mô tả:** Bệnh nhân tự đăng ký tài khoản mới
- **Input:** Họ tên, email, username, password, ngày sinh, giới tính, SĐT, địa chỉ
- **Process:** 
  - Validate dữ liệu đầu vào
  - Kiểm tra username/email trùng lặp
  - Hash password
  - Tạo User và HoSoBenhNhan
- **Output:** Tài khoản bệnh nhân mới, chuyển đến trang đăng nhập
- **Business Rules:**
  - Username phải unique
  - Email phải đúng format
  - Password tối thiểu 8 ký tự
  - Ngày sinh phải < ngày hiện tại

**FR-02: Đăng nhập**
- **Mô tả:** Xác thực người dùng vào hệ thống
- **Input:** Username/Email, Password
- **Process:**
  - Xác thực credentials
  - Tạo session
  - Phân quyền theo role
- **Output:** Chuyển đến dashboard tương ứng với role
- **Business Rules:**
  - Tài khoản phải active (is_active=True)
  - Khóa tài khoản sau 5 lần đăng nhập sai (optional)

**FR-03: Quản lý hồ sơ cá nhân**
- **Mô tả:** Xem và chỉnh sửa thông tin cá nhân
- **Input:** Thông tin cập nhật (SĐT, địa chỉ, ảnh đại diện)
- **Process:** Validate và cập nhật database
- **Output:** Thông báo cập nhật thành công
- **Business Rules:**
  - Không được thay đổi username
  - Email phải unique nếu thay đổi

**FR-04: Quản lý bác sĩ (Admin only)**
- **Mô tả:** Admin quản lý danh sách bác sĩ
- **Chức năng:**
  - Thêm bác sĩ mới (tạo User + HoSoBacSi)
  - Thêm bác sĩ từ User có sẵn
  - Tạm ngưng bác sĩ (is_active=False)
  - Kích hoạt lại bác sĩ
  - Xóa bác sĩ (soft delete)
- **Business Rules:**
  - Bác sĩ bị tạm ngưng không hiển thị trong danh sách đặt lịch
  - Không xóa bác sĩ có lịch hẹn đang active

#### 2.2.2. Module Đặt lịch Khám

**FR-05: Xem danh sách bác sĩ**
- **Mô tả:** Hiển thị danh sách bác sĩ hoạt động
- **Filter:** Theo chuyên khoa
- **Display:** Ảnh, tên, chuyên khoa, bằng cấp, phí khám, đánh giá
- **Business Rules:**
  - Chỉ hiển thị bác sĩ is_active=True
  - Sắp xếp theo đánh giá hoặc tên

**FR-06: Xem lịch làm việc bác sĩ**
- **Mô tả:** Hiển thị lịch trống của bác sĩ
- **Display:** Calendar view với các khung giờ
- **Business Rules:**
  - Chỉ hiển thị lịch trong tương lai
  - Highlight khung giờ còn trống (con_trong=True)
  - Ẩn khung giờ đã đặt

**FR-07: Đặt lịch khám**
- **Mô tả:** Bệnh nhân đặt lịch hẹn với bác sĩ
- **Input:** Chọn khung giờ, nhập triệu chứng
- **Process:**
  - Kiểm tra lịch còn trống
  - Tạo LichHen với trạng thái 'pending'
  - Cập nhật LichLamViec.con_trong = False
- **Output:** Thông báo đặt lịch thành công
- **Business Rules:**
  - Bệnh nhân chỉ đặt được lịch trong tương lai
  - Không đặt trùng giờ với lịch hẹn khác của mình
  - Mỗi khung giờ chỉ 1 bệnh nhân

**FR-08: Xác nhận lịch hẹn (Bác sĩ)**
- **Mô tả:** Bác sĩ xác nhận hoặc hủy lịch hẹn
- **Process:**
  - Xem danh sách lịch hẹn pending
  - Xác nhận: Cập nhật trạng thái 'approved'
  - Hủy: Cập nhật trạng thái 'canceled', LichLamViec.con_trong = True
- **Output:** Thông báo cho bệnh nhân
- **Business Rules:**
  - Chỉ xác nhận lịch hẹn của mình
  - Có thể hủy lịch đã xác nhận (trước 24h)

**FR-09: Hủy lịch hẹn**
- **Mô tả:** Bệnh nhân hoặc bác sĩ hủy lịch
- **Process:**
  - Cập nhật trạng thái 'canceled'
  - Cập nhật LichLamViec.con_trong = True
- **Business Rules:**
  - Bệnh nhân chỉ hủy lịch pending hoặc approved
  - Không hủy lịch đã completed
  - Hủy trước 2 giờ (optional)

#### 2.2.3. Module Hồ sơ Bệnh án

**FR-10: Tạo hồ sơ bệnh án**
- **Mô tả:** Bác sĩ ghi chép sau khi khám
- **Input:** Chẩn đoán, toa thuốc, ghi chú
- **Process:**
  - Tạo HoSoBenhAn liên kết với LichHen
  - Tạo ToaThuoc (nếu có)
  - Cập nhật LichHen.trang_thai = 'completed'
- **Output:** Hồ sơ bệnh án mới
- **Business Rules:**
  - Chỉ tạo cho lịch hẹn approved
  - Mỗi lịch hẹn chỉ có 1 hồ sơ bệnh án
  - Chỉ bác sĩ của lịch hẹn mới tạo được

**FR-11: Xem hồ sơ bệnh án**
- **Mô tả:** Xem chi tiết hồ sơ bệnh án
- **Display:** Chẩn đoán, toa thuốc, ghi chú, ngày khám
- **Business Rules:**
  - Bệnh nhân chỉ xem hồ sơ của mình
  - Bác sĩ xem hồ sơ bệnh nhân đã khám

**FR-12: Lịch sử khám bệnh**
- **Mô tả:** Danh sách hồ sơ bệnh án
- **Display:** Ngày khám, bác sĩ, chẩn đoán
- **Filter:** Theo ngày, bác sĩ
- **Business Rules:**
  - Sắp xếp theo ngày mới nhất

#### 2.2.4. Module Dashboard & Báo cáo

**FR-13: Dashboard bệnh nhân**
- **Display:**
  - Lịch hẹn sắp tới (3 ngày)
  - Tổng số lịch hẹn
  - Số lịch đã khám
  - Quick action: Đặt lịch mới

**FR-14: Dashboard bác sĩ**
- **Display:**
  - Lịch hẹn hôm nay
  - Lịch hẹn chờ xác nhận
  - Tổng bệnh nhân đã khám
  - Lịch hẹn tháng này
  - Biểu đồ thống kê

**FR-15: Dashboard admin**
- **Display:**
  - Tổng bệnh nhân
  - Tổng bác sĩ
  - Lịch hẹn hôm nay
  - Lịch hẹn tháng này
  - Top 5 bác sĩ nhiều lịch hẹn
  - Thống kê theo trạng thái
  - Biểu đồ doanh thu (optional)

### 2.3. Yêu cầu phi chức năng

#### 2.3.1. Hiệu năng (Performance)

| Chỉ số | Yêu cầu | Đo lường |
|--------|---------|----------|
| Thời gian phản hồi | < 3 giây | Page load time |
| Concurrent users | 100 users | Stress testing |
| Database query | < 100ms | Query optimization |
| API response | < 500ms | API testing |

#### 2.3.2. Khả năng sử dụng (Usability)

- **Giao diện:** Đơn giản, trực quan, thân thiện
- **Responsive:** Tương thích mobile, tablet, desktop
- **Ngôn ngữ:** Tiếng Việt 100%
- **Accessibility:** Tuân thủ WCAG 2.1 Level AA
- **Learning curve:** < 30 phút cho người dùng mới

#### 2.3.3. Bảo mật (Security)

- **Authentication:** Django built-in authentication
- **Authorization:** Role-based access control (RBAC)
- **Password:** Hash với PBKDF2 (Django default)
- **CSRF Protection:** Django middleware
- **SQL Injection:** Django ORM parameterized queries
- **XSS Protection:** Django template auto-escape
- **HTTPS:** SSL/TLS encryption (production)
- **Session:** Secure cookie, timeout 30 phút

#### 2.3.4. Độ tin cậy (Reliability)

- **Uptime:** 99% availability
- **Data backup:** Daily backup
- **Error handling:** Graceful degradation
- **Data integrity:** ACID transactions
- **Logging:** Comprehensive audit trail

#### 2.3.5. Khả năng mở rộng (Scalability)

- **Horizontal scaling:** Load balancer support
- **Database:** Migration path to PostgreSQL
- **Caching:** Redis integration ready
- **CDN:** Static files delivery
- **Microservices:** Modular architecture


---

## 3. THIẾT KẾ KIẾN TRÚC HỆ THỐNG

### 3.1. Kiến trúc tổng thể (System Architecture)

```
┌─────────────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Browser    │  │    Mobile    │  │    Tablet    │          │
│  │  (Desktop)   │  │   (Phone)    │  │              │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                            │ HTTPS
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PRESENTATION LAYER                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Django Templates (MTV)                     │   │
│  │  • HTML5 + CSS3 + JavaScript                           │   │
│  │  • Bootstrap 5 Framework                               │   │
│  │  • Responsive Design                                   │   │
│  │  • AJAX for dynamic content                            │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Django Web Framework 5.2.8                 │   │
│  │                                                         │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐ │   │
│  │  │  Views   │  │Templates │  │  Forms   │  │  URLs  │ │   │
│  │  │ (Logic)  │  │ (UI)     │  │(Validate)│  │(Routes)│ │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └────────┘ │   │
│  │                                                         │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │              Middleware Stack                   │   │   │
│  │  │  • Authentication & Authorization              │   │   │
│  │  │  • CSRF Protection                             │   │   │
│  │  │  • Session Management                          │   │   │
│  │  │  • Security Headers                            │   │   │
│  │  │  • Logging & Audit                             │   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    BUSINESS LAYER                               │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                  Django Models (ORM)                    │   │
│  │                                                         │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐ │   │
│  │  │   User   │  │ Patient  │  │  Doctor  │  │Specialty│ │   │
│  │  │  Model   │  │  Model   │  │  Model   │  │ Model  │ │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └────────┘ │   │
│  │                                                         │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐ │   │
│  │  │Schedule  │  │Appointment│ │ Medical  │  │Medicine│ │   │
│  │  │  Model   │  │  Model   │  │  Record  │  │ Model  │ │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └────────┘ │   │
│  │                                                         │   │
│  │  ┌─────────────────────────────────────────────────┐   │   │
│  │  │           Business Logic Services               │   │   │
│  │  │  • Appointment Scheduling Logic                │   │   │
│  │  │  • User Management Service                     │   │   │
│  │  │  • Medical Record Service                      │   │   │
│  │  │  • Notification Service                        │   │   │
│  │  │  • Reporting & Analytics                       │   │   │
│  │  └─────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA LAYER                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   Django ORM                            │   │
│  │  • Query Optimization (select_related, prefetch_related)│   │
│  │  • Migration Management                                │   │
│  │  • Connection Pooling                                  │   │
│  │  • Transaction Management                              │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              SQLite Database (Development)              │   │
│  │              PostgreSQL (Production Ready)              │   │
│  │                                                         │   │
│  │  Tables:                                               │   │
│  │  • auth_user                                           │   │
│  │  • accounts_chuyenkhoa                                 │   │
│  │  • accounts_hosobenhnhan                               │   │
│  │  • accounts_hosobacsi                                  │   │
│  │  • accounts_danhgiabacsi                               │   │
│  │  • appointments_lichlamviec                            │   │
│  │  • appointments_lichhen                                │   │
│  │  • medical_records_hosobenhan                          │   │
│  │  • medical_records_thuoc                               │   │
│  │  • medical_records_toathuoc                            │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2. Kiến trúc Django MTV (Model-Template-View)

#### 3.2.1. Model Layer (Tầng dữ liệu)

**Trách nhiệm:**
- Định nghĩa cấu trúc dữ liệu
- Tương tác với database thông qua ORM
- Chứa business logic liên quan đến dữ liệu
- Validation dữ liệu

**Ví dụ:**
```python
# accounts/models.py
class HoSoBenhNhan(models.Model):
    nguoi_dung = models.OneToOneField(User, on_delete=models.CASCADE)
    ngay_sinh = models.DateField()
    gioi_tinh = models.CharField(max_length=1, choices=GIOI_TINH_CHOICES)
    so_dien_thoai = models.CharField(max_length=15)
    
    def tuoi(self):
        """Business logic: Tính tuổi"""
        return timezone.now().year - self.ngay_sinh.year
    
    def __str__(self):
        return f"{self.nguoi_dung.get_full_name()}"
```

#### 3.2.2. View Layer (Tầng xử lý logic)

**Trách nhiệm:**
- Nhận request từ client
- Xử lý business logic
- Tương tác với Model
- Render Template hoặc trả về JSON
- Xử lý authentication & authorization

**Ví dụ:**
```python
# appointments/views.py
@login_required
def dat_lich_kham(request, lich_lam_viec_id):
    # Authorization check
    if not hasattr(request.user, 'ho_so_benh_nhan'):
        messages.error(request, 'Chỉ bệnh nhân mới có thể đặt lịch')
        return redirect('dang_nhap')
    
    # Get data
    lich_lam_viec = get_object_or_404(LichLamViec, id=lich_lam_viec_id)
    
    # Business logic
    if not lich_lam_viec.con_trong:
        messages.error(request, 'Lịch này đã được đặt')
        return redirect('lich_lam_viec_bac_si', bac_si_id=lich_lam_viec.bac_si.id)
    
    if request.method == 'POST':
        form = DatLichForm(request.POST)
        if form.is_valid():
            lich_hen = form.save(commit=False)
            lich_hen.benh_nhan = request.user.ho_so_benh_nhan
            lich_hen.bac_si = lich_lam_viec.bac_si
            lich_hen.lich_lam_viec = lich_lam_viec
            lich_hen.ngay = lich_lam_viec.ngay
            lich_hen.gio = lich_lam_viec.gio_bat_dau
            lich_hen.save()
            
            # Update schedule
            lich_lam_viec.con_trong = False
            lich_lam_viec.save()
            
            messages.success(request, 'Đặt lịch thành công!')
            return redirect('lich_hen_cua_toi')
    else:
        form = DatLichForm()
    
    context = {
        'form': form,
        'lich_lam_viec': lich_lam_viec,
        'bac_si': lich_lam_viec.bac_si
    }
    return render(request, 'appointments/dat_lich_kham.html', context)
```

#### 3.2.3. Template Layer (Tầng giao diện)

**Trách nhiệm:**
- Hiển thị dữ liệu cho người dùng
- Sử dụng Django Template Language
- Tách biệt logic và presentation
- Responsive design

**Ví dụ:**
```html
<!-- templates/appointments/dat_lich_kham.html -->
{% extends 'base.html' %}

{% block title %}Đặt lịch khám{% endblock %}

{% block content %}
<div class="container mt-4">
    <h2>Đặt lịch khám với {{ bac_si.nguoi_dung.get_full_name }}</h2>
    
    <div class="card mb-3">
        <div class="card-body">
            <h5>Thông tin bác sĩ</h5>
            <p><strong>Chuyên khoa:</strong> {{ bac_si.chuyen_khoa }}</p>
            <p><strong>Ngày khám:</strong> {{ lich_lam_viec.ngay|date:"d/m/Y" }}</p>
            <p><strong>Giờ khám:</strong> {{ lich_lam_viec.gio_bat_dau }} - {{ lich_lam_viec.gio_ket_thuc }}</p>
            <p><strong>Phí khám:</strong> {{ bac_si.phi_kham|floatformat:0 }}đ</p>
        </div>
    </div>
    
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Xác nhận đặt lịch</button>
        <a href="{% url 'lich_lam_viec_bac_si' bac_si.id %}" class="btn btn-secondary">Hủy</a>
    </form>
</div>
{% endblock %}
```

### 3.3. Phân tích luồng xử lý (Flow Diagram)

#### 3.3.1. Luồng đặt lịch khám

```
BỆNH NHÂN                    HỆ THỐNG                      BÁC SĨ
    │                            │                            │
    │ 1. Đăng nhập               │                            │
    ├──────────────────────────>│                            │
    │                            │ Xác thực                   │
    │                            │ Tạo session                │
    │<──────────────────────────┤                            │
    │ Dashboard                  │                            │
    │                            │                            │
    │ 2. Xem danh sách bác sĩ    │                            │
    ├──────────────────────────>│                            │
    │                            │ Query: HoSoBacSi           │
    │                            │ Filter: is_active=True     │
    │<──────────────────────────┤                            │
    │ Danh sách bác sĩ           │                            │
    │                            │                            │
    │ 3. Chọn bác sĩ             │                            │
    ├──────────────────────────>│                            │
    │                            │ Query: LichLamViec         │
    │                            │ Filter: con_trong=True     │
    │<──────────────────────────┤                            │
    │ Lịch làm việc              │                            │
    │                            │                            │
    │ 4. Chọn khung giờ          │                            │
    │    Nhập triệu chứng        │                            │
    ├──────────────────────────>│                            │
    │                            │ Validate                   │
    │                            │ Create: LichHen            │
    │                            │   status='pending'         │
    │                            │ Update: LichLamViec        │
    │                            │   con_trong=False          │
    │<──────────────────────────┤                            │
    │ Thông báo thành công       │                            │
    │                            │                            │
    │                            │ 5. Thông báo lịch hẹn mới  │
    │                            ├──────────────────────────>│
    │                            │                            │
    │                            │ 6. Bác sĩ xem lịch hẹn     │
    │                            │<──────────────────────────┤
    │                            │ Query: LichHen             │
    │                            │ Filter: bac_si=current     │
    │                            │         status='pending'   │
    │                            ├──────────────────────────>│
    │                            │ Danh sách lịch hẹn         │
    │                            │                            │
    │                            │ 7. Xác nhận lịch hẹn       │
    │                            │<──────────────────────────┤
    │                            │ Update: LichHen            │
    │                            │   status='approved'        │
    │ 8. Thông báo xác nhận      │                            │
    │<──────────────────────────┤                            │
    │                            │                            │
```

#### 3.3.2. Luồng tạo hồ sơ bệnh án

```
BÁC SĨ                       HỆ THỐNG                    BỆNH NHÂN
    │                            │                            │
    │ 1. Xem lịch hẹn hôm nay    │                            │
    ├──────────────────────────>│                            │
    │                            │ Query: LichHen             │
    │                            │ Filter: bac_si=current     │
    │                            │         ngay=today         │
    │                            │         status='approved'  │
    │<──────────────────────────┤                            │
    │ Danh sách lịch hẹn         │                            │
    │                            │                            │
    │ 2. Chọn lịch hẹn           │                            │
    │    Xem thông tin BN        │                            │
    ├──────────────────────────>│                            │
    │                            │ Query: HoSoBenhNhan        │
    │                            │ Query: Previous records    │
    │<──────────────────────────┤                            │
    │ Thông tin bệnh nhân        │                            │
    │ Lịch sử khám bệnh          │                            │
    │                            │                            │
    │ 3. Khám bệnh               │                            │
    │    (Offline)               │                            │
    │                            │                            │
    │ 4. Tạo hồ sơ bệnh án       │                            │
    │    - Chẩn đoán             │                            │
    │    - Toa thuốc             │                            │
    │    - Ghi chú               │                            │
    ├──────────────────────────>│                            │
    │                            │ Validate                   │
    │                            │ Create: HoSoBenhAn         │
    │                            │ Create: ToaThuoc (if any)  │
    │                            │ Update: LichHen            │
    │                            │   status='completed'       │
    │<──────────────────────────┤                            │
    │ Thông báo thành công       │                            │
    │                            │                            │
    │                            │ 5. Thông báo hoàn thành    │
    │                            ├──────────────────────────>│
    │                            │                            │
    │                            │ 6. BN xem hồ sơ            │
    │                            │<──────────────────────────┤
    │                            │ Query: HoSoBenhAn          │
    │                            │ Filter: lich_hen.benh_nhan │
    │                            ├──────────────────────────>│
    │                            │ Hồ sơ bệnh án              │
    │                            │                            │
```

### 3.4. Thiết kế API Endpoints

#### 3.4.1. Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/accounts/dang_nhap/` | Hiển thị form đăng nhập | No |
| POST | `/accounts/dang_nhap/` | Xử lý đăng nhập | No |
| GET | `/accounts/dang_xuat/` | Đăng xuất | Yes |
| GET | `/accounts/dang_ky_benh_nhan/` | Form đăng ký BN | No |
| POST | `/accounts/dang_ky_benh_nhan/` | Xử lý đăng ký BN | No |

#### 3.4.2. User Management Endpoints

| Method | Endpoint | Description | Auth Required | Role |
|--------|----------|-------------|---------------|------|
| GET | `/accounts/ho_so/` | Xem hồ sơ cá nhân | Yes | All |
| GET | `/accounts/chinh_sua_ho_so/` | Form chỉnh sửa | Yes | All |
| POST | `/accounts/chinh_sua_ho_so/` | Cập nhật hồ sơ | Yes | All |
| GET | `/accounts/quan_ly_bac_si/` | Quản lý bác sĩ | Yes | Admin |
| POST | `/accounts/them_bac_si/` | Thêm bác sĩ mới | Yes | Admin |
| POST | `/accounts/tam_ngung_bac_si/<id>/` | Tạm ngưng bác sĩ | Yes | Admin |

#### 3.4.3. Appointment Endpoints

| Method | Endpoint | Description | Auth Required | Role |
|--------|----------|-------------|---------------|------|
| GET | `/appointments/danh_sach_bac_si/` | Danh sách bác sĩ | Yes | Patient |
| GET | `/appointments/lich_lam_viec_bac_si/<id>/` | Lịch làm việc | Yes | Patient |
| GET | `/appointments/dat_lich_kham/<id>/` | Form đặt lịch | Yes | Patient |
| POST | `/appointments/dat_lich_kham/<id>/` | Xử lý đặt lịch | Yes | Patient |
| GET | `/appointments/lich_hen_cua_toi/` | Lịch hẹn của tôi | Yes | All |
| POST | `/appointments/xac_nhan_lich_hen/<id>/` | Xác nhận lịch | Yes | Doctor |
| POST | `/appointments/huy_lich_hen/<id>/` | Hủy lịch hẹn | Yes | Patient/Doctor |

#### 3.4.4. Medical Record Endpoints

| Method | Endpoint | Description | Auth Required | Role |
|--------|----------|-------------|---------------|------|
| GET | `/medical_records/tao_ho_so_benh_an/<id>/` | Form tạo HSBA | Yes | Doctor |
| POST | `/medical_records/tao_ho_so_benh_an/<id>/` | Xử lý tạo HSBA | Yes | Doctor |
| GET | `/medical_records/xem_ho_so_benh_an/<id>/` | Xem chi tiết HSBA | Yes | Patient/Doctor |
| GET | `/medical_records/lich_su_kham_benh/` | Lịch sử khám | Yes | Patient/Doctor |

#### 3.4.5. Dashboard Endpoints

| Method | Endpoint | Description | Auth Required | Role |
|--------|----------|-------------|---------------|------|
| GET | `/dashboard/bang_dieu_khien/` | Dashboard | Yes | All |

### 3.5. Thiết kế bảo mật

#### 3.5.1. Authentication Strategy

**Django Built-in Authentication:**
```python
# settings.py
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Password hashing
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]
```

#### 3.5.2. Authorization Strategy (RBAC)

**Role-based Access Control:**
```python
# Custom decorators
def benh_nhan_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not hasattr(request.user, 'ho_so_benh_nhan'):
            messages.error(request, 'Chỉ bệnh nhân mới có quyền truy cập')
            return redirect('dang_nhap')
        return view_func(request, *args, **kwargs)
    return wrapper

def bac_si_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not hasattr(request.user, 'ho_so_bac_si'):
            messages.error(request, 'Chỉ bác sĩ mới có quyền truy cập')
            return redirect('dang_nhap')
        return view_func(request, *args, **kwargs)
    return wrapper

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, 'Chỉ admin mới có quyền truy cập')
            return redirect('dang_nhap')
        return view_func(request, *args, **kwargs)
    return wrapper

# Usage
@login_required
@benh_nhan_required
def dat_lich_kham(request, lich_lam_viec_id):
    # Only patients can access
    pass
```

#### 3.5.3. Data Protection

**Sensitive Data Handling:**
```python
# Encrypt sensitive fields (optional)
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

class HoSoBenhNhan(models.Model):
    so_dien_thoai = EncryptedCharField(max_length=15)
    dia_chi = models.TextField()  # Consider encryption
    
# Audit logging
class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    
    def __str__(self):
        return f"{self.user} - {self.action} - {self.model_name} - {self.timestamp}"
```


---

## 4. THIẾT KẾ CƠ SỞ DỮ LIỆU

### 4.1. Sơ đồ ERD (Entity Relationship Diagram)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         DATABASE SCHEMA                                 │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────┐
    │   auth_user          │ (Django Built-in)
    ├──────────────────────┤
    │ id (PK)              │
    │ username (UNIQUE)    │
    │ password             │
    │ email                │
    │ first_name           │
    │ last_name            │
    │ is_staff             │
    │ is_active            │
    │ is_superuser         │
    │ date_joined          │
    │ last_login           │
    └──────────────────────┘
            │
            │ 1:1
            ├─────────────────────────────────────┐
            │                                     │
            ▼                                     ▼
    ┌──────────────────────┐            ┌──────────────────────┐
    │ HoSoBenhNhan         │            │   HoSoBacSi          │
    ├──────────────────────┤            ├──────────────────────┤
    │ id (PK)              │            │ id (PK)              │
    │ nguoi_dung_id (FK)   │            │ nguoi_dung_id (FK)   │
    │ ngay_sinh            │            │ chuyen_khoa_id (FK)  │
    │ gioi_tinh            │            │ mo_ta                │
    │ so_dien_thoai        │            │ bang_cap             │
    │ dia_chi              │            │ so_dien_thoai        │
    │ anh_dai_dien         │            │ phi_kham             │
    └──────────────────────┘            │ anh_dai_dien         │
            │                           └──────────────────────┘
            │ 1:N                               │
            │                                   │ N:1
            │                                   ▼
            │                           ┌──────────────────────┐
            │                           │   ChuyenKhoa         │
            │                           ├──────────────────────┤
            │                           │ id (PK)              │
            │                           │ ten                  │
            │                           │ mo_ta                │
            │                           └──────────────────────┘
            │                                   │
            │                                   │ 1:N
            │                                   ▼
            │                           ┌──────────────────────┐
            │                           │  LichLamViec         │
            │                           ├──────────────────────┤
            │                           │ id (PK)              │
            │                           │ bac_si_id (FK)       │
            │                           │ ngay                 │
            │                           │ gio_bat_dau          │
            │                           │ gio_ket_thuc         │
            │                           │ con_trong            │
            │                           └──────────────────────┘
            │                                   │
            │                                   │ 1:N
            │                                   │
            └───────────────┐                   │
                            │                   │
                            ▼                   ▼
                    ┌──────────────────────────────────┐
                    │         LichHen                  │
                    ├──────────────────────────────────┤
                    │ id (PK)                          │
                    │ benh_nhan_id (FK)                │
                    │ bac_si_id (FK)                   │
                    │ lich_lam_viec_id (FK)            │
                    │ ngay                             │
                    │ gio                              │
                    │ trang_thai                       │
                    │   - pending                      │
                    │   - approved                     │
                    │   - canceled                     │
                    │   - completed                    │
                    │ trieu_chung                      │
                    │ ngay_tao                         │
                    │ ngay_cap_nhat                    │
                    └──────────────────────────────────┘
                                │
                                │ 1:1
                                ▼
                    ┌──────────────────────────────────┐
                    │      HoSoBenhAn                  │
                    ├──────────────────────────────────┤
                    │ id (PK)                          │
                    │ lich_hen_id (FK)                 │
                    │ chan_doan                        │
                    │ ghi_chu                          │
                    │ ngay_tao                         │
                    │ ngay_cap_nhat                    │
                    └──────────────────────────────────┘
                                │
                                │ 1:N
                                ▼
                    ┌──────────────────────────────────┐
                    │        ToaThuoc                  │
                    ├──────────────────────────────────┤
                    │ id (PK)                          │
                    │ ho_so_benh_an_id (FK)            │
                    │ thuoc_id (FK)                    │
                    │ so_luong                         │
                    │ ghi_chu                          │
                    └──────────────────────────────────┘
                                │
                                │ N:1
                                ▼
                    ┌──────────────────────────────────┐
                    │          Thuoc                   │
                    ├──────────────────────────────────┤
                    │ id (PK)                          │
                    │ ten_thuoc                        │
                    │ don_vi                           │
                    └──────────────────────────────────┘

    ┌──────────────────────┐
    │   DanhGiaBacSi       │ (Optional - Rating System)
    ├──────────────────────┤
    │ id (PK)              │
    │ bac_si_id (FK)       │
    │ benh_nhan_id (FK)    │
    │ diem_so (1-5)        │
    │ nhan_xet             │
    │ ngay_danh_gia        │
    └──────────────────────┘
```

### 4.2. Mô tả chi tiết các bảng

#### 4.2.1. Bảng auth_user (Django Built-in)

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK, Auto | ID người dùng |
| username | VARCHAR(150) | UNIQUE, NOT NULL | Tên đăng nhập |
| password | VARCHAR(128) | NOT NULL | Mật khẩu đã hash |
| email | VARCHAR(254) | | Email |
| first_name | VARCHAR(150) | | Tên |
| last_name | VARCHAR(150) | | Họ |
| is_staff | Boolean | DEFAULT False | Quyền admin |
| is_active | Boolean | DEFAULT True | Trạng thái hoạt động |
| is_superuser | Boolean | DEFAULT False | Quyền superuser |
| date_joined | DateTime | AUTO | Ngày tạo tài khoản |
| last_login | DateTime | NULL | Lần đăng nhập cuối |

**Indexes:**
- PRIMARY KEY (id)
- UNIQUE INDEX (username)
- INDEX (email)

#### 4.2.2. Bảng ChuyenKhoa

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK, Auto | ID chuyên khoa |
| ten | VARCHAR(100) | NOT NULL | Tên chuyên khoa |
| mo_ta | TEXT | | Mô tả chuyên khoa |

**Indexes:**
- PRIMARY KEY (id)
- INDEX (ten)

**Sample Data:**
```sql
INSERT INTO accounts_chuyenkhoa (ten, mo_ta) VALUES
('Nội khoa', 'Chuyên khoa điều trị các bệnh nội khoa'),
('Nhi khoa', 'Chuyên khoa điều trị trẻ em'),
('Da liễu', 'Chuyên khoa điều trị bệnh da'),
('Tim mạch', 'Chuyên khoa điều trị bệnh tim mạch'),
('Tiêu hóa', 'Chuyên khoa điều trị bệnh tiêu hóa');
```

#### 4.2.3. Bảng HoSoBenhNhan

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK, Auto | ID hồ sơ |
| nguoi_dung_id | Integer | FK, UNIQUE, NOT NULL | Liên kết User |
| ngay_sinh | Date | NOT NULL | Ngày sinh |
| gioi_tinh | CHAR(1) | NOT NULL | M/F/O |
| so_dien_thoai | VARCHAR(15) | NOT NULL | Số điện thoại |
| dia_chi | TEXT | | Địa chỉ |
| anh_dai_dien | VARCHAR(100) | NULL | Đường dẫn ảnh |

**Indexes:**
- PRIMARY KEY (id)
- UNIQUE INDEX (nguoi_dung_id)
- INDEX (so_dien_thoai)

**Foreign Keys:**
- nguoi_dung_id REFERENCES auth_user(id) ON DELETE CASCADE

#### 4.2.4. Bảng HoSoBacSi

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK, Auto | ID hồ sơ |
| nguoi_dung_id | Integer | FK, UNIQUE, NOT NULL | Liên kết User |
| chuyen_khoa_id | Integer | FK, NULL | Liên kết ChuyenKhoa |
| mo_ta | TEXT | | Mô tả bác sĩ |
| bang_cap | VARCHAR(200) | NOT NULL | Bằng cấp |
| so_dien_thoai | VARCHAR(15) | NOT NULL | Số điện thoại |
| phi_kham | DECIMAL(10,2) | DEFAULT 0 | Phí khám |
| anh_dai_dien | VARCHAR(100) | NULL | Đường dẫn ảnh |

**Indexes:**
- PRIMARY KEY (id)
- UNIQUE INDEX (nguoi_dung_id)
- INDEX (chuyen_khoa_id)
- INDEX (phi_kham)

**Foreign Keys:**
- nguoi_dung_id REFERENCES auth_user(id) ON DELETE CASCADE
- chuyen_khoa_id REFERENCES accounts_chuyenkhoa(id) ON DELETE SET NULL

#### 4.2.5. Bảng LichLamViec

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK, Auto | ID lịch làm việc |
| bac_si_id | Integer | FK, NOT NULL | Liên kết HoSoBacSi |
| ngay | Date | NOT NULL | Ngày làm việc |
| gio_bat_dau | Time | NOT NULL | Giờ bắt đầu |
| gio_ket_thuc | Time | NOT NULL | Giờ kết thúc |
| con_trong | Boolean | DEFAULT True | Còn trống |

**Indexes:**
- PRIMARY KEY (id)
- UNIQUE INDEX (bac_si_id, ngay, gio_bat_dau)
- INDEX (bac_si_id, ngay)
- INDEX (con_trong)

**Foreign Keys:**
- bac_si_id REFERENCES accounts_hosobacsi(id) ON DELETE CASCADE

**Business Rules:**
- gio_ket_thuc > gio_bat_dau
- ngay >= CURRENT_DATE

#### 4.2.6. Bảng LichHen

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK, Auto | ID lịch hẹn |
| benh_nhan_id | Integer | FK, NOT NULL | Liên kết HoSoBenhNhan |
| bac_si_id | Integer | FK, NOT NULL | Liên kết HoSoBacSi |
| lich_lam_viec_id | Integer | FK, NOT NULL | Liên kết LichLamViec |
| ngay | Date | NOT NULL | Ngày khám |
| gio | Time | NOT NULL | Giờ khám |
| trang_thai | VARCHAR(20) | DEFAULT 'pending' | Trạng thái |
| trieu_chung | TEXT | | Triệu chứng |
| ngay_tao | DateTime | AUTO | Ngày tạo |
| ngay_cap_nhat | DateTime | AUTO | Ngày cập nhật |

**Trạng thái:**
- `pending`: Chờ xác nhận
- `approved`: Đã xác nhận
- `canceled`: Đã hủy
- `completed`: Hoàn thành

**Indexes:**
- PRIMARY KEY (id)
- INDEX (benh_nhan_id)
- INDEX (bac_si_id)
- INDEX (ngay, gio)
- INDEX (trang_thai)
- INDEX (bac_si_id, ngay, trang_thai)

**Foreign Keys:**
- benh_nhan_id REFERENCES accounts_hosobenhnhan(id) ON DELETE CASCADE
- bac_si_id REFERENCES accounts_hosobacsi(id) ON DELETE CASCADE
- lich_lam_viec_id REFERENCES appointments_lichlamviec(id) ON DELETE CASCADE

#### 4.2.7. Bảng HoSoBenhAn

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK, Auto | ID hồ sơ bệnh án |
| lich_hen_id | Integer | FK, UNIQUE, NOT NULL | Liên kết LichHen |
| chan_doan | TEXT | NOT NULL | Chẩn đoán |
| ghi_chu | TEXT | | Ghi chú |
| ngay_tao | DateTime | AUTO | Ngày tạo |
| ngay_cap_nhat | DateTime | AUTO | Ngày cập nhật |

**Indexes:**
- PRIMARY KEY (id)
- UNIQUE INDEX (lich_hen_id)
- INDEX (ngay_tao)

**Foreign Keys:**
- lich_hen_id REFERENCES appointments_lichhen(id) ON DELETE CASCADE

#### 4.2.8. Bảng Thuoc

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK, Auto | ID thuốc |
| ten_thuoc | VARCHAR(200) | NOT NULL | Tên thuốc |
| don_vi | VARCHAR(50) | DEFAULT 'viên' | Đơn vị |

**Indexes:**
- PRIMARY KEY (id)
- INDEX (ten_thuoc)

#### 4.2.9. Bảng ToaThuoc

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | PK, Auto | ID toa thuốc |
| ho_so_benh_an_id | Integer | FK, NOT NULL | Liên kết HoSoBenhAn |
| thuoc_id | Integer | FK, NOT NULL | Liên kết Thuoc |
| so_luong | Integer | NOT NULL | Số lượng |
| ghi_chu | VARCHAR(500) | | Ghi chú |

**Indexes:**
- PRIMARY KEY (id)
- INDEX (ho_so_benh_an_id)
- INDEX (thuoc_id)

**Foreign Keys:**
- ho_so_benh_an_id REFERENCES medical_records_hosobenhan(id) ON DELETE CASCADE
- thuoc_id REFERENCES medical_records_thuoc(id) ON DELETE CASCADE

### 4.3. Ràng buộc toàn vẹn (Integrity Constraints)

#### 4.3.1. Entity Integrity

- Mọi bảng đều có PRIMARY KEY
- PRIMARY KEY NOT NULL và UNIQUE
- Auto-increment cho ID

#### 4.3.2. Referential Integrity

**ON DELETE CASCADE:**
- User → HoSoBenhNhan, HoSoBacSi
- HoSoBacSi → LichLamViec
- HoSoBenhNhan, HoSoBacSi → LichHen
- LichHen → HoSoBenhAn
- HoSoBenhAn → ToaThuoc

**ON DELETE SET NULL:**
- ChuyenKhoa → HoSoBacSi (cho phép xóa chuyên khoa)

#### 4.3.3. Domain Integrity

**Check Constraints:**
```sql
-- HoSoBenhNhan
CHECK (gioi_tinh IN ('M', 'F', 'O'))
CHECK (ngay_sinh < CURRENT_DATE)
CHECK (LENGTH(so_dien_thoai) BETWEEN 10 AND 15)

-- HoSoBacSi
CHECK (phi_kham >= 0)

-- LichLamViec
CHECK (gio_ket_thuc > gio_bat_dau)
CHECK (ngay >= CURRENT_DATE)

-- LichHen
CHECK (trang_thai IN ('pending', 'approved', 'canceled', 'completed'))
CHECK (ngay >= CURRENT_DATE OR trang_thai = 'completed')

-- ToaThuoc
CHECK (so_luong > 0)

-- DanhGiaBacSi
CHECK (diem_so BETWEEN 1 AND 5)
```

#### 4.3.4. Business Rules Constraints

**Unique Constraints:**
```sql
-- Một User chỉ có thể là bệnh nhân HOẶC bác sĩ
-- Implemented at application level

-- Một khung giờ chỉ một lịch hẹn
UNIQUE (bac_si_id, ngay, gio_bat_dau) ON LichLamViec

-- Một lịch hẹn chỉ một hồ sơ bệnh án
UNIQUE (lich_hen_id) ON HoSoBenhAn

-- Một bệnh nhân chỉ đánh giá bác sĩ một lần
UNIQUE (bac_si_id, benh_nhan_id) ON DanhGiaBacSi
```

### 4.4. Tối ưu hóa Database

#### 4.4.1. Indexing Strategy

**Composite Indexes:**
```sql
-- Tìm lịch hẹn của bác sĩ theo ngày
CREATE INDEX idx_lichhen_bacsi_ngay ON appointments_lichhen(bac_si_id, ngay);

-- Tìm lịch làm việc còn trống
CREATE INDEX idx_lichlamviec_bacsi_ngay_controng 
ON appointments_lichlamviec(bac_si_id, ngay, con_trong);

-- Tìm lịch hẹn theo trạng thái
CREATE INDEX idx_lichhen_trangthai_ngay ON appointments_lichhen(trang_thai, ngay);
```

#### 4.4.2. Query Optimization

**Django ORM Optimization:**
```python
# BAD - N+1 query problem
lich_hen_list = LichHen.objects.all()
for lich_hen in lich_hen_list:
    print(lich_hen.benh_nhan.nguoi_dung.get_full_name())  # N queries

# GOOD - Use select_related for ForeignKey
lich_hen_list = LichHen.objects.select_related(
    'benh_nhan__nguoi_dung',
    'bac_si__nguoi_dung',
    'bac_si__chuyen_khoa'
).all()  # 1 query with JOIN

# GOOD - Use prefetch_related for reverse ForeignKey
bac_si_list = HoSoBacSi.objects.prefetch_related(
    'lich_hen__benh_nhan__nguoi_dung'
).all()
```

#### 4.4.3. Database Normalization

**Current Normalization Level: 3NF (Third Normal Form)**

**Justification:**
- Không có transitive dependencies
- Mọi non-key attribute phụ thuộc trực tiếp vào primary key
- Giảm thiểu data redundancy

**Denormalization Considerations (Future):**
```python
# Add computed fields for performance
class HoSoBacSi(models.Model):
    # ... existing fields
    tong_lich_hen = models.IntegerField(default=0)  # Cache
    diem_danh_gia_trung_binh = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    
    def cap_nhat_thong_ke(self):
        self.tong_lich_hen = self.lich_hen.count()
        self.diem_danh_gia_trung_binh = self.danh_gia.aggregate(Avg('diem_so'))['diem_so__avg'] or 0
        self.save()
```

