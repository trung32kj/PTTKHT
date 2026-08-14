from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.bang_dieu_khien, name='bang_dieu_khien'),
    path('import-data/', views.import_data, name='import_data'),
]
