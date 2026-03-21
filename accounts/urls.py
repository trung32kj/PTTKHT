from django.urls import path
from . import views

urlpatterns = [
    path('dang-ky/', views.dang_ky_benh_nhan, name='dang_ky'),
    path('dang-nhap/', views.dang_nhap, name='dang_nhap'),
    path('dang-xuat/', views.dang_xuat, name='dang_xuat'),
    path('ho-so/', views.ho_so, name='ho_so'),
    path('chinh-sua-ho-so/', views.chinh_sua_ho_so, name='chinh_sua_ho_so'),
    path('quan-ly-bac-si/', views.quan_ly_bac_si, name='quan_ly_bac_si'),
]
