@echo off
echo ========================================
echo    SETUP VA TEST AI CHATBOX
echo ========================================
echo.

echo [1/5] Kich hoat virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo ❌ Loi kich hoat venv
    pause
    exit /b 1
)

echo [2/5] Tao migrations...
python manage.py makemigrations
python manage.py makemigrations accounts
python manage.py makemigrations ai_chatbox

echo [3/5] Chay migrations...
python manage.py migrate
if errorlevel 1 (
    echo ❌ Loi chay migrations
    pause
    exit /b 1
)

echo [4/5] Test debug...
python debug_chatbox.py
if errorlevel 1 (
    echo ❌ Debug test failed
    pause
    exit /b 1
)

echo [5/5] Test template...
python test_template.py

echo.
echo ✅ SETUP VA TEST HOAN THANH!
echo.
echo De chay server:
echo   python manage.py runserver
echo.
echo Widget AI se hien thi o goc duoi phai cho benh nhan
echo.
pause