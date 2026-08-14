#!/usr/bin/env bash
# Script build chạy trên Render trước mỗi lần deploy
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Tạo tài khoản admin nếu chưa có (gói free của Render không có tab Shell).
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  export DJANGO_SUPERUSER_EMAIL="${DJANGO_SUPERUSER_EMAIL:-admin@example.com}"
  python manage.py createsuperuser --no-input || \
    echo "Bo qua: tai khoan admin '$DJANGO_SUPERUSER_USERNAME' da ton tai."
fi
