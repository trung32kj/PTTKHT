from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import ChatSession, ChatMessage, TrieuChungAnalysis
from accounts.models import ChuyenKhoa, HoSoBacSi, HoSoBenhNhan


class AIChatboxTestCase(TestCase):
    def setUp(self):
        # Tạo user test
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        
        # Tạo chuyên khoa test
        self.chuyen_khoa = ChuyenKhoa.objects.create(
            ten='Nội khoa',
            mo_ta='Chuyên khoa nội'
        )
    
    def test_chat_interface_requires_login(self):
        """Test chat interface yêu cầu đăng nhập"""
        response = self.client.get(reverse('ai_chatbox:chat_interface'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_start_chat_authenticated(self):
        """Test khởi tạo chat khi đã đăng nhập"""
        self.client.login(username='testuser', password='testpass123')
        
        response = self.client.post(
            reverse('ai_chatbox:chat_api'),
            data={'action': 'start_chat'},
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('session_id', data)
        self.assertIn('message', data)