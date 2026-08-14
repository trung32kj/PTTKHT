#!/usr/bin/env bash
# Script build chạy trên Render trước mỗi lần deploy
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
