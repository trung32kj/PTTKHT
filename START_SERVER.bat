@echo off
cls
echo ========================================
echo    AI CHATBOX - PHONG KHAM
echo ========================================
echo.
echo Dang khoi dong server...
echo.

call venv\Scripts\activate

echo ========================================
echo    HE THONG SAN SANG!
echo ========================================
echo.
echo ✅ Database: 23 bac si, 10 chuyen khoa
echo ✅ Lich lam viec: 5,489 lich trong
echo ✅ AI Service: Hoat dong (Fallback mode)
echo ✅ OpenAI: Da cai dat (can API key de bat)
echo.
echo 🌐 Server: http://127.0.0.1:8000
echo 🤖 Widget AI: Goc duoi phai (cho benh nhan)
echo.
echo ========================================
echo    TAI KHOAN TEST
echo ========================================
echo.
echo BENH NHAN:
echo   Username: patient1 hoac patient2
echo   Password: (mac dinh he thong)
echo   HOAC
echo   Username: benhnhan_test
echo   Password: 123456
echo.
echo BAC SI:
echo   Username: bs001 den bs020
echo   Password: 123456
echo.
echo ========================================
echo    HUONG DAN SU DUNG
echo ========================================
echo.
echo 1. Dang nhap voi tai khoan benh nhan
echo 2. Tim widget AI o goc duoi phai
echo 3. Click icon robot de mo chat
echo 4. Nhap trieu chung:
echo    - "toi bi dau dau va sot"
echo    - "dau nguc kho tho"
echo    - "ho dau hong"
echo 5. Chon bac si HOAC nhap ten bac si:
echo    - "muon dat BS. Anh Le Thi Ngoc"
echo 6. Xac nhan va dat lich
echo.
echo ========================================
echo    BAT CHATGPT (TUY CHON)
echo ========================================
echo.
echo Neu muon dung ChatGPT that:
echo 1. Lay API key tu: https://platform.openai.com
echo 2. Mo file: clinic_management/settings.py
echo 3. Sua dong: OPENAI_API_KEY = 'sk-your-key'
echo 4. Khoi dong lai server
echo.
echo Chi tiet xem file: OPENAI_SETUP.txt
echo.
echo ========================================
echo.
echo Nhan Ctrl+C de dung server
echo.

python manage.py runserver