from django.db import models
from accounts.models import HoSoBacSi, HoSoBenhNhan

class LichLamViec(models.Model):
    bac_si = models.ForeignKey(HoSoBacSi, on_delete=models.CASCADE, related_name='lich_lam_viec', verbose_name="Bác sĩ")
    ngay = models.DateField(verbose_name="Ngày")
    gio_bat_dau = models.TimeField(verbose_name="Giờ bắt đầu")
    gio_ket_thuc = models.TimeField(verbose_name="Giờ kết thúc")
    con_trong = models.BooleanField(default=True, verbose_name="Còn trống")
    
    class Meta:
        verbose_name = "Lịch làm việc"
        verbose_name_plural = "Lịch làm việc"
        unique_together = ['bac_si', 'ngay', 'gio_bat_dau']
    
    def __str__(self):
        return f"{self.bac_si} - {self.ngay} {self.gio_bat_dau}-{self.gio_ket_thuc}"

class LichHen(models.Model):
    TRANG_THAI_CHOICES = [
        ('pending', 'Chờ xác nhận'),
        ('approved', 'Đã xác nhận'),
        ('canceled', 'Đã hủy'),
        ('completed', 'Hoàn thành'),
    ]
    
    benh_nhan = models.ForeignKey(HoSoBenhNhan, on_delete=models.CASCADE, related_name='lich_hen', verbose_name="Bệnh nhân")
    bac_si = models.ForeignKey(HoSoBacSi, on_delete=models.CASCADE, related_name='lich_hen', verbose_name="Bác sĩ")
    lich_lam_viec = models.ForeignKey(LichLamViec, on_delete=models.CASCADE, related_name='lich_hen', verbose_name="Lịch")
    ngay = models.DateField(verbose_name="Ngày khám")
    gio = models.TimeField(verbose_name="Giờ khám")
    trang_thai = models.CharField(max_length=20, choices=TRANG_THAI_CHOICES, default='pending', verbose_name="Trạng thái")
    trieu_chung = models.TextField(blank=True, verbose_name="Triệu chứng")
    ngay_tao = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    ngay_cap_nhat = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")
    
    class Meta:
        verbose_name = "Lịch hẹn"
        verbose_name_plural = "Lịch hẹn"
        ordering = ['-ngay', '-gio']
    
    def __str__(self):
        return f"{self.benh_nhan.nguoi_dung.get_full_name()} - {self.bac_si.nguoi_dung.get_full_name()} - {self.ngay} {self.gio}"
