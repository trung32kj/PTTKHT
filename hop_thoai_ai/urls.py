from django.urls import path
from . import views

app_name = 'hop_thoai_ai'

urlpatterns = [
    path('', views.chat_interface, name='chat_interface'),
    path('api/', views.ChatAPIView.as_view(), name='chat_api'),
]