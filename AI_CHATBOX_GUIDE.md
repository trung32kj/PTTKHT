# 🤖 AI CHATBOX - HƯỚNG DẪN SỬ DỤNG

## 📋 Tổng quan
AI Chatbox là tính năng tư vấn triệu chứng tự động, giúp bệnh nhân:
- Mô tả triệu chứng
- Nhận gợi ý chuyên khoa phù hợp
- Chọn bác sĩ rating cao nhất
- Đặt lịch hẹn trực tiếp

## 🚀 Cài đặt nhanh

### 1. Chạy script setup
```bash
setup_ai_chatbox.bat
```

### 2. Khởi động server
```bash
python manage.py runserver
```

### 3. Truy cập website
- URL: http://127.0.0.1:8000
- Đăng nhập với tài khoản bệnh nhân
- Widget AI sẽ xuất hiện ở góc dưới phải

## 🎯 Cách sử dụng

### Cho bệnh nhân:
1. **Mở widget**: Click vào icon robot ở góc dưới phải
2. **Mô tả triệu chứng**: Gõ triệu chứng vào chat (VD: "Tôi bị đau đầu và sốt")
3. **Nhận gợi ý**: AI sẽ phân tích và đề xuất chuyên khoa + danh sách bác sĩ
4. **Chọn bác sĩ**: Click vào bác sĩ muốn khám
5. **Chọn thời gian**: Chọn lịch trống phù hợp
6. **Xác nhận**: Đặt lịch thành công

### Cho admin:
- Quản lý chat sessions trong Django Admin
- Xem thống kê phân tích triệu chứng
- Theo dõi gợi ý bác sĩ

## 🔧 Cấu hình

### OpenAI API (Tùy chọn):
```python
# settings.py
OPENAI_API_KEY = 'your-api-key-here'
```

### Chuyên khoa mapping:
Hệ thống tự động phân tích dựa trên từ khóa:
- **Tim mạch**: tim, ngực, đau ngực, khó thở
- **Nội khoa**: sốt, đau đầu, mệt mỏi
- **Tai mũi họng**: ho, đau họng, nghẹt mũi
- **Tiêu hóa**: đau bụng, tiêu chảy, nôn

## 📊 Tính năng

### ✅ Đã hoàn thành:
- Widget chat thu nhỏ như Messenger
- Phân tích triệu chứng nhanh (không cần OpenAI)
- Gợi ý bác sĩ theo rating
- Đặt lịch hẹn tự động
- Responsive design
- CSRF protection
- Error handling

### 🔄 Flow hoạt động:
```
User nhập triệu chứng
↓
AI phân tích chuyên khoa (dựa từ khóa)
↓
Query bác sĩ rating cao nhất
↓
Hiển thị danh sách bác sĩ
↓
User chọn bác sĩ
↓
Kiểm tra tối ưu (cảnh báo nếu không phù hợp)
↓
Lấy lịch trống gần nhất
↓
User chọn thời gian
↓
Tạo appointment → Lưu database
```

## 🐛 Troubleshooting

### Lỗi thường gặp:

1. **Widget không hiển thị**:
   - Kiểm tra user đã đăng nhập
   - Đảm bảo user có profile bệnh nhân

2. **Không gửi được tin nhắn**:
   - Kiểm tra CSRF token
   - Xem console browser để debug

3. **Không có bác sĩ gợi ý**:
   - Tạo ít nhất 1 bác sĩ trong admin
   - Kiểm tra chuyên khoa đã được tạo

4. **Lỗi đặt lịch**:
   - Đảm bảo có lịch làm việc cho bác sĩ
   - Kiểm tra lịch còn trống (con_trong=True)

### Debug commands:
```bash
# Kiểm tra models
python manage.py shell
>>> from ai_chatbox.models import *
>>> ChatSession.objects.all()

# Test service
python test_ai_chatbox.py

# Xem logs
python manage.py runserver --verbosity=2
```

## 📱 Responsive Design

Widget tự động điều chỉnh theo màn hình:
- **Desktop**: 350px width, góc dưới phải
- **Mobile**: Full width - 40px, height 70vh
- **Tablet**: Tự động scale

## 🔒 Bảo mật

- CSRF protection enabled
- Login required cho tất cả API
- Input validation
- SQL injection prevention
- XSS protection

## 📈 Performance

- Phân tích triệu chứng nhanh (< 100ms)
- Lazy loading cho widget
- Optimized database queries
- Minimal JavaScript footprint

## 🎨 Customization

### Thay đổi giao diện:
Chỉnh sửa file `templates/ai_chatbox/widget.html`:
- Colors: Sửa CSS variables
- Size: Thay đổi width/height
- Position: Điều chỉnh bottom/right

### Thêm chuyên khoa:
```python
# ai_chatbox/services.py
specialty_keywords = {
    'your_specialty': ['keyword1', 'keyword2'],
    # ...
}
```

## 📞 Hỗ trợ

Nếu gặp vấn đề:
1. Chạy `python test_ai_chatbox.py`
2. Kiểm tra Django admin
3. Xem browser console
4. Check server logs

---
**Phiên bản**: 1.0  
**Cập nhật**: 2026-03-04  
**Tương thích**: Django 5.2+, Python 3.8+