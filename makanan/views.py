import json

from django.core import serializers
from django.http import HttpResponseNotFound, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from makanan.models import Makanan
from review.models import Review
from toko.models import Toko
from makanan.forms import MakananForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from utils.decorators import has_profile_only, penjual_only


@has_profile_only
def detail_makanan(request, makanan_id):
    makanan = Makanan.objects.get(pk=makanan_id)
    reviews = Review.objects.filter(makanan=makanan)
    user = request.user
    profile = user.profile
    is_penjual = False

    try:
        toko = Toko.objects.get(user=request.user)
        if toko == makanan.toko:
            is_penjual = True
    except Toko.DoesNotExist:
        pass

    rating = 0
    count = 0

    for review in reviews:
        rating += review.nilai
        count += 1

    if count != 0:
        rating /= count

    context = {
        'makanan': makanan,
        'reviews': reviews,
        'rating': rating,
        'count': count,
        'is_penjual': is_penjual,
        'profile': profile,
    }

    return render(request, "detail_makanan.html", context)

def detail_makanan_json(request, makanan_id):
    makanan = Makanan.objects.get(pk=makanan_id)
    reviews = Review.objects.filter(makanan=makanan)
    user = request.user
    profile = user.profile
    is_penjual = False

    try:
        toko = Toko.objects.get(user=request.user)
        if toko == makanan.toko:
            is_penjual = True
    except Toko.DoesNotExist:
        pass

    rating = 0
    count = 0

    for review in reviews:
        rating += review.nilai
        count += 1

    if count != 0:
        rating /= count

    context = {
        'nama_makanan': makanan.nama,
        'reviews': rating,
        'harga_makanan': makanan.harga,
        'stok': makanan.stok,


    }

    return JsonResponse(context)

def detail_review_makanan_json(request, makanan_id):
    try:
       makanan_dipilih = Makanan.objects.get(pk=makanan_id)
    except Makanan.DoesNotExist:
        return render(request, "error.html", {"message": "Makanan does not exist."})
    reviews = Review.objects.filter(makanan=makanan_dipilih)
    context = {
        'reviews': [],
        'makanan': makanan_dipilih.nama
    }

    for review in reviews:
        context['reviews'].append({
            'rating': review.nilai
        })
    return JsonResponse(context)





@csrf_exempt
def get_stok(request):
    makanan = Makanan.objects.get(pk=request.GET.get('makanan_id'))
    return render(request, 'get_stok.html', {'makanan': makanan})


@csrf_exempt
def show_makanan(request):
    makanan = Makanan.objects.all()

    context = {
        'name': request.user.username,
        'makanan': makanan

    }

    return render(request, 'main_makanan.html', context)


@csrf_exempt
def delete_makanan(request, makanan_id):
    try:
        makanan = Makanan.objects.get(pk=makanan_id)
        makanan.delete()
    except:
        return HttpResponseNotFound
    return HttpResponseRedirect(reverse('main:index'))


@penjual_only
def edit_makanan(request, makanan_id):
    makanan = Makanan.objects.get(pk=makanan_id)

    form = MakananForm(request.POST or None, instance=makanan)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('makanan:detail', args=[makanan.id]))

    context = {'form': form}
    return render(request, "edit_makanan.html", context)


