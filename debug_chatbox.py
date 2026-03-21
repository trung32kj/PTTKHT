#!/usr/bin/env python
"""
Debug AI Chatbox - Kiểm tra lỗi gửi tin nhắn
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse
import json

def test_api_endpoints():
    """Test các API endpoints"""
    print("=== DEBUG API ENDPOINTS ===")
    
    # Tạo test client
    client = Client()
    
    # Tạo user test
    user, created = User.objects.get_or_create(
        username='test_debug_user',
        defaults={'email': 'debug@test.com'}
    )
    
    # Login
    client.force_login(user)
    print("✅ User logged in")
    
    # Test start_chat
    response = client.post(
        reverse('ai_chatbox:chat_api'),
        data=json.dumps({'action': 'start_chat'}),
        content_type='application/json'
    )
    
    print(f"Start chat response: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Session ID: {data.get('session_id')}")
        session_id = data.get('session_id')
        
        # Test send_message
        response = client.post(
            reverse('ai_chatbox:chat_api'),
            data=json.dumps({
                'action': 'send_message',
                'session_id': session_id,
                'message': 'tôi bị đau đầu'
            }),
            content_type='application/json'
        )
        
        print(f"Send message response: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("✅ Message sent successfully")
            print(f"AI response: {data.get('ai_message', {}).get('content', '')[:100]}...")
        else:
            print(f"❌ Send message failed: {response.content}")
    else:
        print(f"❌ Start chat failed: {response.content}")
    
    # Cleanup
    if created:
        user.delete()

def check_csrf_settings():
    """Kiểm tra CSRF settings"""
    print("\n=== CHECK CSRF SETTINGS ===")
    
    from django.conf import settings
    
    print(f"CSRF_COOKIE_SECURE: {getattr(settings, 'CSRF_COOKIE_SECURE', 'Not set')}")
    print(f"CSRF_COOKIE_HTTPONLY: {getattr(settings, 'CSRF_COOKIE_HTTPONLY', 'Not set')}")
    print(f"CSRF_TRUSTED_ORIGINS: {getattr(settings, 'CSRF_TRUSTED_ORIGINS', 'Not set')}")

def check_models():
    """Kiểm tra models có hoạt động không"""
    print("\n=== CHECK MODELS ===")
    
    try:
        from ai_chatbox.models import ChatSession
        from django.contrib.auth.models import User
        
        # Test tạo session
        user, created = User.objects.get_or_create(
            username='model_test_user',
            defaults={'email': 'model@test.com'}
        )
        
        session = ChatSession.objects.create(
            benh_nhan=user,
            session_id='debug_session_123'
        )
        
        print("✅ Models working correctly")
        
        # Cleanup
        session.delete()
        if created:
            user.delete()
            
    except Exception as e:
        print(f"❌ Models error: {e}")

def main():
    print("🔍 DEBUG AI CHATBOX")
    print("=" * 40)
    
    check_csrf_settings()
    check_models()
    test_api_endpoints()
    
    print("\n" + "=" * 40)
    print("Debug completed!")

if __name__ == '__main__':
    main()