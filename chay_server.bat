@echo off
echo ========================================
echo   KHOI DONG SERVER DJANGO
echo ========================================
echo.

echo [1/2] Kich hoat moi truong ao...
call venv\Scripts\activate.bat

echo.
echo [2/2] Khoi dong Django server...
echo.
echo Server dang chay tai: http://127.0.0.1:8000
echo Nhan Ctrl+C de dung server
echo.
python manage.py runserver

pause
