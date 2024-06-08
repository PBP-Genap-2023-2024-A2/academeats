import environ
import requests
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from makanan.forms import MakananForm
from makanan.models import Makanan
from serializers.toko_serializers import TokoSerializer
from toko.forms import TokoForm
from toko.models import Toko
from utils.decorators import penjual_only, pembeli_only


@penjual_only
def manage_toko(request, toko_id=-1):
    toko = Toko.objects.filter(user=request.user)
    if(toko_id == -1):
        return render(request, 'manage.html', {'toko': toko})
    return render(request, 'manage_toko.html', {'toko': toko})


@pembeli_only
def show_toko(request):
    toko = Toko.objects.all()
    context = {'toko': toko}
    return render(request, 'show_toko.html', context)



@pembeli_only
def info_toko(request, toko_id):
    toko = Toko.objects.get(pk=toko_id)
    menu = Makanan.objects.filter(toko=toko)

    context = {'toko': toko, 'menu': menu}

    print(toko.description)

    return render(request, 'info_toko.html', context)


@penjual_only
def create_toko(request):
    form = TokoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        toko = form.save(commit=False)
        toko.user = request.user
        toko.save()
        return redirect('toko:manage')

    context = {'form': form}
    return render(request, 'create_toko.html', context)


@penjual_only
def edit_toko(request, toko_id):
    toko = Toko.objects.get(pk=toko_id)
    form = TokoForm(request.POST or None, instance=toko)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:index'))

    context = {'form': form}
    return render(request, "edit_toko.html", context)


@penjual_only
def tambah_makanan(request, toko_id):
    toko = Toko.objects.get(pk=toko_id)

    if request.method == "POST":
        form = MakananForm(request.POST, request.FILES)

        if form.is_valid():
            makanan = form.save(commit=False)

            img_file = request.FILES['img_file']

            env = environ.Env()

            key = "6d207e02198a847aa98d0a2a901485a5"
            uri = "https://freeimage.host/api/1/upload"

            res = requests.request("POST", uri + '?key=' + key,
                                   files={'source': img_file})

            img_url = res.json()['image']['url']

            makanan.toko = toko
            makanan.img_url = img_url
            makanan.save()

            return redirect('toko:info_toko', toko_id=toko_id)
    else:
        form = MakananForm()

    context = {
        'form': form
    }

    return render(request, 'tambah_makanan.html', context)


# * FOR FLUTTER ONLY!! * #

# * FLUTTER DEV API * #

@csrf_exempt
def flutter_get_all_toko(request):

    if request.method == "GET":
        toko = Toko.objects.all()

        return JsonResponse(TokoSerializer(toko, many=True).data, status=200, safe=False)

    return HttpResponseNotFound()


@csrf_exempt
def flutter_get_toko_by_id(request, id):

    if request.method == "GET":
        toko = Toko.objects.get(pk=id)

        return JsonResponse(TokoSerializer(toko).data, status=200)

    return HttpResponseNotFound()
