import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
sys.path.append('.')

try:
    django.setup()
    print("✅ Django setup OK")
    
    # Test imports
    from ai_chatbox.models import ChatSession, ChatMessage
    print("✅ AI Chatbox models import OK")
    
    from ai_chatbox.services import OpenAIService, DoctorRecommendationService
    print("✅ AI Chatbox services import OK")
    
    from ai_chatbox.views import ChatAPIView
    print("✅ AI Chatbox views import OK")
    
    # Test AI service
    ai_service = OpenAIService()
    result = ai_service.analyze_symptoms("đau đầu sốt")
    print(f"✅ AI Service test OK - Chuyên khoa: {result['chuyen_khoa_de_xuat']}")
    
    print("\n🎉 TẤT CẢ TEST PASS!")
    print("✅ AI Chatbox sẵn sàng hoạt động!")
    
except Exception as e:
    print(f"❌ Lỗi: {e}")
    import traceback
    traceback.print_exc()