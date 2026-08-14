from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bang_dieu_khien.urls')),
    path('accounts/', include('tai_khoan.urls')),
    path('appointments/', include('lich_hen.urls')),
    path('medical-records/', include('ho_so_benh_an.urls')),
    path('ai-chatbox/', include('hop_thoai_ai.urls')),
]

# File upload (ảnh đại diện, tài liệu) được phục vụ bởi Django vì Render/WhiteNoise
# chỉ phục vụ static files thu thập lúc build, không thấy file người dùng tải lên.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

handler404 = 'bang_dieu_khien.views.custom_404'
handler500 = 'bang_dieu_khien.views.custom_500'
