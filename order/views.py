from django.shortcuts import render
from keranjang.models import ItemKeranjang
from .models import Order, OrderGroup
from user_profile.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from toko.models import Toko
from makanan.models import Makanan
from django.views.decorators.csrf import csrf_exempt

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
    orders = Order.objects.all()
    order_group = OrderGroup.objects.all()
    order_list = []

    for og in order_group:
        print(og)
        order_list.append(orders.filter(order_group = og))

    for ods in order_list:
        total_harga = 0
        pesanan_cnt = 0
        for od in ods:
            total_harga += od.makanan.harga * od.quantity
            pesanan_cnt += 1

    context = {
        'order_group': order_list,
    }
    print(order_list)

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


@csrf_exempt
def edit_status_penjual(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(pk=int(order_id))
        order_status = request.POST.get('order_status')
        order.status = getattr(Order.StatusPesanan, order_status)
        order.save()
        return JsonResponse({'status': 'success'})
    else:
        pass
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def edit_status_batal(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, orderID=order_id)
        order.status = Order.StatusPesanan.DIBATALKAN
        order.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def update_status_batal(request):
    if request.method == 'POST':
        order_group_id = request.POST.get("og_id")
        order_group = OrderGroup.objects.get(pk=int(order_group_id))
        orders = Order.objects.filter(order_group=order_group)

        for order in orders:
            order.status = Order.StatusPesanan.DIBATALKAN
            order.save()


def delete_order(request, order_id):
    order = Order.objects.get(order_id)

    print(order)

    order.delete()

    return HttpResponse('DELETED')