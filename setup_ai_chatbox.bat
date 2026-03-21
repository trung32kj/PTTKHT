@echo off
echo ========================================
echo    SETUP AI CHATBOX - PHONG KHAM
echo ========================================
echo.

echo [1/5] Kich hoat virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo ❌ Loi kich hoat venv. Vui long tao venv truoc:
    echo python -m venv venv
    pause
    exit /b 1
)

echo [2/5] Cai dat dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Loi cai dat packages
    pause
    exit /b 1
)

echo [3/5] Tao migrations...
python manage.py makemigrations
python manage.py makemigrations accounts
python manage.py makemigrations ai_chatbox
if errorlevel 1 (
    echo ❌ Loi tao migrations
    pause
    exit /b 1
)

echo [4/5] Chay migrations...
python manage.py migrate
if errorlevel 1 (
    echo ❌ Loi chay migrations
    pause
    exit /b 1
)

echo [5/5] Test AI Chatbox...
python test_ai_chatbox.py
if errorlevel 1 (
    echo ❌ Loi test system
    pause
    exit /b 1
)

echo.
echo ✅ SETUP HOAN THANH!
echo.
echo De chay server:
echo python manage.py runserver
echo.
echo Sau do truy cap: http://127.0.0.1:8000
echo Widget AI se hien thi o goc duoi phai cho benh nhan
echo.
pause