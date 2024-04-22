from django.shortcuts import render, redirect
from makanan.models import Makanan
from toko.models import Toko
from makanan.forms import MakananForm


def detail_makanan(request, makanan_id):
    makanan = Makanan.objects.get(pk=makanan_id)

    return render(request, "detail_makanan.html", {'makanan': makanan})

def get_stok(request):
    makanan = Makanan.objects.get(pk=request.GET.get('makanan_id'))
    return render(request, 'get_stok.html', {'makanan': makanan})
