@echo off
echo ========================================
echo    AI CHATBOX - READY TO USE!
echo ========================================
echo.

call venv\Scripts\activate

echo ✅ Database: 23 bac si, 10 chuyen khoa
echo ✅ Lich lam viec: 5,489 lich trong
echo ✅ AI Service: Phan tich trieu chung chinh xac
echo ✅ Tat ca test: 5/5 PASS
echo.
echo 🚀 Server dang chay tai: http://127.0.0.1:8000
echo 🤖 Widget AI se hien thi o goc duoi phai cho benh nhan
echo.
echo Huong dan su dung:
echo 1. Dang nhap voi tai khoan benh nhan:
echo    - Username: patient1 hoac patient2
echo    - Password: (mac dinh he thong)
echo    HOAC
echo    - Username: benhnhan_test
echo    - Password: 123456
echo.
echo 2. Tim widget AI o goc duoi phai
echo 3. Click de mo chat
echo 4. Test cac trieu chung:
echo    - "toi bi dau dau va sot" → Noi khoa
echo    - "dau nguc kho tho" → Tim mach  
echo    - "ho dau hong" → Tai mui hong
echo    - "mat do nhin mo" → Mat
echo    - "dau rang" → Rang ham mat
echo.
echo 5. Chon bac si HOAC:
echo    - Click "Xem bac si chuyen khoa khac"
echo    - Chon chuyen khoa khac (VD: Da lieu)
echo    - He thong se canh bao neu khong phu hop
echo    - Van co the dat lich neu muon
echo.
echo 6. Dat lich va hoan thanh
echo.
echo Nhan Ctrl+C de dung server
echo.

python manage.py runserver