import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings')
django.setup()

from appointments.models import LichLamViec
from accounts.models import HoSoBacSi
from datetime import datetime, timedelta, time

doctor = HoSoBacSi.objects.get(id=1)
today = datetime.now().date()

print(f"Tạo lịch cho BS. {doctor.nguoi_dung.get_full_name()}")

for i in range(7):
    day = today + timedelta(days=i)
    slot, created = LichLamViec.objects.get_or_create(
        bac_si=doctor,
        ngay=day,
        gio_bat_dau=time(8, 0),
        gio_ket_thuc=time(9, 0),
        defaults={'con_trong': True}
    )
    if created:
        print(f"✅ Created slot for {day}")
    else:
        print(f"⚠️ Slot already exists for {day}")

print(f"\nTổng lịch trống: {LichLamViec.objects.filter(bac_si=doctor, con_trong=True, ngay__gte=today).count()}")
