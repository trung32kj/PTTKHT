# Generated migration for ai_chatbox

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=100, unique=True, verbose_name='ID phiên')),
                ('ngay_tao', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('trang_thai', models.CharField(choices=[('active', 'Đang hoạt động'), ('completed', 'Hoàn thành'), ('cancelled', 'Đã hủy')], default='active', max_length=20, verbose_name='Trạng thái')),
                ('benh_nhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_sessions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Phiên chat',
                'verbose_name_plural': 'Phiên chat',
                'ordering': ['-ngay_tao'],
            },
        ),
        migrations.CreateModel(
            name='TrieuChungAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trieu_chung_goc', models.TextField(verbose_name='Triệu chứng gốc')),
                ('do_tin_cay', models.FloatField(default=0.0, verbose_name='Độ tin cậy (%)')),
                ('phan_tich_chi_tiet', models.JSONField(verbose_name='Phân tích chi tiết')),
                ('ngay_phan_tich', models.DateTimeField(auto_now_add=True, verbose_name='Ngày phân tích')),
                ('chat_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analyses', to='ai_chatbox.chatsession')),
                ('chuyen_khoa_de_xuat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.chuyenkhoa', verbose_name='Chuyên khoa đề xuất')),
            ],
            options={
                'verbose_name': 'Phân tích triệu chứng',
                'verbose_name_plural': 'Phân tích triệu chứng',
                'ordering': ['-ngay_phan_tich'],
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nguoi_gui', models.CharField(choices=[('user', 'Người dùng'), ('ai', 'AI'), ('system', 'Hệ thống')], max_length=10, verbose_name='Người gửi')),
                ('noi_dung', models.TextField(verbose_name='Nội dung')),
                ('thoi_gian', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian')),
                ('metadata', models.JSONField(blank=True, null=True, verbose_name='Dữ liệu bổ sung')),
                ('chat_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='ai_chatbox.chatsession')),
            ],
            options={
                'verbose_name': 'Tin nhắn chat',
                'verbose_name_plural': 'Tin nhắn chat',
                'ordering': ['thoi_gian'],
            },
        ),
        migrations.CreateModel(
            name='BacSiRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thu_tu_uu_tien', models.IntegerField(verbose_name='Thứ tự ưu tiên')),
                ('ly_do_goi_y', models.TextField(verbose_name='Lý do gợi ý')),
                ('rating_score', models.FloatField(verbose_name='Điểm rating')),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='ai_chatbox.trieuchunganalysis')),
                ('bac_si', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hosobacsi', verbose_name='Bác sĩ')),
            ],
            options={
                'verbose_name': 'Gợi ý bác sĩ',
                'verbose_name_plural': 'Gợi ý bác sĩ',
                'ordering': ['thu_tu_uu_tien'],
            },
        ),
    ]