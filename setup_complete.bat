@echo off
echo ========================================
echo    SETUP COMPLETE AI CHATBOX
echo ========================================
echo.

echo [1/4] Kich hoat virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo ❌ Loi kich hoat venv
    pause
    exit /b 1
)

echo [2/4] Tao va chay migrations...
python manage.py makemigrations
python manage.py makemigrations accounts  
python manage.py makemigrations ai_chatbox
python manage.py migrate
if errorlevel 1 (
    echo ❌ Loi migrations
    pause
    exit /b 1
)

echo [3/4] Chay final test...
python final_test.py
if errorlevel 1 (
    echo ❌ Final test failed
    pause
    exit /b 1
)

echo [4/4] Tao superuser (optional)...
echo Nhan Enter de bo qua tao superuser
python manage.py createsuperuser --noinput --username admin --email admin@test.com 2>nul

echo.
echo ✅ SETUP HOAN THANH THANH CONG!
echo.
echo ===========================================
echo    AI CHATBOX DA SAN SANG HOAT DONG!
echo ===========================================
echo.
echo De chay server:
echo   python manage.py runserver
echo.
echo Sau do:
echo 1. Truy cap: http://127.0.0.1:8000
echo 2. Dang ky tai khoan benh nhan
echo 3. Tim widget AI o goc duoi phai
echo 4. Test chat: "toi bi dau dau va sot"
echo.
pause