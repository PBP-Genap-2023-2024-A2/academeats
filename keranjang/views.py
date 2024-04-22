from django.core import serializers
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from keranjang.models import ItemKeranjang
from makanan.models import Makanan


def show_main(request):
    cart = ItemKeranjang.objects.filter(user=request.user)

    context = {
        'cart': cart,
    }

    return render(request, "main.html", context)


def get_item(request):
    items = ItemKeranjang.objects.filter(user=request.user)

    return HttpResponse(serializers.serialize('json', items), content_type='application/json')


@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        makanan_id = request.POST.get("makanan_id")
        makanan = Makanan.objects.get(pk=int(makanan_id))
        user = request.user

        new_item = ItemKeranjang(makanan=makanan, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


@csrf_exempt
def delete_item(request, keranjang_id):

    if request.method == 'DELETE':
        ItemKeranjang.objects.get(pk=keranjang_id).delete()

        return HttpResponse(b"DELETED", status=200)

    return HttpResponseNotFound()




def checkout_cart(request, checkedout_foods):
    # checkedout_foods =                          # gimana cara dapatin semua id makanan2 yg di-checkout

    return
