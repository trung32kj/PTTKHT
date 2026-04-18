-- =====================================================
-- SCRIPT TẠO DỮ LIỆU MẪU CHO HỆ THỐNG QUẢN LÝ PHÒNG KHÁM
-- Database: pttkht
-- Cập nhật: 34 bác sĩ, 15 chuyên khoa, 10 bệnh nhân
-- =====================================================

USE pttkht;

-- Xóa dữ liệu cũ (nếu có)
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE tai_khoan_danhgiabacsi;
TRUNCATE TABLE ho_so_benh_an_toathuoc;
TRUNCATE TABLE ho_so_benh_an_hosobenhan;
TRUNCATE TABLE lich_hen_lichhen;
TRUNCATE TABLE lich_hen_lichlamviec;
TRUNCATE TABLE tai_khoan_hosobacsi;
TRUNCATE TABLE tai_khoan_hosobenhnhan;
TRUNCATE TABLE tai_khoan_chuyenkhoa;
TRUNCATE TABLE ho_so_benh_an_thuoc;
TRUNCATE TABLE hop_thoai_ai_bacsirecommendation;
TRUNCATE TABLE hop_thoai_ai_trieuchunganalysis;
TRUNCATE TABLE hop_thoai_ai_chatmessage;
TRUNCATE TABLE hop_thoai_ai_chatsession;
DELETE FROM auth_user WHERE id > 0;
SET FOREIGN_KEY_CHECKS = 1;

-- =====================================================
-- 1. TẠO 15 CHUYÊN KHOA
-- =====================================================
INSERT INTO tai_khoan_chuyenkhoa (ten, mo_ta) VALUES
('Nội khoa', 'Khám và điều trị các bệnh nội khoa tổng quát'),
('Ngoại khoa', 'Phẫu thuật và điều trị ngoại khoa'),
('Tim mạch', 'Chuyên khoa tim mạch và huyết áp'),
('Da liễu', 'Điều trị các bệnh về da, tóc, móng'),
('Tai mũi họng', 'Điều trị các bệnh tai mũi họng'),
('Mắt', 'Chuyên khoa nhãn khoa'),
('Răng hàm mặt', 'Nha khoa và phẫu thuật hàm mặt'),
('Thần kinh', 'Chuyên khoa thần kinh'),
('Tiêu hóa', 'Bệnh tiêu hóa và gan mật'),
('Sản phụ khoa', 'Sản khoa và phụ khoa'),
('Nhi khoa', 'Chuyên khoa nhi đồng'),
('Chấn thương chỉnh hình', 'Phẫu thuật xương khớp'),
('Ung bướu', 'Điều trị ung thư và u bướu'),
('Tâm thần', 'Chuyên khoa tâm thần học'),
('Phục hồi chức năng', 'Vật lý trị liệu và phục hồi chức năng');

-- =====================================================
-- 2. TẠO TÀI KHOẢN ADMIN
-- =====================================================
INSERT INTO auth_user (username, first_name, last_name, email, is_staff, is_active, is_superuser, date_joined, password) VALUES
('admin', 'Admin', 'System', 'admin@phongkham.com', 1, 1, 1, NOW(), 'pbkdf2_sha256$600000$randomsalt$hashedpassword');

-- =====================================================
-- 3. TẠO 34 TÀI KHOẢN BÁC SĨ (2-3 bác sĩ mỗi chuyên khoa)
-- =====================================================
INSERT INTO auth_user (username, first_name, last_name, email, is_staff, is_active, date_joined, password) VALUES
-- Nội khoa (3 bác sĩ)
('bs_nguyenvan', 'Nguyễn', 'Văn An', 'bs_nguyenvan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_tranvan', 'Trần', 'Văn Bình', 'bs_tranvan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_lethi', 'Lê', 'Thị Cúc', 'bs_lethi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Tim mạch (2 bác sĩ)
('bs_phamvan', 'Phạm', 'Văn Đức', 'bs_phamvan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_hoangthi', 'Hoàng', 'Thị Em', 'bs_hoangthi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Ngoại khoa (3 bác sĩ)
('bs_vuvan', 'Vũ', 'Văn Phúc', 'bs_vuvan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_dangthi', 'Đặng', 'Thị Giang', 'bs_dangthi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_buivan', 'Bùi', 'Văn Hải', 'bs_buivan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Da liễu (2 bác sĩ)
('bs_ngothi', 'Ngô', 'Thị Lan', 'bs_ngothi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_lyvan', 'Lý', 'Văn Minh', 'bs_lyvan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Tai mũi họng (2 bác sĩ)
('bs_doivan', 'Đỗ', 'Văn Nam', 'bs_doivan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_vothi', 'Võ', 'Thị Oanh', 'bs_vothi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Mắt (2 bác sĩ)
('bs_maithi', 'Mai', 'Thị Phương', 'bs_maithi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_caovan', 'Cao', 'Văn Quang', 'bs_caovan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Răng hàm mặt (3 bác sĩ)
('bs_dinhvan', 'Đinh', 'Văn Rồng', 'bs_dinhvan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_tranthi', 'Trần', 'Thị Sương', 'bs_tranthi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_levan', 'Lê', 'Văn Tài', 'bs_levan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Thần kinh (2 bác sĩ)
('bs_phamthi', 'Phạm', 'Thị Uyên', 'bs_phamthi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_hoangvan', 'Hoàng', 'Văn Việt', 'bs_hoangvan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Tiêu hóa (2 bác sĩ)
('bs_vuthi', 'Vũ', 'Thị Xuân', 'bs_vuthi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_dangvan', 'Đặng', 'Văn Yên', 'bs_dangvan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Sản phụ khoa (3 bác sĩ)
('bs_buithi', 'Bùi', 'Thị Zung', 'bs_buithi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_ngovan', 'Ngô', 'Văn An2', 'bs_ngovan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_lythi', 'Lý', 'Thị Bình2', 'bs_lythi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Nhi khoa (2 bác sĩ)
('bs_doithi', 'Đỗ', 'Thị Cường2', 'bs_doithi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_voivan', 'Võ', 'Văn Dũng2', 'bs_voivan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Chấn thương chỉnh hình (2 bác sĩ)
('bs_maivan', 'Mai', 'Văn Em2', 'bs_maivan@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_caothi', 'Cao', 'Thị Phúc2', 'bs_caothi@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Ung bướu (2 bác sĩ)
('bs_dinhvan2', 'Đinh', 'Văn Giang2', 'bs_dinhvan2@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_tranthi2', 'Trần', 'Thị Hoa2', 'bs_tranthi2@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Tâm thần (2 bác sĩ)
('bs_levan2', 'Lê', 'Văn Lan2', 'bs_levan2@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_phamthi2', 'Phạm', 'Thị Minh2', 'bs_phamthi2@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),

-- Phục hồi chức năng (2 bác sĩ)
('bs_hoangvan2', 'Hoàng', 'Văn Nam2', 'bs_hoangvan2@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bs_vuthi2', 'Vũ', 'Thị Oanh2', 'bs_vuthi2@clinic.com', 1, 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456');

-- =====================================================
-- 4. TẠO HỒ SƠ BÁC SĨ (34 bác sĩ với chuyên khoa tương ứng)
-- =====================================================
INSERT INTO tai_khoan_hosobacsi (nguoi_dung_id, chuyen_khoa_id, bang_cap, so_dien_thoai, phi_kham, mo_ta, anh_dai_dien) VALUES
-- Nội khoa (3 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_nguyenvan'), 1, 'Tiến sĩ Y khoa Nội khoa', '0901234567', 250000, 'Bác sĩ Nội khoa với 15 năm kinh nghiệm', 'bac_si/bacsi_van_an_nguyen_noi_khoa.jpg'),
((SELECT id FROM auth_user WHERE username='bs_tranvan'), 1, 'Thạc sĩ Y khoa Nội khoa', '0901234568', 220000, 'Bác sĩ Nội khoa với 10 năm kinh nghiệm', 'bac_si/bacsi_van_binh_tran_noi_khoa.jpg'),
((SELECT id FROM auth_user WHERE username='bs_lethi'), 1, 'Bác sĩ chuyên khoa I Nội khoa', '0901234569', 200000, 'Bác sĩ Nội khoa với 8 năm kinh nghiệm', 'bac_si/bacsi_thi_cuc_le_noi_khoa.jpg'),

-- Tim mạch (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_phamvan'), 3, 'Tiến sĩ Y khoa Tim mạch', '0901234570', 350000, 'Bác sĩ Tim mạch với 18 năm kinh nghiệm', 'bac_si/bacsi_van_duc_pham_tim_mach.jpg'),
((SELECT id FROM auth_user WHERE username='bs_hoangthi'), 3, 'Thạc sĩ Y khoa Tim mạch', '0901234571', 300000, 'Bác sĩ Tim mạch với 12 năm kinh nghiệm', 'bac_si/bacsi_thi_em_hoang_tim_mach.jpg'),

-- Ngoại khoa (3 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_vuvan'), 2, 'Tiến sĩ Y khoa Ngoại khoa', '0901234572', 320000, 'Bác sĩ Ngoại khoa với 16 năm kinh nghiệm', 'bac_si/bacsi_van_phuc_vu_ngoai_khoa.jpg'),
((SELECT id FROM auth_user WHERE username='bs_dangthi'), 2, 'Thạc sĩ Y khoa Ngoại khoa', '0901234573', 280000, 'Bác sĩ Ngoại khoa với 11 năm kinh nghiệm', 'bac_si/bacsi_thi_giang_dang_ngoai_khoa.jpg'),
((SELECT id FROM auth_user WHERE username='bs_buivan'), 2, 'Bác sĩ chuyên khoa II Ngoại khoa', '0901234574', 250000, 'Bác sĩ Ngoại khoa với 9 năm kinh nghiệm', 'bac_si/bacsi_van_hai_bui_ngoai_khoa.jpg'),

-- Da liễu (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_ngothi'), 4, 'Thạc sĩ Y khoa Da liễu', '0901234575', 200000, 'Bác sĩ Da liễu với 7 năm kinh nghiệm', 'bac_si/bacsi_thi_lan_ngo_da_lieu.jpg'),
((SELECT id FROM auth_user WHERE username='bs_lyvan'), 4, 'Bác sĩ chuyên khoa I Da liễu', '0901234576', 180000, 'Bác sĩ Da liễu với 6 năm kinh nghiệm', 'bac_si/bacsi_van_minh_ly_da_lieu.jpg'),

-- Tai mũi họng (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_doivan'), 5, 'Thạc sĩ Y khoa Tai mũi họng', '0901234577', 220000, 'Bác sĩ Tai mũi họng với 10 năm kinh nghiệm', 'bac_si/bacsi_van_nam_do_tai_mui_hong.jpg'),
((SELECT id FROM auth_user WHERE username='bs_vothi'), 5, 'Bác sĩ chuyên khoa I Tai mũi họng', '0901234578', 200000, 'Bác sĩ Tai mũi họng với 8 năm kinh nghiệm', 'bac_si/bacsi_thi_oanh_vo_tai_mui_hong.jpg'),

-- Mắt (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_maithi'), 6, 'Thạc sĩ Y khoa Nhãn khoa', '0901234579', 250000, 'Bác sĩ Mắt với 12 năm kinh nghiệm', 'bac_si/bacsi_thi_phuong_mai_mat.jpg'),
((SELECT id FROM auth_user WHERE username='bs_caovan'), 6, 'Bác sĩ chuyên khoa II Nhãn khoa', '0901234580', 230000, 'Bác sĩ Mắt với 9 năm kinh nghiệm', 'bac_si/bacsi_van_quang_cao_mat.jpg'),

-- Răng hàm mặt (3 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_dinhvan'), 7, 'Tiến sĩ Nha khoa', '0901234581', 180000, 'Bác sĩ Răng hàm mặt với 14 năm kinh nghiệm', 'bac_si/bacsi_van_rong_dinh_rang_ham_mat.jpg'),
((SELECT id FROM auth_user WHERE username='bs_tranthi'), 7, 'Thạc sĩ Nha khoa', '0901234582', 160000, 'Bác sĩ Răng hàm mặt với 8 năm kinh nghiệm', 'bac_si/bacsi_thi_suong_tran_rang_ham_mat.jpg'),
((SELECT id FROM auth_user WHERE username='bs_levan'), 7, 'Bác sĩ Nha khoa', '0901234583', 150000, 'Bác sĩ Răng hàm mặt với 6 năm kinh nghiệm', 'bac_si/bacsi_van_tai_le_rang_ham_mat.jpg'),

-- Thần kinh (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_phamthi'), 8, 'Tiến sĩ Y khoa Thần kinh', '0901234584', 400000, 'Bác sĩ Thần kinh với 20 năm kinh nghiệm', 'bac_si/bacsi_thi_uyen_pham_than_kinh.jpg'),
((SELECT id FROM auth_user WHERE username='bs_hoangvan'), 8, 'Thạc sĩ Y khoa Thần kinh', '0901234585', 350000, 'Bác sĩ Thần kinh với 15 năm kinh nghiệm', 'bac_si/bacsi_van_viet_hoang_than_kinh.jpg'),

-- Tiêu hóa (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_vuthi'), 9, 'Thạc sĩ Y khoa Tiêu hóa', '0901234586', 280000, 'Bác sĩ Tiêu hóa với 11 năm kinh nghiệm', 'bac_si/bacsi_thi_xuan_vu_tieu_hoa.jpg'),
((SELECT id FROM auth_user WHERE username='bs_dangvan'), 9, 'Bác sĩ chuyên khoa II Tiêu hóa', '0901234587', 260000, 'Bác sĩ Tiêu hóa với 9 năm kinh nghiệm', 'bac_si/bacsi_van_yen_dang_tieu_hoa.jpg'),

-- Sản phụ khoa (3 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_buithi'), 10, 'Tiến sĩ Y khoa Sản phụ khoa', '0901234588', 300000, 'Bác sĩ Sản phụ khoa với 16 năm kinh nghiệm', 'bac_si/bacsi_thi_zung_bui_san_phu_khoa.jpg'),
((SELECT id FROM auth_user WHERE username='bs_ngovan'), 10, 'Thạc sĩ Y khoa Sản phụ khoa', '0901234589', 280000, 'Bác sĩ Sản phụ khoa với 12 năm kinh nghiệm', 'bac_si/bacsi_van_an2_ngo_san_phu_khoa.jpg'),
((SELECT id FROM auth_user WHERE username='bs_lythi'), 10, 'Bác sĩ chuyên khoa I Sản phụ khoa', '0901234590', 250000, 'Bác sĩ Sản phụ khoa với 8 năm kinh nghiệm', 'bac_si/bacsi_thi_binh2_ly_san_phu_khoa.jpg'),

-- Nhi khoa (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_doithi'), 11, 'Thạc sĩ Y khoa Nhi khoa', '0901234591', 220000, 'Bác sĩ Nhi khoa với 10 năm kinh nghiệm', 'bac_si/bacsi_thi_cuong2_do_nhi_khoa.jpg'),
((SELECT id FROM auth_user WHERE username='bs_voivan'), 11, 'Bác sĩ chuyên khoa I Nhi khoa', '0901234592', 200000, 'Bác sĩ Nhi khoa với 7 năm kinh nghiệm', 'bac_si/bacsi_van_dung2_vo_nhi_khoa.jpg'),

-- Chấn thương chỉnh hình (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_maivan'), 12, 'Tiến sĩ Y khoa Chấn thương chỉnh hình', '0901234593', 350000, 'Bác sĩ Chấn thương chỉnh hình với 18 năm kinh nghiệm', 'bac_si/bacsi_van_em2_mai_chan_thuong_chinh_hinh.jpg'),
((SELECT id FROM auth_user WHERE username='bs_caothi'), 12, 'Thạc sĩ Y khoa Chấn thương chỉnh hình', '0901234594', 320000, 'Bác sĩ Chấn thương chỉnh hình với 14 năm kinh nghiệm', 'bac_si/bacsi_thi_phuc2_cao_chan_thuong_chinh_hinh.jpg'),

-- Ung bướu (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_dinhvan2'), 13, 'Tiến sĩ Y khoa Ung bướu', '0901234595', 450000, 'Bác sĩ Ung bướu với 22 năm kinh nghiệm', 'bac_si/bacsi_van_giang2_dinh_ung_buou.jpg'),
((SELECT id FROM auth_user WHERE username='bs_tranthi2'), 13, 'Thạc sĩ Y khoa Ung bướu', '0901234596', 400000, 'Bác sĩ Ung bướu với 16 năm kinh nghiệm', 'bac_si/bacsi_thi_hoa2_tran_ung_buou.jpg'),

-- Tâm thần (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_levan2'), 14, 'Tiến sĩ Y khoa Tâm thần', '0901234597', 380000, 'Bác sĩ Tâm thần với 19 năm kinh nghiệm', 'bac_si/bacsi_van_lan2_le_tam_than.jpg'),
((SELECT id FROM auth_user WHERE username='bs_phamthi2'), 14, 'Thạc sĩ Y khoa Tâm thần', '0901234598', 350000, 'Bác sĩ Tâm thần với 15 năm kinh nghiệm', 'bac_si/bacsi_thi_minh2_pham_tam_than.jpg'),

-- Phục hồi chức năng (2 bác sĩ)
((SELECT id FROM auth_user WHERE username='bs_hoangvan2'), 15, 'Thạc sĩ Y khoa Phục hồi chức năng', '0901234599', 250000, 'Bác sĩ Phục hồi chức năng với 11 năm kinh nghiệm', 'bac_si/bacsi_van_nam2_hoang_phuc_hoi_chuc_nang.jpg'),
((SELECT id FROM auth_user WHERE username='bs_vuthi2'), 15, 'Bác sĩ chuyên khoa I Phục hồi chức năng', '0901234600', 230000, 'Bác sĩ Phục hồi chức năng với 8 năm kinh nghiệm', 'bac_si/bacsi_thi_oanh2_vu_phuc_hoi_chuc_nang.jpg');

-- =====================================================
-- 5. TẠO 10 TÀI KHOẢN BỆNH NHÂN
-- =====================================================
INSERT INTO auth_user (username, first_name, last_name, email, is_active, date_joined, password) VALUES
('bn_nguyenthi', 'Nguyễn', 'Thị Hoa', 'bn_nguyenthi@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_tranvan', 'Trần', 'Văn Nam', 'bn_tranvan@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_lethi', 'Lê', 'Thị Mai', 'bn_lethi@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_phamvan', 'Phạm', 'Văn Đức', 'bn_phamvan@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_hoangthi', 'Hoàng', 'Thị Linh', 'bn_hoangthi@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_vuvan', 'Vũ', 'Văn Tùng', 'bn_vuvan@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_dangthi', 'Đặng', 'Thị Yến', 'bn_dangthi@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_buivan', 'Bùi', 'Văn Khoa', 'bn_buivan@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_ngothi', 'Ngô', 'Thị Lan', 'bn_ngothi@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456'),
('bn_lyvan', 'Lý', 'Văn Minh', 'bn_lyvan@patient.com', 1, NOW(), 'pbkdf2_sha256$600000$salt$hash123456');

-- =====================================================
-- 6. TẠO HỒ SƠ BỆNH NHÂN
-- =====================================================
INSERT INTO tai_khoan_hosobenhnhan (nguoi_dung_id, ngay_sinh, gioi_tinh, so_dien_thoai, dia_chi, anh_dai_dien) VALUES
((SELECT id FROM auth_user WHERE username='bn_nguyenthi'), '1990-05-15', 'F', '0987654321', 'Số 10, Phố Huế, Hai Bà Trưng, Hà Nội', 'benh_nhan/benhnhan_thi_hoa_nguyen_nu.jpg'),
((SELECT id FROM auth_user WHERE username='bn_tranvan'), '1985-08-20', 'M', '0987654322', '123 Nguyễn Huệ, Quận 1, TP.HCM', 'benh_nhan/benhnhan_van_nam_tran_nam.jpg'),
((SELECT id FROM auth_user WHERE username='bn_lethi'), '1992-12-10', 'F', '0987654323', '45 Trần Phú, Hải Châu, Đà Nẵng', 'benh_nhan/benhnhan_thi_mai_le_nu.jpg'),
((SELECT id FROM auth_user WHERE username='bn_phamvan'), '1988-03-25', 'M', '0987654324', '67 Lê Lợi, Quận 1, TP.HCM', 'benh_nhan/benhnhan_van_duc_pham_nam.jpg'),
((SELECT id FROM auth_user WHERE username='bn_hoangthi'), '1995-07-08', 'F', '0987654325', '89 Điện Biên Phủ, Ba Đình, Hà Nội', 'benh_nhan/benhnhan_thi_linh_hoang_nu.jpg'),
((SELECT id FROM auth_user WHERE username='bn_vuvan'), '1987-11-30', 'M', '0987654326', '12 Ngô Quyền, Sơn Trà, Đà Nẵng', 'benh_nhan/benhnhan_van_tung_vu_nam.jpg'),
((SELECT id FROM auth_user WHERE username='bn_dangthi'), '1993-09-14', 'F', '0987654327', '34 Hai Bà Trưng, Quận 3, TP.HCM', 'benh_nhan/benhnhan_thi_yen_dang_nu.jpg'),
((SELECT id FROM auth_user WHERE username='bn_buivan'), '1991-01-22', 'M', '0987654328', '56 Láng Hạ, Đống Đa, Hà Nội', 'benh_nhan/benhnhan_van_khoa_bui_nam.jpg'),
((SELECT id FROM auth_user WHERE username='bn_ngothi'), '1994-04-18', 'F', '0987654329', '78 Lê Duẩn, Quận 1, TP.HCM', 'benh_nhan/benhnhan_thi_lan_ngo_nu.jpg'),
((SELECT id FROM auth_user WHERE username='bn_lyvan'), '1989-06-12', 'M', '0987654330', '90 Trường Chinh, Thanh Xuân, Hà Nội', 'benh_nhan/benhnhan_van_minh_ly_nam.jpg');

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
-- 7. TẠO 15 LOẠI THUỐC
-- =====================================================
INSERT INTO ho_so_benh_an_thuoc (ten_thuoc, don_vi) VALUES
('Paracetamol 500mg', 'viên'),
('Amoxicillin 500mg', 'viên'),
('Ibuprofen 400mg', 'viên'),
('Omeprazole 20mg', 'viên'),
('Cetirizine 10mg', 'viên'),
('Metformin 500mg', 'viên'),
('Amlodipine 5mg', 'viên'),
('Atorvastatin 20mg', 'viên'),
('Losartan 50mg', 'viên'),
('Aspirin 100mg', 'viên'),
('Vitamin D3 1000IU', 'viên'),
('Calcium 500mg', 'viên'),
('Dexamethasone 0.5mg', 'viên'),
('Furosemide 40mg', 'viên'),
('Simvastatin 20mg', 'viên');

-- =====================================================
-- 8. TẠO LỊCH LÀM VIỆC CHO 34 BÁC SĨ (30 NGÀY TỚI)
-- =====================================================

DELIMITER $
CREATE PROCEDURE TaoLichLamViecMoi()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE bac_si_id INT;
    DECLARE ngay_lam DATE;
    DECLARE i INT DEFAULT 0;
    
    DECLARE bac_si_cursor CURSOR FOR 
        SELECT id FROM tai_khoan_hosobacsi;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN bac_si_cursor;
    
    bac_si_loop: LOOP
        FETCH bac_si_cursor INTO bac_si_id;
        IF done THEN
            LEAVE bac_si_loop;
        END IF;
        
        SET i = 0;
        WHILE i < 30 DO
            SET ngay_lam = DATE_ADD(CURDATE(), INTERVAL i DAY);
            
            -- Bỏ qua chủ nhật (DAYOFWEEK = 1)
            IF DAYOFWEEK(ngay_lam) != 1 THEN
                -- 70% khả năng có ca sáng
                IF RAND() < 0.7 THEN
                    INSERT IGNORE INTO lich_hen_lichlamviec (bac_si_id, ngay, gio_bat_dau, gio_ket_thuc, con_trong)
                    VALUES (bac_si_id, ngay_lam, '08:00:00', '12:00:00', 1);
                END IF;
                
                -- 60% khả năng có ca chiều
                IF RAND() < 0.6 THEN
                    INSERT IGNORE INTO lich_hen_lichlamviec (bac_si_id, ngay, gio_bat_dau, gio_ket_thuc, con_trong)
                    VALUES (bac_si_id, ngay_lam, '14:00:00', '18:00:00', 1);
                END IF;
            END IF;
            
            SET i = i + 1;
        END WHILE;
    END LOOP;
    
    CLOSE bac_si_cursor;
END$
DELIMITER ;

CALL TaoLichLamViecMoi();
DROP PROCEDURE TaoLichLamViecMoi;

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
FROM tai_khoan_chuyenkhoa
UNION ALL
SELECT 
    'Bác sĩ' as loai_du_lieu, 
    COUNT(*) as so_luong 
FROM tai_khoan_hosobacsi
UNION ALL
SELECT 
    'Bệnh nhân' as loai_du_lieu, 
    COUNT(*) as so_luong 
FROM tai_khoan_hosobenhnhan
UNION ALL
SELECT 
    'Thuốc' as loai_du_lieu, 
    COUNT(*) as so_luong 
FROM ho_so_benh_an_thuoc
UNION ALL
SELECT 
    'Lịch làm việc' as loai_du_lieu, 
    COUNT(*) as so_luong 
FROM lich_hen_lichlamviec;

-- =====================================================
-- HƯỚNG DẪN SỬ DỤNG
-- =====================================================
/*
CẤU TRÚC DỮ LIỆU MỚI:
- 15 chuyên khoa (mỗi chuyên khoa có 2-3 bác sĩ)
- 34 bác sĩ với ảnh đại diện
- 10 bệnh nhân với ảnh đại diện
- 15 loại thuốc
- Lịch làm việc cho 30 ngày tới

TÀI KHOẢN MẶC ĐỊNH:
- Admin: admin/admin123
- Bác sĩ: bs_nguyenvan/123456, bs_phamvan/123456, v.v.
- Bệnh nhân: bn_nguyenthi/123456, bn_tranvan/123456, v.v.

CÁCH SỬ DỤNG:
1. Import file SQL này vào database pttkht
2. Chạy: python tao_du_lieu_mau.py (để set đúng mật khẩu Django)
3. Chạy: python manage.py runserver
4. Truy cập: http://127.0.0.1:8000/

LƯU Ý: 
- Tất cả tên thư mục đã được đổi thành tiếng Việt không dấu
- Ảnh đại diện được lưu trong file_media/bac_si/ và file_media/benh_nhan/
- Template được lưu trong mau_giao_dien/
*/