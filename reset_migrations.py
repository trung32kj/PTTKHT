#!/usr/bin/env python
"""
Reset migrations sau khi đổi tên thư mục
"""

import os
import shutil

def xoa_migrations_cu():
    """Xóa tất cả migrations cũ"""
    
    print("🗑️  XÓA MIGRATIONS CŨ...")
    
    thu_muc_apps = [
        'tai_khoan',
        'hop_thoai_ai',
        'lich_hen',
        'bang_dieu_khien', 
        'ho_so_benh_an'
    ]
    
    for app in thu_muc_apps:
        migrations_dir = f"{app}/migrations"
        
        if os.path.exists(migrations_dir):
            # Xóa tất cả file .py trừ __init__.py
            for file in os.listdir(migrations_dir):
                if file.endswith('.py') and file != '__init__.py':
                    file_path = os.path.join(migrations_dir, file)
                    try:
                        os.remove(file_path)
                        print(f"   ✅ Xóa {file_path}")
                    except Exception as e:
                        print(f"   ❌ Lỗi xóa {file_path}: {e}")
                
                # Xóa __pycache__
                pycache_dir = os.path.join(migrations_dir, '__pycache__')
                if os.path.exists(pycache_dir):
                    try:
                        shutil.rmtree(pycache_dir)
                        print(f"   ✅ Xóa {pycache_dir}")
                    except Exception as e:
                        print(f"   ❌ Lỗi xóa {pycache_dir}: {e}")

def main():
    """Chạy tất cả"""
    
    print("🔄 RESET MIGRATIONS")
    print("=" * 30)
    
    try:
        xoa_migrations_cu()
        
        print("\n" + "=" * 30)
        print("✅ HOÀN THÀNH!")
        print("🚀 Chạy tiếp:")
        print("   python manage.py makemigrations")
        print("   python manage.py migrate")
        print("=" * 30)
        
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")

if __name__ == '__main__':
    main()