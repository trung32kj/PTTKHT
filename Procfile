release: python manage.py migrate --noinput && python create_superuser.py && python manage.py import_sample_data
web: gunicorn quan_ly_phong_kham.wsgi:application
