from django.core import serializers
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from keranjang.models import ItemKeranjang
from makanan.models import Makanan
from order.models import OrderGroup, Order
from django.contrib.auth.decorators import login_required

from serializers.keranjang_seraializers import KeranjangSerializer
from user_profile.models import UserProfile
from utils.decorators import has_profile_only


def show_main(request):
    # cart = ItemKeranjang.objects.filter(user=request.user)
    cart = ItemKeranjang.objects.all()
    context = {
        'cart': cart,
    }

    return render(request, "keranjang.html", context)


@csrf_exempt
def get_item(request):
    items = ItemKeranjang.objects.filter(user=request.user)

    return HttpResponse(serializers.serialize('json', items), content_type='application/json')


@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        makanan_id = request.POST.get("makanan_id")
        makanan = Makanan.objects.get(pk=int(makanan_id))
        user = request.user

        try:
            item = ItemKeranjang.objects.get(makanan=makanan)

            if item.jumlah >= item.makanan.stok:
                return HttpResponse(status=400)

            item.jumlah = item.jumlah + 1
            item.save()
        except ItemKeranjang.DoesNotExist:
            new_item = ItemKeranjang(makanan=makanan, user=user)
            new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


@csrf_exempt
def delete_item(request, keranjang_id):

    ItemKeranjang.objects.get(pk=keranjang_id).delete()

    return HttpResponse(b"DELETED", status=200)


@csrf_exempt
def cek_stok(request, keranjang_id):
    keranjang = ItemKeranjang.objects.get(pk=keranjang_id)
    stok = keranjang.makanan.stok
    return JsonResponse({'stok': stok, 'message' : 'success'})


@csrf_exempt
def checkout_cart(request):
    if request.method == 'POST':
        ids = json.loads(request.POST.get('obj'))
        total_harga = request.POST.get('total')

        if total_harga == 0:
            return HttpResponse(status=400)

        order_group = OrderGroup(user=request.user, total_harga=total_harga)
        order_group.save()

        for item_id in ids:
            item = ItemKeranjang.objects.get(pk=int(item_id))

            if item.jumlah > item.makanan.stok:
                order_group.delete()
                return HttpResponse(400)

            order = Order(order_group=order_group, user=request.user, makanan=item.makanan, toko=item.makanan.toko, quantity=item.jumlah)
            order.save()

            item.makanan.stok -= item.jumlah
            item.makanan.save()

            item.delete()

        return JsonResponse({'message': 'Checkout successful'})

    return HttpResponseNotFound()


@csrf_exempt
def update_jumlah(request, keranjang_id):

    if request.method == "POST":
        keranjang = ItemKeranjang.objects.get(pk=keranjang_id)
        keranjang.jumlah = request.POST.get('jumlah')
        keranjang.save()

        return JsonResponse({'jumlah': keranjang.jumlah})

    return HttpResponseNotFound()


@csrf_exempt
def cek_jumlah_item(request):
    item_keranjang = ItemKeranjang.objects.filter(user=request.user)
    return HttpResponse(len(item_keranjang))

# * FOR FLUTTER ONLY!! * #

# * FLUTTER DEV API * #

@csrf_exempt
def get_users_cart_items(request, username):
    if request.method == "GET":
        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return HttpResponseBadRequest()

        keranjang_item = ItemKeranjang.objects.filter(user=user)

        return JsonResponse(KeranjangSerializer(keranjang_item, many=True).data, status=200, safe=False)
    return HttpResponseNotFound()

@csrf_exempt
def flutter_checkout_cart(request, username):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        ids = body['obj']
        total_harga = body['total_harga']
        print(ids)

        if total_harga == 0:
            return HttpResponse(status=400)

        user = UserProfile.objects.get(username=username)
        order_group = OrderGroup(user=user, total_harga=total_harga)
        order_group.save()

        for item_id in ids:
            item = ItemKeranjang.objects.get(pk=int(item_id))

            if item.jumlah > item.makanan.stok:
                order_group.delete()
                return HttpResponse(400)

            order = Order(order_group=order_group, user=user, makanan=item.makanan, toko=item.makanan.toko, quantity=item.jumlah)
            order.save()

            item.makanan.stok -= item.jumlah
            item.makanan.save()

            item.delete()

        return JsonResponse({'message': 'Checkout successful'})

    return HttpResponseNotFound()

@csrf_exempt
def flutter_update_jumlah(request, keranjang_id):
    if request.method == "POST":
        keranjang = ItemKeranjang.objects.get(pk=keranjang_id)

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        keranjang.jumlah = body['jumlah']
        keranjang.save()

        return JsonResponse({'jumlah': keranjang.jumlah, 'status': 'success'})

    return HttpResponseNotFound()

@csrf_exempt
def flutter_delete_item(request, keranjang_id):

    ItemKeranjang.objects.get(pk=keranjang_id).delete()

    return JsonResponse({'message': 'success'})
