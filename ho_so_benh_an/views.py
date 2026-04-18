from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import HoSoBenhAn, Thuoc, ToaThuoc
from lich_hen.models import LichHen
import json

@login_required
def tao_ho_so_benh_an(request, lich_hen_id):
    lich_hen = get_object_or_404(LichHen, id=lich_hen_id)
    
    if not hasattr(request.user, 'ho_so_bac_si') or lich_hen.bac_si != request.user.ho_so_bac_si:
        messages.error(request, 'Bạn không có quyền tạo hồ sơ này')
        return redirect('lich_hen_cua_toi')
    
    if request.method == 'POST':
        chan_doan = request.POST.get('diagnosis')
        ghi_chu = request.POST.get('notes', '')
        
        # Tạo hồ sơ bệnh án
        ho_so = HoSoBenhAn.objects.create(
            lich_hen=lich_hen,
            chan_doan=chan_doan,
            ghi_chu=ghi_chu
        )
        
        # Xử lý toa thuốc (JSON từ frontend)
        toa_thuoc_data = request.POST.get('toa_thuoc_json', '[]')
        
        # EMERGENCY DEBUG: Log everything for ID 13+ 
        with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
            f.write(f"\n=== EMERGENCY DEBUG HoSo ID {ho_so.id} ===\n")
            f.write(f"Time: {ho_so.ngay_tao}\n")
            f.write(f"All POST keys: {list(request.POST.keys())}\n")
            for key, value in request.POST.items():
                f.write(f"  {key}: '{value}'\n")
            f.write(f"toa_thuoc_json raw: '{toa_thuoc_data}'\n")
            f.write(f"toa_thuoc_json length: {len(toa_thuoc_data)}\n")
            f.write(f"toa_thuoc_json == '[]': {toa_thuoc_data == '[]'}\n")
            f.write(f"toa_thuoc_data.strip(): '{toa_thuoc_data.strip()}'\n")
        
        if toa_thuoc_data and toa_thuoc_data.strip() and toa_thuoc_data != '[]':
            try:
                toa_thuoc_list = json.loads(toa_thuoc_data)
                
                with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
                    f.write(f"✅ JSON parsed successfully: {toa_thuoc_list}\n")
                    f.write(f"Items count: {len(toa_thuoc_list)}\n")
                
                created_count = 0
                for i, item in enumerate(toa_thuoc_list):
                    ten_thuoc = item.get('ten_thuoc', '').strip()
                    so_luong_str = str(item.get('so_luong', '')).strip()
                    
                    with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
                        f.write(f"Item {i+1}: {item}\n")
                        f.write(f"  ten_thuoc: '{ten_thuoc}'\n")
                        f.write(f"  so_luong_str: '{so_luong_str}'\n")
                    
                    if ten_thuoc and so_luong_str:
                        try:
                            so_luong = int(so_luong_str)
                            if so_luong > 0:
                                # Tạo hoặc lấy thuốc
                                thuoc, created = Thuoc.objects.get_or_create(
                                    ten_thuoc=ten_thuoc,
                                    defaults={'don_vi': item.get('don_vi', 'viên')}
                                )
                                
                                # Tạo toa thuốc
                                toa_obj = ToaThuoc.objects.create(
                                    ho_so_benh_an=ho_so,
                                    thuoc=thuoc,
                                    so_luong=so_luong,
                                    ghi_chu=item.get('ghi_chu', '').strip()
                                )
                                created_count += 1
                                
                                with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
                                    f.write(f"  ✅ CREATED: {toa_obj} (ID: {toa_obj.id})\n")
                            else:
                                with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
                                    f.write(f"  ❌ Invalid quantity: {so_luong}\n")
                        except (ValueError, TypeError) as e:
                            with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
                                f.write(f"  ❌ Error converting quantity: {e}\n")
                    else:
                        with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
                            f.write(f"  ⏭️ Skipped - missing data\n")
                
                with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
                    f.write(f"FINAL RESULT: {created_count} prescriptions created\n")
                            
            except (json.JSONDecodeError, ValueError, TypeError) as e:
                with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
                    f.write(f"❌ JSON DECODE ERROR: {e}\n")
        else:
            with open('emergency_debug.txt', 'a', encoding='utf-8') as f:
                f.write(f"❌ NO PRESCRIPTION DATA OR EMPTY!\n")
                f.write(f"  Condition checks:\n")
                f.write(f"  - toa_thuoc_data: {bool(toa_thuoc_data)}\n")
                f.write(f"  - toa_thuoc_data.strip(): {bool(toa_thuoc_data.strip()) if toa_thuoc_data else 'N/A'}\n")
                f.write(f"  - != '[]': {toa_thuoc_data != '[]'}\n")
        
        lich_hen.trang_thai = 'completed'
        lich_hen.save()
        
        messages.success(request, 'Đã tạo hồ sơ bệnh án')
        return redirect('lich_hen_cua_toi')
    
    return render(request, 'ho_so_benh_an/tao_ho_so_benh_an.html', {'lich_hen': lich_hen})

@login_required
def lich_su_kham_benh(request):
    if hasattr(request.user, 'ho_so_benh_nhan'):
        ho_so_list = HoSoBenhAn.objects.filter(lich_hen__benh_nhan=request.user.ho_so_benh_nhan)
    elif hasattr(request.user, 'ho_so_bac_si'):
        ho_so_list = HoSoBenhAn.objects.filter(lich_hen__bac_si=request.user.ho_so_bac_si)
    else:
        ho_so_list = HoSoBenhAn.objects.all()
    
    return render(request, 'ho_so_benh_an/lich_su_kham_benh.html', {'ho_so_list': ho_so_list})

@login_required
def xem_ho_so_benh_an(request, ho_so_id):
    ho_so = get_object_or_404(HoSoBenhAn, id=ho_so_id)
    
    if hasattr(request.user, 'ho_so_benh_nhan'):
        if ho_so.lich_hen.benh_nhan != request.user.ho_so_benh_nhan:
            messages.error(request, 'Bạn không có quyền xem hồ sơ này')
            return redirect('lich_su_kham_benh')
    elif hasattr(request.user, 'ho_so_bac_si'):
        if ho_so.lich_hen.bac_si != request.user.ho_so_bac_si:
            messages.error(request, 'Bạn không có quyền xem hồ sơ này')
            return redirect('lich_su_kham_benh')
    
    return render(request, 'ho_so_benh_an/xem_ho_so_benh_an.html', {'ho_so': ho_so})
