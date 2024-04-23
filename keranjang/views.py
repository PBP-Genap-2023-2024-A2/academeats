from django.core import serializers
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from keranjang.models import ItemKeranjang
from makanan.models import Makanan


def show_main(request):
    cart = ItemKeranjang.objects.all()

    print(cart)

    context = {
        'cart': cart,
    }

    return render(request, "home.html", context)


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

    ItemKeranjang.objects.get(pk=keranjang_id).delete()

    return HttpResponse(b"DELETED", status=200)


def cek_stok(request, keranjang_id):
    keranjang = ItemKeranjang.objects.get(pk=keranjang_id)
    stok = keranjang.makanan.stok
    return JsonResponse({'stok': stok})

@csrf_exempt
def checkout_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        checkedout_foods = data.get('checkedout_foods', [])

        # Sekarang Anda memiliki list dari semua id makanan yang di-checkout
        # Anda bisa menambahkan kode untuk memproses checkout di sini

        return JsonResponse({'message': 'Checkout successful'})

    return JsonResponse({'message': 'Invalid request'}, status=400)