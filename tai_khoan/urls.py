from django.urls import path
from . import views

urlpatterns = [
    path('dang-ky/', views.dang_ky_benh_nhan, name='dang_ky'),
    path('dang-nhap/', views.dang_nhap, name='dang_nhap'),
    path('dang-xuat/', views.dang_xuat, name='dang_xuat'),
    path('ho-so/', views.ho_so, name='ho_so'),
    path('chinh-sua-ho-so/', views.chinh_sua_ho_so, name='chinh_sua_ho_so'),
    path('quan-ly-bac-si/', views.quan_ly_bac_si, name='quan_ly_bac_si'),
    path('quen-mat-khau/', views.quen_mat_khau, name='quen_mat_khau'),
    path('doi-mat-khau/', views.doi_mat_khau, name='doi_mat_khau'),
    path('danh-gia-bac-si/<int:bac_si_id>/', views.danh_gia_bac_si, name='danh_gia_bac_si'),
]
