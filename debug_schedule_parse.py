"""
Debug parse_schedule_request
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from ai_chatbox.views import ChatAPIView
from ai_chatbox.models import ChatSession, ChatMessage
from accounts.models import HoSoBenhNhan
from django.contrib.auth.models import User

# Tạo test session
user = HoSoBenhNhan.objects.first().nguoi_dung
session = ChatSession.objects.create(
    benh_nhan=user,
    session_id='test-debug-123'
)

# Tạo tin nhắn AI với warning
ChatMessage.objects.create(
    chat_session=session,
    nguoi_gui='ai',
    noi_dung='Cảnh báo test',
    metadata={'warning': True, 'doctor_id': 1}
)

view = ChatAPIView()

messages = [
    'tôi muốn hiện thời gian rảnh của bác sĩ để đặt lịch',
    'xem lịch trống',
    'hiển thị lịch rảnh',
    'đặt lịch luôn',
    'có lịch nào không'
]

print("=" * 60)
print("TEST PARSE SCHEDULE REQUEST")
print("=" * 60)

for msg in messages:
    result = view.parse_schedule_request(msg, session)
    status = "✅" if result else "❌"
    print(f"{status} '{msg}' → {result}")

# Cleanup
session.delete()
