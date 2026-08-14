# Thiết kế hệ thống điểm danh QR Code - Google Sheets + Zalo Business

## 1. Kiến trúc hệ thống

### Lựa chọn nền tảng: AppSheet (Khuyên dùng)

**Lý do chọn AppSheet:**
- Tích hợp sẵn với Google Sheets
- Hỗ trợ QR code scanning native
- Miễn phí cho đến 10 users, sau đó $10/user/tháng
- Automation mạnh mẽ với AppSheet Automation
- Dễ dàng mở rộng thêm cơ sở mới

**Glide Apps (Phương án thay thế):**
- Giao diện đẹp hơn
- Free plan giới hạn tính năng
- Khó tích hợp automation phức tạp

---

## 2. Cấu trúc Database (Google Sheets)

### Sheet 1: `HocVien` (Danh sách học viên)
| Column | Type | Mô tả |
|--------|------|-------|
| MaHocVien | TEXT | ID tự động (HV + timestamp) |
| HoTen | TEXT | Họ tên học viên |
| SoDienThoai | TEXT | Số điện thoại (unique) |
| BoMon | TEXT | Bộ môn (Yoga, Gym, Kickfit...) |
| CoSo | TEXT | Cơ sở đăng ký (Cơ sở 1, 2, 3) |
| NgayDangKy | DATE | Ngày đăng ký |
| LoaiThe | TEXT | Loại thẻ (Tháng, Quý, Năm) |
| NgayBatDau | DATE | Ngày bắt đầu thẻ |
| NgayKetThuc | DATE | Ngày kết thúc thẻ |
| SoLanDaDiemDanh | NUMBER | Số lần đã điểm danh |
| TrangThai | TEXT | Active/Expired/Trial |
| ZaloID | TEXT | ID Zalo (để gửi tin nhắn cá nhân) |

### Sheet 2: `CoSo` (Danh sách cơ sở)
| Column | Type | Mô tả |
|--------|------|-------|
| MaCoSo | TEXT | ID cơ sở (CS1, CS2, CS3) |
| TenCoSo | TEXT | Tên cơ sở |
| DiaChi | TEXT | Địa chỉ |
| QRCodeURL | IMAGE | URL QR code của cơ sở |
| ZaloGroupID | TEXT | ID nhóm Zalo để thông báo |

### Sheet 3: `DiemDanh` (Lịch sử điểm danh)
| Column | Type | Mô tả |
|--------|------|-------|
| MaDiemDanh | TEXT | ID tự động (DD + timestamp) |
| MaHocVien | TEXT | Khóa ngoại đến HocVien |
| MaCoSo | TEXT | Khóa ngoại đến CoSo |
| ThoiGianCheckIn | DATETIME | Thời gian quét QR |
| ThoiGianCheckOut | DATETIME | Thời gian check-out (tuỳ chọn) |
| Ca | TEXT | Ca (Sáng, Chiều, Tối) |
| TrangThai | TEXT | Completed/Duplicate |

### Sheet 4: `DangKyThu` (Đăng ký tập thử)
| Column | Type | Mô tả |
|--------|------|-------|
| MaDangKy | TEXT | ID tự động (DK + timestamp) |
| HoTen | TEXT | Họ tên |
| SoDienThoai | TEXT | Số điện thoại |
| BoMon | TEXT | Bộ môn muốn thử |
| CoSoQuet | TEXT | Cơ sở quét QR |
| ThoiGianDangKy | DATETIME | Thời gian đăng ký |
| TrangThai | TEXT | Pending/Contacted/Converted |

### Sheet 5: `NguoiDung` (Quản lý Admin/Staff)
| Column | Type | Mô tả |
|--------|------|-------|
| MaNguoiDung | TEXT | ID tự động (ND + timestamp) |
| Email | TEXT | Email đăng nhập AppSheet |
| HoTen | TEXT | Họ tên |
| VaiTro | TEXT | Admin/Staff/Manager |
| CoSoQuanLy | TEXT | Cơ sở được quản lý (All/CS1/CS2/CS3) |
| QuyenHan | TEXT | Danh sách quyền (cách nhau bởi dấu phẩy) |
| TrangThai | TEXT | Active/Inactive |
| NgayTao | DATE | Ngày tạo tài khoản |

### Sheet 6: `GoiTap` (Gói tập/Thẻ thành viên)
| Column | Type | Mô tả |
|--------|------|-------|
| MaGoi | TEXT | ID gói (GT + timestamp) |
| TenGoi | TEXT | Tên gói (Tháng Yoga, Quý Gym...) |
| BoMon | TEXT | Bộ môn áp dụng |
| SoBuoi | NUMBER | Số buổi tập |
| GiaTien | CURRENCY | Giá tiền |
| ThoiHan | NUMBER | Thời hạn (ngày) |
| TrangThai | TEXT | Active/Inactive |

### Sheet 7: `LichSuGiaHan` (Lịch sử gia hạn thẻ)
| Column | Type | Mô tả |
|--------|------|-------|
| MaGiaHan | TEXT | ID tự động (GH + timestamp) |
| MaHocVien | TEXT | Khóa ngoại đến HocVien |
| MaGoi | TEXT | Khóa ngoại đến GoiTap |
| NgayGiaHan | DATE | Ngày gia hạn |
| NgayBatDau | DATE | Ngày bắt đầu hiệu lực |
| NgayKetThuc | DATE | Ngày kết thúc hiệu lực |
| SoTien | CURRENCY | Số tiền thanh toán |
| NguoiTao | TEXT | Người thực hiện gia hạn |
| GhiChu | TEXT | Ghi chú |

### Sheet 8: `BaoCao` (Báo cáo thống kê)
| Column | Type | Mô tả |
|--------|------|-------|
| MaBaoCao | TEXT | ID tự động (BC + timestamp) |
| LoaiBaoCao | TEXT | Daily/Weekly/Monthly |
| NgayBaoCao | DATE | Ngày báo cáo |
| CoSo | TEXT | Cơ sở báo cáo |
| TongHocVien | NUMBER | Tổng số học viên |
| SoHocVienMoi | NUMBER | Số học viên mới |
| SoDiemDanh | NUMBER | Tổng số điểm danh |
| DoanhThu | CURRENCY | Doanh thu |
| NgayTao | DATETIME | Thời gian tạo báo cáo |

---

## 3. Workflow quét QR Code

### 3.1 Tạo QR Code cho từng cơ sở
```
Format: https://script.google.com/.../exec?coso=CS1&bomon=Yoga
```

- Mỗi cơ sở + bộ môn có 1 QR code riêng
- Dán QR code cố định tại cửa từng bộ môn
- Sử dụng Google Apps Script để xử lý

### 3.2 Luồng xử lý khi quét QR

**Bước 1: Học viên quét QR**
- Mở AppSheet app trên điện thoại
- Chọn "Quét QR" → Camera mở
- Quét QR code tại cơ sở

**Bước 2: Xác định học viên**
- AppSheet kiểm tra số điện thoại đã đăng ký chưa
- Nếu **CHƯA** → Hiển thị form đăng ký tập thử
- Nếu **ĐÃ CÓ** → Hiển thị thông tin học viên

**Bước 3: Hiển thị thông tin (Học viên cũ)**
```
┌─────────────────────────────┐
│ Họ tên: Nguyễn Văn A         │
│ Bộ môn: Yoga                │
│ Thẻ: Tháng                  │
│ Hạn thẻ còn: 15 ngày        │
│ Số lần đã đi: 20/30         │
│                             │
│ [CHECK-IN]  [CHECK-OUT]     │
└─────────────────────────────┘
```

**Bước 4: Xử lý Check-in**
- Kiểm tra trùng lặp trong ngày (cùng số điện thoại + cùng cơ sở)
- Nếu **TRÙNG** → Hiển thị thông báo "Bạn đã điểm danh hôm nay"
- Nếu **KHÔNG** → Ghi nhận điểm danh + Bắn thông báo Zalo

---

## 4. Tích hợp Zalo Business API

### 4.1 Cấu hình Zalo Business Account

**Bước chuẩn bị:**
1. Đăng ký Zalo Business Account
2. Tạo Zalo OA (Official Account)
3. Lấy `OA_ID` và `SECRET_KEY`
4. Tạo Zalo Group cho từng cơ sở
5. Lấy `GROUP_ID` của từng nhóm

### 4.2 Google Apps Script gửi tin nhắn Zalo

```javascript
function sendZaloNotification(message, groupId) {
  var zaloApiUrl = "https://openapi.zalo.me/v2/group/message";
  
  var payload = {
    "oa_id": "YOUR_OA_ID",
    "group_id": groupId,
    "message": {
      "text": message
    },
    "timestamp": Math.floor(Date.now() / 1000)
  };
  
  var options = {
    "method": "post",
    "contentType": "application/json",
    "headers": {
      "access_token": "YOUR_ACCESS_TOKEN"
    },
    "payload": JSON.stringify(payload),
    "muteHttpExceptions": true
  };
  
  var response = UrlFetchApp.fetch(zaloApiUrl, options);
  return JSON.parse(response.getContentText());
}
```

### 4.3 Nội dung thông báo

**Format tin nhắn:**
```
🔔 THÔNG BÁO ĐIỂM DANH
━━━━━━━━━━━━━━━━━━
👤 Học viên: Nguyễn Văn A
📱 SĐT: 0912345678
🏋️ Bộ môn: Yoga
📍 Cơ sở: Cơ sở 1 - Quận 1
⏰ Thời gian: 11/07/2026 08:30
📊 Thẻ còn: 15 ngày
━━━━━━━━━━━━━━━━━━
```

---

## 5. Logic chặn trùng lặp

### 5.1 Rule trong AppSheet

**Expression:**
```
COUNT(
  SELECT(DiemDanh[MaDiemDanh], 
    AND(
      [MaHocVien] = [_THISROW].[MaHocVien],
      [MaCoSo] = [_THISROW].[MaCoSo],
      DATE([ThoiGianCheckIn]) = TODAY()
    )
  )
) = 0
```

### 5.2 Workflow Automation

**Trigger:** Khi record mới được tạo trong `DiemDanh`

**Action:**
1. Kiểm tra trùng lặp
2. Nếu trùng → Delete record + Send notification "Đã điểm danh hôm nay"
3. Nếu không trùng → Keep record + Send Zalo notification

---

## 6. Flow đăng ký học viên mới

### 6.1 Form đăng ký tập thử

```
┌─────────────────────────────┐
│ ĐĂNG KÝ TẬP THỬ            │
├─────────────────────────────┤
│ Họ tên: [__________]        │
│ SĐT:   [__________]         │
│ Bộ môn: [Dropdown ▼]        │
│   - Yoga                    │
│   - Gym                     │
│   - Kickfit                 │
│                             │
│ [ĐĂNG KÝ NGAY]              │
└─────────────────────────────┘
```

### 6.2 Xử lý sau đăng ký

1. Lưu vào sheet `DangKyThu`
2. Gửi thông báo Zalo đến nhóm quản lý
3. Staff sẽ liên hệ để chuyển thành học viên chính thức
4. Staff thủ công thêm vào sheet `HocVien`

---

## 7. Admin Dashboard (Quản trị viên)

### 7.1 Màn hình Dashboard chính

```
┌─────────────────────────────────────────────┐
│  DASHBOARD QUẢN LÝ - CƠ SỞ 1                │
├─────────────────────────────────────────────┤
│  📊 THỐNG KÊ HÔM NAY                        │
│  ├─ Tổng học viên: 156                       │
│  ├─ Đã điểm danh: 89                         │
│  ├─ Học viên mới: 3                          │
│  └─ Doanh thu: 5.400.000đ                    │
│                                              │
│  📈 BIỂU ĐỒ ĐIỂM DANH (7 ngày)              │
│  [Chart: Số lượng điểm danh theo ngày]      │
│                                              │
│  🔔 THÔNG BÁO GẦN ĐÂY                       │
│  ├─ Nguyễn Văn A vừa gia hạn thẻ Yoga       │
│  ├─ 3 đăng ký tập thử chưa liên hệ           │
│  └─ 5 học viên sắp hết hạn thẻ              │
└─────────────────────────────────────────────┘
```

### 7.2 Quản lý học viên

**Chức năng:**
- **Danh sách học viên:** Xem, tìm kiếm, lọc theo cơ sở/bộ môn/trạng thái
- **Thêm học viên:** Form nhập thông tin đầy đủ
- **Sửa thông tin:** Cập nhật tên, SĐT, bộ môn, cơ sở
- **Gia hạn thẻ:** Chọn gói tập, tính ngày kết thúc tự động
- **Xóa học viên:** Xóa mềm (đánh dấu inactive)
- **Xem lịch sử điểm danh:** Chi tiết từng lần check-in/check-out
- **Xem lịch sử gia hạn:** Lịch sử thanh toán thẻ

**Filter nâng cao:**
- Theo cơ sở
- Theo bộ môn
- Theo trạng thái thẻ (Active/Expired/Trial)
- Theo thời gian đăng ký
- Theo số lần điểm danh

### 7.3 Quản lý điểm danh

**Chức năng:**
- **Xem lịch sử điểm danh:** Tất cả hoặc theo ngày/cơ sở
- **Điểm danh thủ công:** Admin có thể điểm danh thay học viên
- **Sửa điểm danh:** Điều chỉnh thời gian check-in/check-out
- **Xóa điểm danh:** Xóa record điểm danh sai
- **Export dữ liệu:** Xuất Excel/PDF theo khoảng thời gian

**Báo cáo điểm danh:**
- Báo cáo ngày: Tổng số điểm danh theo cơ sở/bộ môn
- Báo cáo tuần: Tổng hợp điểm danh 7 ngày
- Báo cáo tháng: Thống kê điểm danh tháng
- Báo cáo học viên vắng: Danh sách học viên không đi tập

### 7.4 Quản lý gói tập

**Chức năng:**
- **Danh sách gói tập:** Xem tất cả gói đang active
- **Thêm gói mới:** Tạo gói tập với tên, số buổi, giá, thời hạn
- **Sửa gói:** Cập nhật thông tin gói
- **Xóa gói:** Xóa gói không còn sử dụng
- **Gán gói cho bộ môn:** Gói áp dụng cho bộ môn nào

**Gợi ý gói tập:**
- Tháng Yoga: 12 buổi - 800.000đ - 30 ngày
- Tháng Gym: Không giới hạn - 1.200.000đ - 30 ngày
- Quỹ Yoga: 36 buổi - 2.000.000đ - 90 ngày
- Năm Gym: Không giới hạn - 10.000.000đ - 365 ngày

### 7.5 Quản lý đăng ký tập thử

**Chức năng:**
- **Danh sách đăng ký:** Xem tất cả đăng ký tập thử
- **Cập nhật trạng thái:** Pending → Contacted → Converted
- **Ghi chú liên hệ:** Thêm ghi chú sau khi gọi điện
- **Chuyển thành học viên:** Tự động chuyển sang sheet HocVien
- **Gửi tin nhắn Zalo:** Gửi tin nhắn mời tập thử

### 7.6 Quản lý người dùng (Admin/Staff)

**Chức năng:**
- **Danh sách user:** Xem tất cả admin/staff
- **Thêm user:** Tạo tài khoản với vai trò và quyền hạn
- **Phân quyền:** Gán quyền theo vai trò
- **Gán cơ sở:** User quản lý cơ sở nào (All hoặc cụ thể)
- **Khoá/Mở khoá:** Kích hoạt/vô hiệu hóa tài khoản

**Quyền hạn (Permissions):**
- `view_dashboard`: Xem dashboard
- `manage_students`: Quản lý học viên
- `manage_attendance`: Quản lý điểm danh
- `manage_packages`: Quản lý gói tập
- `manage_users`: Quản lý người dùng (chỉ Admin)
- `view_reports`: Xem báo cáo
- `export_data`: Xuất dữ liệu

**Vai trò mặc định:**
- **Admin:** Toàn bộ quyền
- **Manager:** view_dashboard, manage_students, manage_attendance, manage_packages, view_reports, export_data
- **Staff:** manage_attendance, view_reports

### 7.7 Báo cáo & Thống kê

**Các loại báo cáo:**

**Báo cáo doanh thu:**
- Doanh thu theo ngày/tuần/tháng
- Doanh thu theo cơ sở
- Doanh thu theo bộ môn
- Doanh thu theo gói tập

**Báo cáo học viên:**
- Số lượng học viên mới theo tháng
- Tỷ lệ chuyển đổi từ tập thử → chính thức
- Số học viên active/expired
- Học viên sắp hết hạn thẻ

**Báo cáo điểm danh:**
- Tỷ lệ điểm danh (số lần đi / số buổi thẻ)
- Giờ cao điểm điểm danh
- Số điểm danh theo cơ sở/bộ môn
- Học viên đi nhiều nhất

**Báo cáo nhân sự:**
- Số điểm danh được xử lý bởi từng staff
- Hiệu suất liên hệ đăng ký tập thử

### 7.8 Cài đặt hệ thống

**Chức năng:**
- **Cấu hình cơ sở:** Thêm/sửa/xóa cơ sở mới
- **Cấu hình bộ môn:** Thêm/sửa/xóa bộ môn
- **Cấu hình QR code:** Tạo mới QR code cho cơ sở/bộ môn
- **Cấu hình Zalo:** Cập nhật OA_ID, Access Token, Group IDs
- **Cấu hình thời gian:** Định nghĩa ca (Sáng: 6-12, Chiều: 12-18, Tối: 18-22)
- **Backup dữ liệu:** Tự động backup Google Sheets
- **Xóa dữ liệu cũ:** Cleanup dữ liệu điểm danh cũ hơn X tháng

---

## 8. Implementation Steps

### Phase 1: Setup (1-2 ngày)
- [ ] Tạo Google Sheets với cấu trúc trên
- [ ] Đăng ký Zalo Business Account
- [ ] Lấy API keys Zalo
- [ ] Tạo Google Apps Script xử lý QR

### Phase 2: AppSheet Development (5-7 ngày)
- [ ] Kết nối Google Sheets với AppSheet
- [ ] Design UI cho học viên (QR scanning, check-in)
- [ ] Design Admin Dashboard
- [ ] Implement quản lý học viên (CRUD)
- [ ] Implement quản lý điểm danh
- [ ] Implement quản lý gói tập
- [ ] Implement quản lý người dùng & phân quyền
- [ ] Implement báo cáo & thống kê
- [ ] Setup automation rules
- [ ] Test flow điểm danh

### Phase 3: Zalo Integration (2-3 ngày)
- [ ] Implement Apps Script gửi Zalo
- [ ] Test notification
- [ ] Setup message templates

### Phase 4: Testing & Deployment (3-4 ngày)
- [ ] Test tại 1 cơ sở
- [ ] Test Admin Dashboard đầy đủ
- [ ] Test phân quyền user
- [ ] Fix bugs
- [ ] Deploy cho 3 cơ sở
- [ ] Training staff

---

## 9. Chi phí ước tính

| Item | Chi phí |
|------|---------|
| Google Sheets | Miễn phí |
| AppSheet | $10/user × 5 staff = $50/tháng |
| Zalo Business | Miễn phí (nếu < 10k tin/tháng) |
| QR Code in ấn | ~$50/lần |
| **Tổng** | **~$50/tháng** |

---

## 10. Mở rộng tương lai

- Tích hợp thanh toán thẻ tự động
- Dashboard thống kê doanh thu
- Hệ thống đặt lịch tập
- Tích hợp camera nhận diện khuôn mặt
- Mobile app riêng cho chuỗi

---

## 11. Lưu ý quan trọng

1. **Security:** Không lưu thông tin nhạy cảm (CCCD, v.v.)
2. **Backup:** Tự động backup Google Sheets hàng ngày
3. **Offline:** AppSheet hỗ trợ offline mode
4. **Scalability:** Dễ dàng thêm cơ sở mới chỉ cần thêm row trong sheet `CoSo`
5. **Performance:** Google Sheets giới hạn 10M cells, cần cleanup dữ liệu cũ định kỳ
