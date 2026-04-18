from django.contrib import admin
from .models import ChatSession, ChatMessage, TrieuChungAnalysis, BacSiRecommendation


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'benh_nhan', 'trang_thai', 'ngay_tao']
    list_filter = ['trang_thai', 'ngay_tao']
    search_fields = ['session_id', 'benh_nhan__username']
    readonly_fields = ['session_id', 'ngay_tao']


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['chat_session', 'nguoi_gui', 'noi_dung_short', 'thoi_gian']
    list_filter = ['nguoi_gui', 'thoi_gian']
    search_fields = ['noi_dung', 'chat_session__session_id']
    readonly_fields = ['thoi_gian']
    
    def noi_dung_short(self, obj):
        return obj.noi_dung[:50] + "..." if len(obj.noi_dung) > 50 else obj.noi_dung
    noi_dung_short.short_description = "Nội dung"


@admin.register(TrieuChungAnalysis)
class TrieuChungAnalysisAdmin(admin.ModelAdmin):
    list_display = ['chat_session', 'chuyen_khoa_de_xuat', 'do_tin_cay', 'ngay_phan_tich']
    list_filter = ['chuyen_khoa_de_xuat', 'ngay_phan_tich']
    search_fields = ['trieu_chung_goc']
    readonly_fields = ['ngay_phan_tich']


@admin.register(BacSiRecommendation)
class BacSiRecommendationAdmin(admin.ModelAdmin):
    list_display = ['analysis', 'bac_si', 'thu_tu_uu_tien', 'rating_score']
    list_filter = ['bac_si__chuyen_khoa', 'thu_tu_uu_tien']
    search_fields = ['bac_si__nguoi_dung__username', 'ly_do_goi_y']