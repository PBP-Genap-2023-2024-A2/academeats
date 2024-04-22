from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse

from makanan.forms import MakananForm
from makanan.models import Makanan, Kategori
from toko.forms import TokoForm
from toko.models import Toko
from user_profile.models import Profile


def manage_toko(request):
    toko = Toko.objects.filter(user=request.user)

    return render(request, 'manage.html', {'toko': toko})


def info_toko(request, toko_id):
    toko = Toko.objects.get(pk=toko_id)
    menu = Makanan.objects.filter(toko=toko)

    context = {'toko': toko, 'menu': menu}

    print(toko.description)

    return render(request, 'info_toko.html', context)


def create_toko(request):
    form = TokoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        toko = form.save(commit=False)
        toko.user = request.user
        toko.save()
        return redirect('toko:manage')

    context = {'form': form}
    return render(request, 'create_toko.html', context)


def edit_toko(request, toko_id):
    toko = Toko.objects.get(pk=toko_id)
    form = TokoForm(request.POST or None, instance=toko)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:index'))

    context = {'form': form}
    return render(request, "edit_toko.html", context)


def tambah_makanan(request, toko_id):
    toko = Toko.objects.get(pk=toko_id)
    form = MakananForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        makanan = form.save(commit=False)

        makanan.toko = toko
        makanan.kategori = Kategori.objects.get(pk=int(form.cleaned_data.get("kategori")))
        makanan.save()
        return redirect('toko:info_toko', toko_id=toko_id)

    context = {
        'form': form
    }

    return render(request, 'tambah_makanan.html', context)
