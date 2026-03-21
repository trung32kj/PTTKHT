@echo off
echo ========================================
echo    KHOI CHAY AI CHATBOX SERVER
echo ========================================
echo.

echo Kich hoat virtual environment...
call venv\Scripts\activate

echo Khoi dong Django server...
echo.
echo ✅ Server dang chay tai: http://127.0.0.1:8000
echo ✅ Widget AI se hien thi cho benh nhan o goc duoi phai
echo.
echo Nhan Ctrl+C de dung server
echo.

python manage.py runserver