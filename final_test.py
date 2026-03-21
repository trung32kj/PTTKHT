#!/usr/bin/env python
"""
FINAL TEST - AI CHATBOX SYSTEM
Kiểm tra toàn bộ hệ thống trước khi deploy
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

def test_imports():
    """Test tất cả imports"""
    print("=== TEST IMPORTS ===")
    
    try:
        from ai_chatbox.models import ChatSession, ChatMessage, TrieuChungAnalysis, BacSiRecommendation
        print("✅ Models import OK")
        
        from ai_chatbox.views import ChatAPIView, chat_interface
        print("✅ Views import OK")
        
        from ai_chatbox.services import OpenAIService, DoctorRecommendationService, AppointmentService
        print("✅ Services import OK")
        
        from ai_chatbox.admin import ChatSessionAdmin
        print("✅ Admin import OK")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_services():
    """Test services functionality"""
    print("\n=== TEST SERVICES ===")
    
    try:
        # Test AI Service
        from ai_chatbox.services import OpenAIService
        ai_service = OpenAIService()
        
        test_cases = [
            "đau đầu sốt",
            "đau ngực khó thở", 
            "đau bụng tiêu chảy",
            "ho đau họng"
        ]
        
        for symptom in test_cases:
            result = ai_service.analyze_symptoms(symptom)
            assert 'chuyen_khoa_de_xuat' in result
            assert 'do_tin_cay' in result
            assert result['do_tin_cay'] > 0
            print(f"✅ AI analysis: {symptom} → {result['chuyen_khoa_de_xuat']}")
        
        # Test Doctor Service
        from ai_chatbox.services import DoctorRecommendationService
        from accounts.models import ChuyenKhoa
        
        # Tạo chuyên khoa test nếu chưa có
        chuyen_khoa, created = ChuyenKhoa.objects.get_or_create(
            ten='Nội khoa',
            defaults={'mo_ta': 'Test specialty'}
        )
        
        recommendations = DoctorRecommendationService.get_top_doctors('Nội khoa', limit=3)
        print(f"✅ Doctor recommendations: {len(recommendations)} doctors found")
        
        return True
    except Exception as e:
        print(f"❌ Services error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_urls():
    """Test URL patterns"""
    print("\n=== TEST URLS ===")
    
    try:
        from django.urls import reverse
        
        chat_url = reverse('ai_chatbox:chat_interface')
        api_url = reverse('ai_chatbox:chat_api')
        
        assert chat_url == '/ai-chatbox/'
        assert api_url == '/ai-chatbox/api/'
        
        print("✅ URL patterns OK")
        return True
    except Exception as e:
        print(f"❌ URL error: {e}")
        return False

def test_templates():
    """Test template syntax"""
    print("\n=== TEST TEMPLATES ===")
    
    try:
        from django.template import Template, Context
        
        # Test widget template
        with open('templates/ai_chatbox/widget.html', 'r', encoding='utf-8') as f:
            template = Template(f.read())
            template.render(Context({}))
        print("✅ Widget template OK")
        
        # Test chat template  
        with open('templates/ai_chatbox/chat.html', 'r', encoding='utf-8') as f:
            template = Template(f.read())
            template.render(Context({}))
        print("✅ Chat template OK")
        
        return True
    except Exception as e:
        print(f"❌ Template error: {e}")
        return False

def test_models():
    """Test model creation"""
    print("\n=== TEST MODELS ===")
    
    try:
        from django.contrib.auth.models import User
        from ai_chatbox.models import ChatSession
        
        # Test tạo user và session
        user, created = User.objects.get_or_create(
            username='test_ai_user',
            defaults={'email': 'test@ai.com'}
        )
        
        session = ChatSession.objects.create(
            benh_nhan=user,
            session_id='test_session_final'
        )
        
        assert session.trang_thai == 'active'
        print("✅ Models creation OK")
        
        # Cleanup
        session.delete()
        if created:
            user.delete()
            
        return True
    except Exception as e:
        print(f"❌ Models error: {e}")
        return False

def main():
    """Chạy tất cả tests"""
    print("🚀 FINAL TEST - AI CHATBOX SYSTEM")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_services, 
        test_urls,
        test_templates,
        test_models
    ]
    
    passed = 0
    total = len(tests)
    
    for test_func in tests:
        if test_func():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED!")
        print("✅ AI Chatbox system is ready to deploy!")
        print("\nNext steps:")
        print("1. Run: python manage.py runserver")
        print("2. Login as patient user")
        print("3. Look for AI widget at bottom-right corner")
        print("4. Test the chat functionality")
    else:
        print("❌ Some tests failed. Please fix issues before deploying.")
        return False
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)