from django.urls import path
from . import views

urlpatterns = [
    path('tao-ho-so/<int:lich_hen_id>/', views.tao_ho_so_benh_an, name='tao_ho_so_benh_an'),
    path('lich-su-kham/', views.lich_su_kham_benh, name='lich_su_kham_benh'),
    path('xem-ho-so/<int:ho_so_id>/', views.xem_ho_so_benh_an, name='xem_ho_so_benh_an'),
]
