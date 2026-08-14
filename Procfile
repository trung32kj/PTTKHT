release: python manage.py migrate --noinput && python create_superuser.py
web: gunicorn quan_ly_phong_kham.wsgi:application
