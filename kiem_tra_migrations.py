#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quan_ly_phong_kham.settings')
sys.path.append('.')
django.setup()

from django.db import connection

def check_migrations():
    with connection.cursor() as cursor:
        cursor.execute("SELECT app, name FROM django_migrations ORDER BY app, name")
        migrations = cursor.fetchall()
        print("Current migrations in database:")
        for app, name in migrations:
            print(f"  {app}: {name}")
        
        print("\nLooking for old app names in migrations:")
        old_apps = [m for m in migrations if m[0] in ['accounts', 'ai_chatbox', 'appointments', 'medical_records', 'dashboard']]
        if old_apps:
            print("Found old app migrations:")
            for app, name in old_apps:
                print(f"  {app}: {name}")
        else:
            print("No old app migrations found")

if __name__ == '__main__':
    check_migrations()