from django.shortcuts import render
from keranjang.models import ItemKeranjang
from .models import Order
from user_profile.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from toko.models import Toko


def show_main_penjual(request):
    foods = Order.objects.filter()

    total_harga = 0
    for i in foods:
        total_harga += i.makanan.harga

    context = {
        'orderID' : order_id_generator,
        #'foods' : foods,
        'status' : Order.status,
        'harga' : total_harga,
        'jumlah_pesanan' : ItemKeranjang.jumlah
    }

    return render(request, "penjual.html", context)

def show_main_pembeli(request):
    foods = Order.objects.filter(user=request.user)

    total_harga = 0
    for i in foods:
        total_harga += i.makanan.harga

    context = {
        'orderID' : order_id_generator,
        'foods' : foods,
        'status' : Order.status,
        'harga' : total_harga,
        'jumlah_pesanan' : Order.quantity,
    }

    return render(request, "pembeli.html", context)

def order_id_generator(request):
    orderID = request.user.username.upper()[:5] + Toko.name.upper()[:5]
    date_added = Order.date_added.split()
    date = date_added[0][:11]
    orderID += date.replace("-", "")
    checksum = 0
    for i in orderID:
        checksum += ord(i)

    orderID += (checksum % 10)
    return orderID

def edit_status_penjual(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, orderID=order_id)
        order.status = Order.StatusPesanan.DIPROSES
        order.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def edit_status_selesai(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, orderID=order_id)
        order.status = Order.StatusPesanan.SELESAI
        order.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def edit_status_batal(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, orderID=order_id)
        order.status = Order.StatusPesanan.DIBATALKAN
        order.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})