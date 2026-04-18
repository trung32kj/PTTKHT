-- =====================================================
-- SCRIPT TẠO DỮ LIỆU MẪU CHO HỆ THỐNG QUẢN LÝ PHÒNG KHÁM
-- Database: pttkht
-- =====================================================

USE pttkht;

-- Xóa dữ liệu cũ (nếu có)
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE accounts_danhgiabacsi;
TRUNCATE TABLE medical_records_toathuoc;
TRUNCATE TABLE medical_records_hosobenhan;
TRUNCATE TABLE appointments_lichhen;
TRUNCATE TABLE appointments_lichlamviec;
TRUNCATE TABLE accounts_hosobacsi;
TRUNCATE TABLE accounts_hosobenhnhan;
TRUNCATE TABLE accounts_chuyenkhoa;
TRUNCATE TABLE medical_records_thuoc;
TRUNCATE TABLE ai_chatbox_bacsirecommendation;
TRUNCATE TABLE ai_chatbox_trieuchunganalysis;
TRUNCATE TABLE ai_chatbox_chatmessage;
TRUNCATE TABLE ai_chatbox_chatsession;
DELETE FROM auth_user WHERE id > 0;
SET FOREIGN_KEY_CHECKS = 1;

-- =====================================================
-- 1. TẠO CHUYÊN KHOA
-- =====================================================
INSERT INTO accounts_chuyenkhoa (ten, mo_ta) VALUES
('Nội khoa', 'Khám và điều trị các bệnh nội khoa tổng quát'),
('Ngoại khoa', 'Phẫu thuật và điều trị ngoại khoa'),
('Da liễu', 'Điều trị các bệnh về da, tóc, móng'),
('Tim mạch', 'Chuyên khoa tim mạch và huyết áp'),
('Tai mũi họng', 'Điều trị các bệnh tai mũi họng'),
('Mắt', 'Chuyên khoa nhãn khoa'),
('Răng hàm mặt', 'Nha khoa và phẫu thuật hàm mặt'),
('Thần kinh', 'Chuyên khoa thần kinh'),
('Tiêu hóa', 'Bệnh tiêu hóa và gan mật'),
('Sản phụ khoa', 'Sản khoa và phụ khoa');

-- =====================================================
-- 2. TẠO TÀI KHOẢN ADMIN
-- =====================================================
INSERT INTO auth_user (username, first_name, last_name, email, is_staff, is_active, is_superuser, date_joined, password) VALUES
('admin', 'Admin', 'System', 'admin@phongkham.com', 1, 1, 1, NOW(), 'pbkdf2_sha256$600000$randomsalt$hashedpassword');

-- =====================================================
-- 3. TẠO TÀI KHOẢN BÁC SĨ
-- =====================================================
INSERT INTO auth_user (username, first_name, last_name, email, is_staff, is_active, date_joined, password) VALUES
('bs_nguyenvan', 'Nguyễn', 'Văn An', 'bs_nguyenvan@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_tranthi', 'Trần', 'Thị Bình', 'bs_tranthi@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_levan', 'Lê', 'Văn Cường', 'bs_levan@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_phamthi', 'Phạm', 'Thị Dung', 'bs_phamthi@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_hoangvan', 'Hoàng', 'Văn Em', 'bs_hoangvan@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_vuthi', 'Vũ', 'Thị Hoa', 'bs_vuthi@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_dangvan', 'Đặng', 'Văn Giang', 'bs_dangvan@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_buithi', 'Bùi', 'Thị Lan', 'bs_buithi@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_ngovan', 'Ngô', 'Văn Minh', 'bs_ngovan@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_lythi', 'Lý', 'Thị Nga', 'bs_lythi@phongkham.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456');

-- =====================================================
-- 4. TẠO HỒ SƠ BÁC SĨ
-- =====================================================
INSERT INTO accounts_hosobacsi (nguoi_dung_id, chuyen_khoa_id, bang_cap, so_dien_thoai, phi_kham, mo_ta) VALUES
((SELECT id FROM auth_user WHERE username='bs_nguyenvan'), 1, 'Tiến sĩ Y khoa', '0901234567', 200000, 'Bác sĩ Nội khoa với kinh nghiệm Tiến sĩ Y khoa'),
((SELECT id FROM auth_user WHERE username='bs_tranthi'), 4, 'Thạc sĩ Y khoa', '0901234568', 300000, 'Bác sĩ Tim mạch với kinh nghiệm Thạc sĩ Y khoa'),
((SELECT id FROM auth_user WHERE username='bs_levan'), 2, 'Bác sĩ chuyên khoa II', '0901234569', 250000, 'Bác sĩ Ngoại khoa với kinh nghiệm Bác sĩ chuyên khoa II'),
((SELECT id FROM auth_user WHERE username='bs_phamthi'), 3, 'Thạc sĩ Y khoa', '0901234570', 180000, 'Bác sĩ Da liễu với kinh nghiệm Thạc sĩ Y khoa'),
((SELECT id FROM auth_user WHERE username='bs_hoangvan'), 5, 'Bác sĩ chuyên khoa I', '0901234571', 220000, 'Bác sĩ Tai mũi họng với kinh nghiệm Bác sĩ chuyên khoa I'),
((SELECT id FROM auth_user WHERE username='bs_vuthi'), 6, 'Thạc sĩ Y khoa', '0901234572', 200000, 'Bác sĩ Mắt với kinh nghiệm Thạc sĩ Y khoa'),
((SELECT id FROM auth_user WHERE username='bs_dangvan'), 7, 'Bác sĩ nha khoa', '0901234573', 150000, 'Bác sĩ Răng hàm mặt với kinh nghiệm Bác sĩ nha khoa'),
((SELECT id FROM auth_user WHERE username='bs_buithi'), 8, 'Tiến sĩ Y khoa', '0901234574', 350000, 'Bác sĩ Thần kinh với kinh nghiệm Tiến sĩ Y khoa'),
((SELECT id FROM auth_user WHERE username='bs_ngovan'), 9, 'Bác sĩ chuyên khoa II', '0901234575', 280000, 'Bác sĩ Tiêu hóa với kinh nghiệm Bác sĩ chuyên khoa II'),
((SELECT id FROM auth_user WHERE username='bs_lythi'), 10, 'Thạc sĩ Y khoa', '0901234576', 250000, 'Bác sĩ Sản phụ khoa với kinh nghiệm Thạc sĩ Y khoa');

-- =====================================================
-- 5. TẠO TÀI KHOẢN BỆNH NHÂN
-- =====================================================
INSERT INTO auth_user (username, first_name, last_name, email, is_active, date_joined, password) VALUES
('bn_nguyenthi', 'Nguyễn', 'Thị Hoa', 'bn_nguyenthi@benhnhan.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_tranvan', 'Trần', 'Văn Nam', 'bn_tranvan@benhnhan.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_lethi', 'Lê', 'Thị Mai', 'bn_lethi@benhnhan.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_phamvan', 'Phạm', 'Văn Đức', 'bn_phamvan@benhnhan.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_hoangthi', 'Hoàng', 'Thị Linh', 'bn_hoangthi@benhnhan.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_vuvan', 'Vũ', 'Văn Tùng', 'bn_vuvan@benhnhan.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_dangthi', 'Đặng', 'Thị Yến', 'bn_dangthi@benhnhan.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_buivan', 'Bùi', 'Văn Khoa', 'bn_buivan@benhnhan.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456');

-- =====================================================
-- 6. TẠO HỒ SƠ BỆNH NHÂN
-- =====================================================
INSERT INTO accounts_hosobenhnhan (nguoi_dung_id, ngay_sinh, gioi_tinh, so_dien_thoai, dia_chi) VALUES
((SELECT id FROM auth_user WHERE username='bn_nguyenthi'), '1990-05-15', 'F', '0987654321', 'Số 10, Phố Huế, Hai Bà Trưng, Hà Nội'),
((SELECT id FROM auth_user WHERE username='bn_tranvan'), '1985-08-20', 'M', '0987654322', '123 Nguyễn Huệ, Quận 1, TP.HCM'),
((SELECT id FROM auth_user WHERE username='bn_lethi'), '1992-12-10', 'F', '0987654323', '45 Trần Phú, Hải Châu, Đà Nẵng'),
((SELECT id FROM auth_user WHERE username='bn_phamvan'), '1988-03-25', 'M', '0987654324', '67 Lê Lợi, Quận 1, TP.HCM'),
((SELECT id FROM auth_user WHERE username='bn_hoangthi'), '1995-07-08', 'F', '0987654325', '89 Điện Biên Phủ, Ba Đình, Hà Nội'),
((SELECT id FROM auth_user WHERE username='bn_vuvan'), '1987-11-30', 'M', '0987654326', '12 Ngô Quyền, Sơn Trà, Đà Nẵng'),
((SELECT id FROM auth_user WHERE username='bn_dangthi'), '1993-09-14', 'F', '0987654327', '34 Hai Bà Trưng, Quận 3, TP.HCM'),
((SELECT id FROM auth_user WHERE username='bn_buivan'), '1991-01-22', 'M', '0987654328', '56 Láng Hạ, Đống Đa, Hà Nội');

-- =====================================================
-- 7. TẠO THUỐC
-- =====================================================
INSERT INTO medical_records_thuoc (ten_thuoc, don_vi) VALUES
('Paracetamol 500mg', 'viên'),
('Amoxicillin 250mg', 'viên'),
('Vitamin C 1000mg', 'viên'),
('Aspirin 100mg', 'viên'),
('Omeprazole 20mg', 'viên'),
('Ibuprofen 400mg', 'viên'),
('Cetirizine 10mg', 'viên'),
('Metformin 500mg', 'viên'),
('Atorvastatin 20mg', 'viên'),
('Losartan 50mg', 'viên'),
('Cough Syrup', 'chai'),
('Eye Drops', 'lọ'),
('Nasal Spray', 'lọ'),
('Antiseptic Solution', 'chai'),
('Bandage', 'cuộn');

-- =====================================================
-- 8. TẠO LỊCH LÀM VIỆC CHO BÁC SĨ (14 NGÀY TỚI)
-- =====================================================

-- Tạo lịch làm việc cho tất cả bác sĩ
-- Ca sáng: 08:00 - 12:00
-- Ca chiều: 14:00 - 18:00
-- Bỏ qua chủ nhật

DELIMITER $$
CREATE PROCEDURE TaoLichLamViec()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE bac_si_id INT;
    DECLARE ngay_lam DATE;
    DECLARE i INT DEFAULT 0;
    
    DECLARE bac_si_cursor CURSOR FOR 
        SELECT id FROM accounts_hosobacsi;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN bac_si_cursor;
    
    bac_si_loop: LOOP
        FETCH bac_si_cursor INTO bac_si_id;
        IF done THEN
            LEAVE bac_si_loop;
        END IF;
        
        SET i = 0;
        WHILE i < 14 DO
            SET ngay_lam = DATE_ADD(CURDATE(), INTERVAL i DAY);
            
            -- Bỏ qua chủ nhật (DAYOFWEEK = 1)
            IF DAYOFWEEK(ngay_lam) != 1 THEN
                -- Ca sáng
                INSERT IGNORE INTO appointments_lichlamviec (bac_si_id, ngay, gio_bat_dau, gio_ket_thuc, con_trong)
                VALUES (bac_si_id, ngay_lam, '08:00:00', '12:00:00', 1);
                
                -- Ca chiều
                INSERT IGNORE INTO appointments_lichlamviec (bac_si_id, ngay, gio_bat_dau, gio_ket_thuc, con_trong)
                VALUES (bac_si_id, ngay_lam, '14:00:00', '18:00:00', 1);
            END IF;
            
            SET i = i + 1;
        END WHILE;
    END LOOP;
    
    CLOSE bac_si_cursor;
END$$
DELIMITER ;

CALL TaoLichLamViec();
DROP PROCEDURE TaoLichLamViec;

-- =====================================================
-- 9. CẬP NHẬT MẬT KHẨU (SỬ DỤNG DJANGO HASH)
-- =====================================================
-- Lưu ý: Mật khẩu được hash bằng Django, cần chạy script Python để set đúng

-- =====================================================
-- HOÀN THÀNH
-- =====================================================
SELECT 'Dữ liệu mẫu đã được tạo thành công!' as message;

-- Thống kê dữ liệu
SELECT 
    'Chuyên khoa' as loai_du_lieu, 
    COUNT(*) as so_luong 
FROM accounts_chuyenkhoa
UNION ALL
SELECT 
    'Bác sĩ' as loai_du_lieu, 
    COUNT(*) as so_luong 
FROM accounts_hosobacsi
UNION ALL
SELECT 
    'Bệnh nhân' as loai_du_lieu, 
    COUNT(*) as so_luong 
FROM accounts_hosobenhnhan
UNION ALL
SELECT 
    'Thuốc' as loai_du_lieu, 
    COUNT(*) as so_luong 
FROM medical_records_thuoc
UNION ALL
SELECT 
    'Lịch làm việc' as loai_du_lieu, 
    COUNT(*) as so_luong 
FROM appointments_lichlamviec;

-- =====================================================
-- HƯỚNG DẪN SỬ DỤNG
-- =====================================================
/*
TÀI KHOẢN MẶC ĐỊNH:
- Admin: admin/admin123
- Bác sĩ: bs_nguyenvan/123456
- Bệnh nhân: bn_nguyenthi/123456

LỚI ÍCH: Để set đúng mật khẩu Django, chạy:
python tao_du_lieu_mau.py

HOẶC trong Django shell:
python manage.py shell
>>> from django.contrib.auth.models import User
>>> for user in User.objects.all():
...     user.set_password('123456')
...     user.save()
>>> admin = User.objects.get(username='admin')
>>> admin.set_password('admin123')
>>> admin.save()
*/