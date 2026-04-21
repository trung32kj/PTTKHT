from lich_hen.models import ThongBao


def thong_bao_context(request):
    """Context processor để hiển thị số thông báo chưa đọc trên navbar"""
    if request.user.is_authenticated:
        so_thong_bao = ThongBao.objects.filter(
            nguoi_nhan=request.user,
            da_doc=False
        ).count()
        thong_bao_moi = ThongBao.objects.filter(
            nguoi_nhan=request.user,
            da_doc=False
        )[:5]
        return {
            'so_thong_bao': so_thong_bao,
            'thong_bao_moi': thong_bao_moi,
        }
    return {}
