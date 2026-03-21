from django.urls import path
from . import views

urlpatterns = [
    path('danh-sach-bac-si/', views.danh_sach_bac_si, name='danh_sach_bac_si'),
    path('bac-si/<int:bac_si_id>/lich-lam-viec/', views.lich_lam_viec_bac_si, name='lich_lam_viec_bac_si'),
    path('dat-lich/<int:lich_lam_viec_id>/', views.dat_lich_kham, name='dat_lich_kham'),
    path('lich-hen-cua-toi/', views.lich_hen_cua_toi, name='lich_hen_cua_toi'),
    path('huy-lich/<int:lich_hen_id>/', views.huy_lich_hen, name='huy_lich_hen'),
    path('xac-nhan-lich/<int:lich_hen_id>/', views.xac_nhan_lich_hen, name='xac_nhan_lich_hen'),
    # URLs cho bác sĩ
    path('dang-ky-lich-lam-viec/', views.dang_ky_lich_lam_viec, name='dang_ky_lich_lam_viec'),
    path('lich-lam-viec-cua-toi/', views.lich_lam_viec_cua_toi, name='lich_lam_viec_cua_toi'),
]
