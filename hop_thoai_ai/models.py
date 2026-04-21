from django.db import models
from django.contrib.auth.models import User
from tai_khoan.models import HoSoBacSi, ChuyenKhoa


class ChatSession(models.Model):
    """Phiên chat với AI"""
    benh_nhan = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_sessions')
    session_id = models.CharField(max_length=100, unique=True, verbose_name="ID phiên")
    ngay_tao = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    trang_thai = models.CharField(max_length=20, choices=[
        ('active', 'Đang hoạt động'),
        ('completed', 'Hoàn thành'),
        ('cancelled', 'Đã hủy')
    ], default='active', verbose_name="Trạng thái")
    
    class Meta:
        verbose_name = "Phiên chat"
        verbose_name_plural = "Phiên chat"
        ordering = ['-ngay_tao']
    
    def __str__(self):
        return f"Chat {self.session_id} - {self.benh_nhan.username}"


class ChatMessage(models.Model):
    """Tin nhắn trong chat"""
    NGUOI_GUI_CHOICES = [
        ('user', 'Người dùng'),
        ('ai', 'AI'),
        ('system', 'Hệ thống')
    ]
    
    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    nguoi_gui = models.CharField(max_length=10, choices=NGUOI_GUI_CHOICES, verbose_name="Người gửi")
    noi_dung = models.TextField(verbose_name="Nội dung")
    thoi_gian = models.DateTimeField(auto_now_add=True, verbose_name="Thời gian")
    metadata = models.JSONField(blank=True, null=True, verbose_name="Dữ liệu bổ sung")
    
    class Meta:
        verbose_name = "Tin nhắn chat"
        verbose_name_plural = "Tin nhắn chat"
        ordering = ['thoi_gian']
    
    def __str__(self):
        return f"{self.nguoi_gui}: {self.noi_dung[:50]}..."


class TrieuChungAnalysis(models.Model):
    """Phân tích triệu chứng từ AI"""
    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='analyses')
    trieu_chung_goc = models.TextField(verbose_name="Triệu chứng gốc")
    chuyen_khoa_de_xuat = models.ForeignKey(ChuyenKhoa, on_delete=models.SET_NULL, null=True, verbose_name="Chuyên khoa đề xuất")
    do_tin_cay = models.FloatField(default=0.0, verbose_name="Độ tin cậy (%)")
    phan_tich_chi_tiet = models.JSONField(verbose_name="Phân tích chi tiết")
    ngay_phan_tich = models.DateTimeField(auto_now_add=True, verbose_name="Ngày phân tích")
    
    class Meta:
        verbose_name = "Phân tích triệu chứng"
        verbose_name_plural = "Phân tích triệu chứng"
        ordering = ['-ngay_phan_tich']
    
    def __str__(self):
        return f"Phân tích: {self.chuyen_khoa_de_xuat} - {self.do_tin_cay}%"


class BacSiRecommendation(models.Model):
    """Gợi ý bác sĩ từ AI"""
    analysis = models.ForeignKey(TrieuChungAnalysis, on_delete=models.CASCADE, related_name='recommendations')
    bac_si = models.ForeignKey(HoSoBacSi, on_delete=models.CASCADE, verbose_name="Bác sĩ")
    thu_tu_uu_tien = models.IntegerField(verbose_name="Thứ tự ưu tiên")
    ly_do_goi_y = models.TextField(verbose_name="Lý do gợi ý")
    rating_score = models.FloatField(verbose_name="Điểm rating")
    
    class Meta:
        verbose_name = "Gợi ý bác sĩ"
        verbose_name_plural = "Gợi ý bác sĩ"
        ordering = ['thu_tu_uu_tien']
    
    def __str__(self):
        return f"{self.thu_tu_uu_tien}. {self.bac_si} - {self.rating_score}"


class CachedSymptomAnalysis(models.Model):
    """Cache kết quả phân tích triệu chứng để tái sử dụng.
    Khi bệnh nhân hỏi triệu chứng, kết quả sẽ được lưu ở đây.
    Lần sau có người hỏi tương tự, hệ thống sẽ trả từ cache thay vì phân tích lại.
    """
    PHUONG_PHAP_CHOICES = [
        ('keyword', 'Từ khóa'),
        ('ai', 'AI Gemini'),
        ('keyword_fallback', 'Từ khóa (dự phòng)')
    ]

    trieu_chung = models.TextField(verbose_name="Triệu chứng gốc")
    trieu_chung_chuan_hoa = models.CharField(
        max_length=500,
        verbose_name="Triệu chứng chuẩn hóa",
        db_index=True,
        help_text="Dạng lowercase + trim để so sánh nhanh"
    )
    chuyen_khoa = models.ForeignKey(
        ChuyenKhoa, on_delete=models.CASCADE,
        related_name='cached_analyses',
        verbose_name="Chuyên khoa"
    )
    do_tin_cay = models.FloatField(verbose_name="Độ tin cậy (%)")
    phan_tich_chi_tiet = models.JSONField(verbose_name="Phân tích chi tiết")
    phuong_phap = models.CharField(
        max_length=20, choices=PHUONG_PHAP_CHOICES,
        verbose_name="Phương pháp phân tích"
    )
    so_lan_su_dung = models.IntegerField(default=1, verbose_name="Số lần sử dụng")
    ngay_tao = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    ngay_cap_nhat = models.DateTimeField(auto_now=True, verbose_name="Cập nhật lần cuối")

    class Meta:
        verbose_name = "Cache phân tích triệu chứng"
        verbose_name_plural = "Cache phân tích triệu chứng"
        ordering = ['-so_lan_su_dung', '-ngay_cap_nhat']

    def __str__(self):
        return f"[{self.phuong_phap}] {self.trieu_chung[:50]} → {self.chuyen_khoa} ({self.so_lan_su_dung} lần)"