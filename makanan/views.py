from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from makanan.models import Makanan
from toko.models import Toko
from makanan.forms import MakananForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def detail_makanan(request, makanan_id):
    makanan = Makanan.objects.get(pk=makanan_id)

    return render(request, "detail_makanan.html", {'makanan': makanan})


def get_stok(request):
    makanan = Makanan.objects.get(pk=request.GET.get('makanan_id'))
    return render(request, 'get_stok.html', {'makanan': makanan})


def show_makanan(request):
    makanan = Makanan.objects.all()

    context = {
        'name': request.user.username,
        'makanan': makanan

    }

    return render(request, 'main_makanan.html', context)


def delete_makanan(request, makanan_id):
    makanan = Makanan.objects.get(pk=makanan_id)
    makanan.delete()
    return HttpResponseRedirect(reverse('main:index'))


def edit_makanan(request, makanan_id):
    makanan = Makanan.objects.get(pk=makanan_id)

    form = MakananForm(request.POST or None, instance=makanan)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:index'))

    context = {'form': form}
    return render(request, "edit_makanan.html", context)
