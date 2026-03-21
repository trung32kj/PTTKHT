from django.contrib import admin
from django.contrib.auth.models import User
from .models import ChuyenKhoa, HoSoBenhNhan, HoSoBacSi

@admin.register(ChuyenKhoa)
class ChuyenKhoaAdmin(admin.ModelAdmin):
    list_display = ['ten', 'mo_ta']
    search_fields = ['ten']

@admin.register(HoSoBacSi)
class HoSoBacSiAdmin(admin.ModelAdmin):
    list_display = ['nguoi_dung', 'chuyen_khoa', 'so_dien_thoai', 'phi_kham', 'anh_dai_dien']
    search_fields = ['nguoi_dung__username', 'nguoi_dung__first_name', 'nguoi_dung__last_name', 'so_dien_thoai']
    list_filter = ['chuyen_khoa']
    fields = ['nguoi_dung', 'chuyen_khoa', 'mo_ta', 'bang_cap', 'so_dien_thoai', 'phi_kham', 'anh_dai_dien']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change and obj.nguoi_dung:
            obj.nguoi_dung.is_staff = True
            obj.nguoi_dung.save()
