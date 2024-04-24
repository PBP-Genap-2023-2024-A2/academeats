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
    }

    return render(request, "penjual.html", context)

def show_main_pembeli(request):
    orders = Order.objects.all()
    order_group = OrderGroup.objects.all()
    order_list = []

    for og in order_group:
        o = orders.filter(order_group = og)

        order_list.append({'pk': og.pk, 'total_harga': og.total_harga, 'orders': o, 'status': aggregat_status(o)})

    context = {
        'order_group': order_list,
    }
    print(order_list)

    return render(request, "pembeli.html", context)

def order_id_generator(og):
    orderID = og.user.username.upper()[:5] + og.toko.name.upper()[:5]  # ???
    date_added = og.date_added.split()
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

        if (order.status == "DIBATALKAN"):
            return HttpResponse(400)

        order_status = request.POST.get('order_status')
        order.status = getattr(Order.StatusPesanan, order_status)
        order.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def edit_status_batal(request, og_id):
    order_group = OrderGroup.objects.get(pk=og_id)
    orders = Order.objects.filter(order_group=order_group)

    for order in orders:
        order.status = Order.StatusPesanan.DIBATALKAN
        order.save()

    return HttpResponse(status=200)


# HELPER FUNCTION
def aggregat_status(orders):
    statuses = []
    status = ""

    for order in orders:
        statuses.append(order.status)

    for s in statuses:
        if s == "DIBATALKAN":
            status = "DIBATALKAN"
            break
        elif s == "DIPESAN" or s == "DIPROSES":
            status = "DIPROSES"
            break
    else:
        status = "SELESAI"
    return status