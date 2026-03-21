from django.db import models
from appointments.models import LichHen

class Thuoc(models.Model):
    ten_thuoc = models.CharField(max_length=200, verbose_name="Tên thuốc")
    don_vi = models.CharField(max_length=50, default="viên", verbose_name="Đơn vị")
    
    class Meta:
        verbose_name = "Thuốc"
        verbose_name_plural = "Thuốc"
    
    def __str__(self):
        return f"{self.ten_thuoc} ({self.don_vi})"

class HoSoBenhAn(models.Model):
    lich_hen = models.OneToOneField(LichHen, on_delete=models.CASCADE, related_name='ho_so_benh_an', verbose_name="Lịch hẹn")
    chan_doan = models.TextField(verbose_name="Chẩn đoán")
    ghi_chu = models.TextField(blank=True, verbose_name="Ghi chú")
    ngay_tao = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    ngay_cap_nhat = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")
    
    class Meta:
        verbose_name = "Hồ sơ bệnh án"
        verbose_name_plural = "Hồ sơ bệnh án"
        ordering = ['-ngay_tao']
    
    def __str__(self):
        return f"Hồ sơ - {self.lich_hen.benh_nhan.nguoi_dung.get_full_name()} - {self.lich_hen.ngay}"

class ToaThuoc(models.Model):
    ho_so_benh_an = models.ForeignKey(HoSoBenhAn, on_delete=models.CASCADE, related_name='toa_thuoc', verbose_name="Hồ sơ bệnh án")
    thuoc = models.ForeignKey(Thuoc, on_delete=models.CASCADE, verbose_name="Thuốc")
    so_luong = models.PositiveIntegerField(verbose_name="Số lượng")
    ghi_chu = models.CharField(max_length=500, blank=True, verbose_name="Ghi chú")
    
    class Meta:
        verbose_name = "Toa thuốc"
        verbose_name_plural = "Toa thuốc"
    
    def __str__(self):
        return f"{self.thuoc.ten_thuoc} - {self.so_luong} {self.thuoc.don_vi}"
