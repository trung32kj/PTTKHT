import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from django.urls import reverse, resolve
from django.test import RequestFactory
from django.contrib.auth.models import User

try:
    # Test URL patterns
    chat_url = reverse('ai_chatbox:chat_interface')
    print(f"✅ Chat interface URL: {chat_url}")
    
    api_url = reverse('ai_chatbox:chat_api')
    print(f"✅ Chat API URL: {api_url}")
    
    # Test URL resolution
    resolver = resolve('/ai-chatbox/')
    print(f"✅ URL resolver OK: {resolver.view_name}")
    
    resolver = resolve('/ai-chatbox/api/')
    print(f"✅ API resolver OK: {resolver.view_name}")
    
    print("✅ All URL patterns working correctly!")
    
except Exception as e:
    print(f"❌ URL error: {e}")
    import traceback
    traceback.print_exc()