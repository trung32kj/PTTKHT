from django.contrib import admin
from .models import LichLamViec, LichHen, ThongBao

@admin.register(LichLamViec)
class LichLamViecAdmin(admin.ModelAdmin):
    list_display = ['bac_si', 'ngay', 'gio_bat_dau', 'gio_ket_thuc', 'con_trong']
    list_filter = ['ngay', 'con_trong', 'bac_si']
    search_fields = ['bac_si__nguoi_dung__first_name', 'bac_si__nguoi_dung__last_name']

@admin.register(LichHen)
class LichHenAdmin(admin.ModelAdmin):
    list_display = ['benh_nhan', 'bac_si', 'ngay', 'gio', 'trang_thai', 'ngay_tao']
    list_filter = ['trang_thai', 'ngay', 'bac_si']
    search_fields = ['benh_nhan__nguoi_dung__first_name', 'benh_nhan__nguoi_dung__last_name', 'bac_si__nguoi_dung__first_name']
    actions = ['xac_nhan_lich_hen', 'huy_lich_hen']
    
    def xac_nhan_lich_hen(self, request, queryset):
        queryset.update(trang_thai='approved')
    xac_nhan_lich_hen.short_description = "Xác nhận lịch hẹn"
    
    def huy_lich_hen(self, request, queryset):
        queryset.update(trang_thai='canceled')
    huy_lich_hen.short_description = "Hủy lịch hẹn"


@admin.register(ThongBao)
class ThongBaoAdmin(admin.ModelAdmin):
    list_display = ['tieu_de', 'nguoi_nhan', 'loai', 'da_doc', 'ngay_tao']
    list_filter = ['loai', 'da_doc', 'ngay_tao']
    search_fields = ['tieu_de', 'noi_dung', 'nguoi_nhan__username']
    actions = ['danh_dau_da_doc']
    
    def danh_dau_da_doc(self, request, queryset):
        queryset.update(da_doc=True)
    danh_dau_da_doc.short_description = "Đánh dấu đã đọc"
