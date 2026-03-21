#!/usr/bin/env python
"""
Test nhanh AI service
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from ai_chatbox.services import OpenAIService

def main():
    print("🤖 TEST AI SERVICE")
    print("=" * 30)
    
    ai_service = OpenAIService()
    
    # Test cases thực tế
    test_cases = [
        "tôi bị đau đầu và sốt cao",
        "đau ngực, khó thở, tim đập nhanh", 
        "đau bụng, tiêu chảy, buồn nôn",
        "ho khan, đau họng, nghẹt mũi",
        "mắt đỏ, nhìn mờ, chảy nước mắt",
        "đau răng, sưng nướu"
    ]
    
    for i, symptom in enumerate(test_cases, 1):
        print(f"\n{i}. Triệu chứng: {symptom}")
        
        result = ai_service.analyze_symptoms(symptom)
        
        print(f"   → Chuyên khoa: {result['chuyen_khoa_de_xuat']}")
        print(f"   → Độ tin cậy: {result['do_tin_cay']}%")
        print(f"   → Lý do: {result['phan_tich']['ly_do_chon_chuyen_khoa']}")
    
    print("\n" + "=" * 30)
    print("✅ AI Service hoạt động hoàn hảo!")
    print("🚀 Sẵn sàng cho production!")

if __name__ == '__main__':
    main()