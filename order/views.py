from django.shortcuts import render
from keranjang.models import ItemKeranjang, Keranjang
from .models import Order
from user_profile.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from toko.models import Toko
from makanan.models import Makanan

def show_main_penjual(request):
    orders = Order.objects.filter(toko = request.user.toko)

    for order in orders:
        total_harga = 0
        pesanan_cnt = 0
        orderID = order_id_generator(order)
        foods = Makanan.objects.filter(order = order) # apa makanan perlu tambahin model order ya...
        for food in foods:
            nama_makanan = food.nama
            harga_makanan = food.harga
            total_harga += food.harga
            pesanan_cnt += 1
        status = order.status
        harga_total = total_harga
        jumlah_pesanan = pesanan_cnt

    context = {
        'orderID' : orderID,
        'nama_makanan' : nama_makanan,
        'harga_makanan' : harga_makanan,
        'status' : status,
        'harga_total' : total_harga,
        'jumlah_pesanan' : pesanan_cnt,
    }

    return render(request, "penjual.html", context)

def show_main_pembeli(request):
    orders = Order.objects.filter(user = request.user)

    for order in orders:
        total_harga = 0
        pesanan_cnt = 0
        orderID = order_id_generator(order)
        foods = Makanan.objects.filter(order = order) # apa makanan perlu tambahin model order ya...
        for food in foods:
            nama_makanan = food.nama
            harga_makanan = food.harga
            total_harga += food.harga
            pesanan_cnt += 1
        status = order.status
        harga_total = total_harga
        jumlah_pesanan = pesanan_cnt

    context = {
        'orderID' : orderID,
        'nama_makanan' : nama_makanan,
        'harga_makanan' : harga_makanan,
        'status' : status,
        'harga_total' : total_harga,
        'jumlah_pesanan' : pesanan_cnt,
    }

    return render(request, "pembeli.html", context)

def order_id_generator(order):
    orderID = order.user.username.upper()[:5] + order.toko.name.upper()[:5] #???
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