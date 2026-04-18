from django.contrib import admin
from .models import HoSoBenhAn

@admin.register(HoSoBenhAn)
class HoSoBenhAnAdmin(admin.ModelAdmin):
    list_display = ['lich_hen', 'chan_doan', 'ngay_tao']
    search_fields = ['lich_hen__benh_nhan__nguoi_dung__first_name', 'lich_hen__benh_nhan__nguoi_dung__last_name', 'chan_doan']
    list_filter = ['ngay_tao']
