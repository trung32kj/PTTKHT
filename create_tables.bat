@echo off
echo Tao bang database cho AI Chatbox...
echo.

call venv\Scripts\activate

echo Tao migrations...
python manage.py makemigrations ai_chatbox
python manage.py makemigrations accounts

echo Chay migrations...
python manage.py migrate

echo.
echo Kiem tra bang da tao...
python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic_management.settings'); django.setup(); from ai_chatbox.models import ChatSession; print('✅ Bang ChatSession da tao thanh cong!')"

echo.
echo ✅ HOAN THANH! Ban co the chay server bay gio.
pause