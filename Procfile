release: python manage.py migrate --noinput && python create_superuser.py && python manage.py loaddata data.json
web: gunicorn quan_ly_phong_kham.wsgi:application
