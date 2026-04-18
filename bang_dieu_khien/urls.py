from django.urls import path
from . import views

urlpatterns = [
    path('', views.bang_dieu_khien, name='bang_dieu_khien'),
]
