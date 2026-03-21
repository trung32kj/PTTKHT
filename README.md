# Hệ thống Quản lý Phòng khám & Đặt lịch Khám trực tuyến

## Tính năng chính

### 1. Bệnh nhân (Patient)
- Đăng ký / đăng nhập
- Cập nhật hồ sơ cá nhân
- Xem danh sách bác sĩ theo chuyên khoa
- Xem lịch làm việc của bác sĩ
- Đặt lịch khám theo giờ
- Xem lịch sử khám
- Hủy lịch hẹn

### 2. Bác sĩ (Doctor)
- Đăng nhập
- Xác nhận lịch hẹn
- Hủy / đổi lịch
- Ghi hồ sơ khám bệnh (Medical record)
- Xem danh sách bệnh nhân đã khám
- Thay đổi lịch làm việc (Schedule)

### 3. Admin
- Quản lý bác sĩ
- Quản lý bệnh nhân
- Quản lý chuyên khoa
- Quản lý lịch khám
- Xem báo cáo thống kê
- Gửi thông báo cho người dùng

## Cài đặt

1. Tạo virtual environment:
```bash
python -m venv venv
```

2. Kích hoạt virtual environment:
```bash
# Windows
.\venv\Scripts\activate
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

4. Chạy migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Tạo superuser (admin):
```bash
python manage.py createsuperuser
```

6. Chạy server:
```bash
python manage.py runserver
```

7. Truy cập:
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Cấu trúc Database

- **User**: Django Auth (username, password, role)
- **PatientProfile**: Hồ sơ bệnh nhân (ngày sinh, giới tính, SĐT, địa chỉ)
- **DoctorProfile**: Hồ sơ bác sĩ (chuyên khoa, mô tả, bằng cấp, phí khám)
- **Specialty**: Chuyên khoa
- **Schedule**: Lịch làm việc bác sĩ
- **Appointment**: Lịch hẹn khám
- **MedicalRecord**: Hồ sơ bệnh án

## Hướng dẫn sử dụng

### Bước 1: Tạo dữ liệu mẫu qua Admin
1. Đăng nhập admin
2. Tạo Chuyên khoa (Specialty)
3. Tạo User cho bác sĩ
4. Tạo DoctorProfile liên kết với User
5. Tạo Schedule (lịch làm việc) cho bác sĩ

### Bước 2: Đăng ký bệnh nhân
1. Truy cập trang đăng ký
2. Điền thông tin và đăng ký

### Bước 3: Đặt lịch khám
1. Đăng nhập với tài khoản bệnh nhân
2. Xem danh sách bác sĩ
3. Chọn bác sĩ và xem lịch làm việc
4. Đặt lịch khám

### Bước 4: Bác sĩ xác nhận và khám
1. Đăng nhập với tài khoản bác sĩ
2. Xem lịch hẹn chờ xác nhận
3. Xác nhận lịch hẹn
4. Sau khi khám, ghi hồ sơ bệnh án

## Công nghệ sử dụng
- Django 5.2.8
- SQLite
- HTML/CSS
- Python 3.14
