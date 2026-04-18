#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quan_ly_phong_kham.settings')
sys.path.append('.')
django.setup()

from django.db import connection

def check_tables():
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Current tables in database:")
        for table in tables:
            print(f"  - {table[0]}")
        
        print("\nChecking for old vs new table names:")
        old_tables = [t[0] for t in tables if t[0].startswith('accounts_')]
        new_tables = [t[0] for t in tables if t[0].startswith('tai_khoan_')]
        
        print(f"Old tables (accounts_*): {len(old_tables)}")
        for table in old_tables:
            print(f"  - {table}")
            
        print(f"New tables (tai_khoan_*): {len(new_tables)}")
        for table in new_tables:
            print(f"  - {table}")

if __name__ == '__main__':
    check_tables()