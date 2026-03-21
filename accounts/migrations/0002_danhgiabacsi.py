# Generated migration for DanhGiaBacSi model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DanhGiaBacSi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diem_so', models.IntegerField(choices=[(1, '1 sao'), (2, '2 sao'), (3, '3 sao'), (4, '4 sao'), (5, '5 sao')], verbose_name='Điểm số')),
                ('nhan_xet', models.TextField(blank=True, verbose_name='Nhận xét')),
                ('ngay_danh_gia', models.DateTimeField(auto_now_add=True, verbose_name='Ngày đánh giá')),
                ('bac_si', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='danh_gia', to='accounts.hosobacsi')),
                ('benh_nhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='danh_gia_da_cho', to='accounts.hosobenhnhan')),
            ],
            options={
                'verbose_name': 'Đánh giá bác sĩ',
                'verbose_name_plural': 'Đánh giá bác sĩ',
            },
        ),
        migrations.AlterUniqueTogether(
            name='danhgiabacsi',
            unique_together={('bac_si', 'benh_nhan')},
        ),
    ]