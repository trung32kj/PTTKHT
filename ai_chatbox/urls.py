from django.urls import path
from . import views

app_name = 'ai_chatbox'

urlpatterns = [
    path('', views.chat_interface, name='chat_interface'),
    path('api/', views.ChatAPIView.as_view(), name='chat_api'),
]