from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bang_dieu_khien.urls')),
    path('accounts/', include('tai_khoan.urls')),
    path('appointments/', include('lich_hen.urls')),
    path('medical-records/', include('ho_so_benh_an.urls')),
    path('ai-chatbox/', include('hop_thoai_ai.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'bang_dieu_khien.views.custom_404'
handler500 = 'bang_dieu_khien.views.custom_500'
