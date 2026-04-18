from django.db import models
from django.contrib.auth.models import User

class ChuyenKhoa(models.Model):
    ten = models.CharField(max_length=100, verbose_name="Tên chuyên khoa")
    mo_ta = models.TextField(blank=True, verbose_name="Mô tả")
    
    class Meta:
        verbose_name = "Chuyên khoa"
        verbose_name_plural = "Chuyên khoa"
    
    def __str__(self):
        return self.ten

class HoSoBenhNhan(models.Model):
    GIOI_TINH_CHOICES = [
        ('M', 'Nam'),
        ('F', 'Nữ'),
        ('O', 'Khác'),
    ]
    
    nguoi_dung = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ho_so_benh_nhan')
    ngay_sinh = models.DateField(verbose_name="Ngày sinh")
    gioi_tinh = models.CharField(max_length=1, choices=GIOI_TINH_CHOICES, verbose_name="Giới tính")
    so_dien_thoai = models.CharField(max_length=15, verbose_name="Số điện thoại")
    dia_chi = models.TextField(blank=True, verbose_name="Địa chỉ")
    anh_dai_dien = models.ImageField(upload_to='benh_nhan/', blank=True, null=True, verbose_name="Ảnh đại diện")
    
    class Meta:
        verbose_name = "Hồ sơ bệnh nhân"
        verbose_name_plural = "Hồ sơ bệnh nhân"
    
    def __str__(self):
        return f"{self.nguoi_dung.get_full_name()} - {self.so_dien_thoai}"

class HoSoBacSi(models.Model):
    nguoi_dung = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ho_so_bac_si')
    chuyen_khoa = models.ForeignKey(ChuyenKhoa, on_delete=models.SET_NULL, null=True, verbose_name="Chuyên khoa")
    mo_ta = models.TextField(blank=True, verbose_name="Mô tả")
    bang_cap = models.CharField(max_length=200, verbose_name="Bằng cấp")
    so_dien_thoai = models.CharField(max_length=15, verbose_name="Số điện thoại")
    phi_kham = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Phí khám")
    anh_dai_dien = models.ImageField(upload_to='bac_si/', blank=True, null=True, verbose_name="Ảnh đại diện")
    
    class Meta:
        verbose_name = "Hồ sơ bác sĩ"
        verbose_name_plural = "Hồ sơ bác sĩ"
    
    def __str__(self):
        return f"BS. {self.nguoi_dung.get_full_name()} - {self.chuyen_khoa}"

class DanhGiaBacSi(models.Model):
    """Đánh giá bác sĩ từ bệnh nhân"""
    bac_si = models.ForeignKey(HoSoBacSi, on_delete=models.CASCADE, related_name='danh_gia')
    benh_nhan = models.ForeignKey(HoSoBenhNhan, on_delete=models.CASCADE, related_name='danh_gia_da_cho')
    diem_so = models.IntegerField(choices=[(i, f"{i} sao") for i in range(1, 6)], verbose_name="Điểm số")
    nhan_xet = models.TextField(blank=True, verbose_name="Nhận xét")
    ngay_danh_gia = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đánh giá")
    
    class Meta:
        verbose_name = "Đánh giá bác sĩ"
        verbose_name_plural = "Đánh giá bác sĩ"
        unique_together = ['bac_si', 'benh_nhan']  # Mỗi bệnh nhân chỉ đánh giá 1 lần
    
    def __str__(self):
        return f"{self.benh_nhan} đánh giá {self.bac_si} - {self.diem_so} sao"