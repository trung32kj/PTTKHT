from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Import sample data from SQL equivalent'

    def handle(self, *args, **options):
        from tai_khoan.models import ChuyenKhoa, HoSoBacSi, HoSoBenhNhan
        from ho_so_benh_an.models import Thuoc
        from lich_hen.models import LichLamViec
        
        self.stdout.write('🔄 Bắt đầu import dữ liệu mẫu...')
        
        # 1. Tạo chuyên khoa
        chuyen_khoa_data = [
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
            ('Phục hồi chức năng', 'Vật lý trị liệu và phục hồi chức năng'),
        ]
        
        chuyen_khoa_map = {}
        for ten, mo_ta in chuyen_khoa_data:
            ck, created = ChuyenKhoa.objects.get_or_create(ten=ten, defaults={'mo_ta': mo_ta})
            chuyen_khoa_map[ten] = ck
            if created:
                self.stdout.write(f'✅ Tạo chuyên khoa: {ten}')
        
        # 2. Tạo bác sĩ
        bac_si_data = [
            # Nội khoa
            ('bs_nguyenvan', 'Nguyễn', 'Văn An', 'bs_nguyenvan@clinic.com', 1, 'Tiến sĩ Y khoa Nội khoa', '0901234567', 250000, 'Bác sĩ Nội khoa với 15 năm kinh nghiệm'),
            ('bs_tranvan', 'Trần', 'Văn Bình', 'bs_tranvan@clinic.com', 1, 'Thạc sĩ Y khoa Nội khoa', '0901234568', 220000, 'Bác sĩ Nội khoa với 10 năm kinh nghiệm'),
            ('bs_lethi', 'Lê', 'Thị Cúc', 'bs_lethi@clinic.com', 1, 'Bác sĩ chuyên khoa I Nội khoa', '0901234569', 200000, 'Bác sĩ Nội khoa với 8 năm kinh nghiệm'),
            # Tim mạch
            ('bs_phamvan', 'Phạm', 'Văn Đức', 'bs_phamvan@clinic.com', 3, 'Tiến sĩ Y khoa Tim mạch', '0901234570', 350000, 'Bác sĩ Tim mạch với 18 năm kinh nghiệm'),
            ('bs_hoangthi', 'Hoàng', 'Thị Em', 'bs_hoangthi@clinic.com', 3, 'Thạc sĩ Y khoa Tim mạch', '0901234571', 300000, 'Bác sĩ Tim mạch với 12 năm kinh nghiệm'),
            # Ngoại khoa
            ('bs_vuvan', 'Vũ', 'Văn Phúc', 'bs_vuvan@clinic.com', 2, 'Tiến sĩ Y khoa Ngoại khoa', '0901234572', 320000, 'Bác sĩ Ngoại khoa với 16 năm kinh nghiệm'),
            ('bs_dangthi', 'Đặng', 'Thị Giang', 'bs_dangthi@clinic.com', 2, 'Thạc sĩ Y khoa Ngoại khoa', '0901234573', 280000, 'Bác sĩ Ngoại khoa với 11 năm kinh nghiệm'),
            ('bs_buivan', 'Bùi', 'Văn Hải', 'bs_buivan@clinic.com', 2, 'Bác sĩ chuyên khoa II Ngoại khoa', '0901234574', 250000, 'Bác sĩ Ngoại khoa với 9 năm kinh nghiệm'),
            # Da liễu
            ('bs_ngothi', 'Ngô', 'Thị Lan', 'bs_ngothi@clinic.com', 4, 'Thạc sĩ Y khoa Da liễu', '0901234575', 200000, 'Bác sĩ Da liễu với 7 năm kinh nghiệm'),
            ('bs_lyvan', 'Lý', 'Văn Minh', 'bs_lyvan@clinic.com', 4, 'Bác sĩ chuyên khoa I Da liễu', '0901234576', 180000, 'Bác sĩ Da liễu với 6 năm kinh nghiệm'),
            # Tai mũi họng
            ('bs_doivan', 'Đỗ', 'Văn Nam', 'bs_doivan@clinic.com', 5, 'Thạc sĩ Y khoa Tai mũi họng', '0901234577', 220000, 'Bác sĩ Tai mũi họng với 10 năm kinh nghiệm'),
            ('bs_vothi', 'Võ', 'Thị Oanh', 'bs_vothi@clinic.com', 5, 'Bác sĩ chuyên khoa I Tai mũi họng', '0901234578', 200000, 'Bác sĩ Tai mũi họng với 8 năm kinh nghiệm'),
            # Mắt
            ('bs_maithi', 'Mai', 'Thị Phương', 'bs_maithi@clinic.com', 6, 'Thạc sĩ Y khoa Nhãn khoa', '0901234579', 250000, 'Bác sĩ Mắt với 12 năm kinh nghiệm'),
            ('bs_caovan', 'Cao', 'Văn Quang', 'bs_caovan@clinic.com', 6, 'Bác sĩ chuyên khoa II Nhãn khoa', '0901234580', 230000, 'Bác sĩ Mắt với 9 năm kinh nghiệm'),
            # Răng hàm mặt
            ('bs_dinhvan', 'Đinh', 'Văn Rồng', 'bs_dinhvan@clinic.com', 7, 'Tiến sĩ Nha khoa', '0901234581', 180000, 'Bác sĩ Răng hàm mặt với 14 năm kinh nghiệm'),
            ('bs_tranthi', 'Trần', 'Thị Sương', 'bs_tranthi@clinic.com', 7, 'Thạc sĩ Nha khoa', '0901234582', 160000, 'Bác sĩ Răng hàm mặt với 8 năm kinh nghiệm'),
            ('bs_levan', 'Lê', 'Văn Tài', 'bs_levan@clinic.com', 7, 'Bác sĩ Nha khoa', '0901234583', 150000, 'Bác sĩ Răng hàm mặt với 6 năm kinh nghiệm'),
            # Thần kinh
            ('bs_phamthi', 'Phạm', 'Thị Uyên', 'bs_phamthi@clinic.com', 8, 'Tiến sĩ Y khoa Thần kinh', '0901234584', 400000, 'Bác sĩ Thần kinh với 20 năm kinh nghiệm'),
            ('bs_hoangvan', 'Hoàng', 'Văn Việt', 'bs_hoangvan@clinic.com', 8, 'Thạc sĩ Y khoa Thần kinh', '0901234585', 350000, 'Bác sĩ Thần kinh với 15 năm kinh nghiệm'),
            # Tiêu hóa
            ('bs_vuthi', 'Vũ', 'Thị Xuân', 'bs_vuthi@clinic.com', 9, 'Thạc sĩ Y khoa Tiêu hóa', '0901234586', 280000, 'Bác sĩ Tiêu hóa với 11 năm kinh nghiệm'),
            ('bs_dangvan', 'Đặng', 'Văn Yên', 'bs_dangvan@clinic.com', 9, 'Bác sĩ chuyên khoa II Tiêu hóa', '0901234587', 260000, 'Bác sĩ Tiêu hóa với 9 năm kinh nghiệm'),
            # Sản phụ khoa
            ('bs_buithi', 'Bùi', 'Thị Zung', 'bs_buithi@clinic.com', 10, 'Tiến sĩ Y khoa Sản phụ khoa', '0901234588', 300000, 'Bác sĩ Sản phụ khoa với 16 năm kinh nghiệm'),
            ('bs_ngovan', 'Ngô', 'Văn An2', 'bs_ngovan@clinic.com', 10, 'Thạc sĩ Y khoa Sản phụ khoa', '0901234589', 280000, 'Bác sĩ Sản phụ khoa với 12 năm kinh nghiệm'),
            ('bs_lythi', 'Lý', 'Thị Bình2', 'bs_lythi@clinic.com', 10, 'Bác sĩ chuyên khoa I Sản phụ khoa', '0901234590', 250000, 'Bác sĩ Sản phụ khoa với 8 năm kinh nghiệm'),
            # Nhi khoa
            ('bs_doithi', 'Đỗ', 'Thị Cường2', 'bs_doithi@clinic.com', 11, 'Thạc sĩ Y khoa Nhi khoa', '0901234591', 220000, 'Bác sĩ Nhi khoa với 10 năm kinh nghiệm'),
            ('bs_voivan', 'Võ', 'Văn Dũng2', 'bs_voivan@clinic.com', 11, 'Bác sĩ chuyên khoa I Nhi khoa', '0901234592', 200000, 'Bác sĩ Nhi khoa với 7 năm kinh nghiệm'),
            # Chấn thương chỉnh hình
            ('bs_maivan', 'Mai', 'Văn Em2', 'bs_maivan@clinic.com', 12, 'Tiến sĩ Y khoa Chấn thương chỉnh hình', '0901234593', 350000, 'Bác sĩ Chấn thương chỉnh hình với 18 năm kinh nghiệm'),
            ('bs_caothi', 'Cao', 'Thị Phúc2', 'bs_caothi@clinic.com', 12, 'Thạc sĩ Y khoa Chấn thương chỉnh hình', '0901234594', 320000, 'Bác sĩ Chấn thương chỉnh hình với 14 năm kinh nghiệm'),
            # Ung bướu
            ('bs_dinhvan2', 'Đinh', 'Văn Giang2', 'bs_dinhvan2@clinic.com', 13, 'Tiến sĩ Y khoa Ung bướu', '0901234595', 450000, 'Bác sĩ Ung bướu với 22 năm kinh nghiệm'),
            ('bs_tranthi2', 'Trần', 'Thị Hoa2', 'bs_tranthi2@clinic.com', 13, 'Thạc sĩ Y khoa Ung bướu', '0901234596', 400000, 'Bác sĩ Ung bướu với 16 năm kinh nghiệm'),
            # Tâm thần
            ('bs_levan2', 'Lê', 'Văn Lan2', 'bs_levan2@clinic.com', 14, 'Tiến sĩ Y khoa Tâm thần', '0901234597', 380000, 'Bác sĩ Tâm thần với 19 năm kinh nghiệm'),
            ('bs_phamthi2', 'Phạm', 'Thị Minh2', 'bs_phamthi2@clinic.com', 14, 'Thạc sĩ Y khoa Tâm thần', '0901234598', 350000, 'Bác sĩ Tâm thần với 15 năm kinh nghiệm'),
            # Phục hồi chức năng
            ('bs_hoangvan2', 'Hoàng', 'Văn Nam2', 'bs_hoangvan2@clinic.com', 15, 'Thạc sĩ Y khoa Phục hồi chức năng', '0901234599', 250000, 'Bác sĩ Phục hồi chức năng với 11 năm kinh nghiệm'),
            ('bs_vuthi2', 'Vũ', 'Thị Oanh2', 'bs_vuthi2@clinic.com', 15, 'Bác sĩ chuyên khoa I Phục hồi chức năng', '0901234600', 230000, 'Bác sĩ Phục hồi chức năng với 8 năm kinh nghiệm'),
        ]
        
        bac_si_map = {}
        for username, first_name, last_name, email, ck_index, bang_cap, sdt, phi_kham, mo_ta in bac_si_data:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'is_staff': True,
                    'is_active': True,
                }
            )
            if created:
                user.set_password('123456')
                user.save()
            
            ck = chuyen_khoa_map[list(chuyen_khoa_map.keys())[ck_index - 1]]
            ho_so, created = HoSoBacSi.objects.get_or_create(
                nguoi_dung=user,
                defaults={
                    'chuyen_khoa': ck,
                    'bang_cap': bang_cap,
                    'so_dien_thoai': sdt,
                    'phi_kham': phi_kham,
                    'mo_ta': mo_ta,
                }
            )
            bac_si_map[username] = ho_so
            if created:
                self.stdout.write(f'✅ Tạo bác sĩ: {first_name} {last_name}')
        
        # 3. Tạo bệnh nhân
        benh_nhan_data = [
            ('bn_nguyenthi', 'Nguyễn', 'Thị Hoa', 'bn_nguyenthi@patient.com', '1990-05-15', 'F', '0987654321', 'Số 10, Phố Huế, Hai Bà Trưng, Hà Nội'),
            ('bn_tranvan', 'Trần', 'Văn Nam', 'bn_tranvan@patient.com', '1985-08-20', 'M', '0987654322', '123 Nguyễn Huệ, Quận 1, TP.HCM'),
            ('bn_lethi', 'Lê', 'Thị Mai', 'bn_lethi@patient.com', '1992-12-10', 'F', '0987654323', '45 Trần Phú, Hải Châu, Đà Nẵng'),
            ('bn_phamvan', 'Phạm', 'Văn Đức', 'bn_phamvan@patient.com', '1988-03-25', 'M', '0987654324', '67 Lê Lợi, Quận 1, TP.HCM'),
            ('bn_hoangthi', 'Hoàng', 'Thị Linh', 'bn_hoangthi@patient.com', '1995-07-08', 'F', '0987654325', '89 Điện Biên Phủ, Ba Đình, Hà Nội'),
            ('bn_vuvan', 'Vũ', 'Văn Tùng', 'bn_vuvan@patient.com', '1987-11-30', 'M', '0987654326', '12 Ngô Quyền, Sơn Trà, Đà Nẵng'),
            ('bn_dangthi', 'Đặng', 'Thị Yến', 'bn_dangthi@patient.com', '1993-09-14', 'F', '0987654327', '34 Hai Bà Trưng, Quận 3, TP.HCM'),
            ('bn_buivan', 'Bùi', 'Văn Khoa', 'bn_buivan@patient.com', '1991-01-22', 'M', '0987654328', '56 Láng Hạ, Đống Đa, Hà Nội'),
            ('bn_ngothi', 'Ngô', 'Thị Lan', 'bn_ngothi@patient.com', '1994-04-18', 'F', '0987654329', '78 Lê Duẩn, Quận 1, TP.HCM'),
            ('bn_lyvan', 'Lý', 'Văn Minh', 'bn_lyvan@patient.com', '1989-06-12', 'M', '0987654330', '90 Trường Chinh, Thanh Xuân, Hà Nội'),
        ]
        
        for username, first_name, last_name, email, ngay_sinh, gioi_tinh, sdt, dia_chi in benh_nhan_data:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'is_active': True,
                }
            )
            if created:
                user.set_password('123456')
                user.save()
            
            ho_so, created = HoSoBenhNhan.objects.get_or_create(
                nguoi_dung=user,
                defaults={
                    'ngay_sinh': ngay_sinh,
                    'gioi_tinh': gioi_tinh,
                    'so_dien_thoai': sdt,
                    'dia_chi': dia_chi,
                }
            )
            if created:
                self.stdout.write(f'✅ Tạo bệnh nhân: {first_name} {last_name}')
        
        # 4. Tạo thuốc
        thuoc_data = [
            'Paracetamol 500mg', 'Amoxicillin 500mg', 'Ibuprofen 400mg', 'Omeprazole 20mg',
            'Cetirizine 10mg', 'Metformin 500mg', 'Amlodipine 5mg', 'Atorvastatin 20mg',
            'Losartan 50mg', 'Aspirin 100mg', 'Vitamin D3 1000IU', 'Calcium 500mg',
            'Dexamethasone 0.5mg', 'Furosemide 40mg', 'Simvastatin 20mg',
        ]
        
        for ten_thuoc in thuoc_data:
            thuoc, created = Thuoc.objects.get_or_create(ten_thuoc=ten_thuoc, defaults={'don_vi': 'viên'})
            if created:
                self.stdout.write(f'✅ Tạo thuốc: {ten_thuoc}')
        
        # 5. Tạo lịch làm việc cho 30 ngày tới
        self.stdout.write('🔄 Tạo lịch làm việc...')
        for ho_so_bac_si in HoSoBacSi.objects.all():
            for i in range(30):
                ngay = timezone.now().date() + timedelta(days=i)
                
                # Bỏ qua chủ nhật
                if ngay.weekday() == 6:
                    continue
                
                # 70% khả năng có ca sáng
                if random.random() < 0.7:
                    LichLamViec.objects.get_or_create(
                        bac_si=ho_so_bac_si,
                        ngay=ngay,
                        gio_bat_dau='08:00',
                        gio_ket_thuc='12:00',
                        defaults={'con_trong': True}
                    )
                
                # 60% khả năng có ca chiều
                if random.random() < 0.6:
                    LichLamViec.objects.get_or_create(
                        bac_si=ho_so_bac_si,
                        ngay=ngay,
                        gio_bat_dau='14:00',
                        gio_ket_thuc='18:00',
                        defaults={'con_trong': True}
                    )
        
        self.stdout.write(self.style.SUCCESS('✅ Import dữ liệu mẫu thành công!'))
