from django.shortcuts import render
from keranjang.models import ItemKeranjang
from .models import Order, OrderGroup
from user_profile.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from toko.models import Toko
from makanan.models import Makanan


def show_main_penjual(request, toko_id):
    toko = Toko.objects.get(pk=toko_id)
    orders = Order.objects.filter(toko=toko)

    pesanan_cnt = 0
    for order in orders:
        pesanan_cnt += 1

    context = {
        'orders': orders,
        'jumlah_pesanan': pesanan_cnt,
    }

    return render(request, "penjual.html", context)


def show_main_pembeli(request):
    orders = Order.objects.filter(user=request.user)
    order_group = OrderGroup.objects.filter(user=request.user)
    order_list = []

    for og in order_list:
        order_list.append(orders.filter(order_group = og))

    for og in order_group:
        total_harga = 0
        pesanan_cnt = 0
        for order in og:
            total_harga += order.makanan.harga * order.quantity
            pesanan_cnt += 1

    context = {
        'harga_total': total_harga,
        'jumlah_pesanan': pesanan_cnt,
        'order_group': order_list,
    }

    return render(request, "pembeli.html", context)


def order_id_generator(order):
    orderID = order.user.username.upper()[:5] + order.toko.name.upper()[:5]  # ???
    date_added = order.date_added.split()
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

def update_status_batal(request, order_id):
    orders = Order.objects.filter(user=request.user)
    order_group = OrderGroup.objects.filter(user=request.user)
    order_list = []

    for og in order_group:
        order_list.append(orders.filter(order_group = og))

    #for og in order_group:
    #    for order in og:
    #        if order.status == Order.StatusPesanan.DIBATALKAN

