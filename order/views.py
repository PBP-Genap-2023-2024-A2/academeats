from django.shortcuts import render
from keranjang.models import ItemKeranjang
from utils.decorators import penjual_only, pembeli_only
from .models import Order, OrderGroup
from user_profile.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from toko.models import Toko
from makanan.models import Makanan
from django.views.decorators.csrf import csrf_exempt


@penjual_only
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
    
def show_main_penjual_json(request, toko_id):
    toko = Toko.objects.get(pk=toko_id)
    orders = Order.objects.filter(toko=toko)

    pesanan_cnt = 0
    for order in orders:
        pesanan_cnt += 1

    orders_list = []
    for order in orders:
        orders_list.append({'food_name': order.makanan.nama, 'quantity': order.quantity, 'status': order.status, 'id': order.pk})

    # nanti yang direturn (order_list) jadinya gini: [{order}, {order}, ...]
    context = {
        'orders': orders_list,
    }

    return JsonResponse(context)

@pembeli_only
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

def show_main_pembeli_json(request):
    orders = Order.objects.all()
    order_group = OrderGroup.objects.all()

    # yang direturn jadi gini: [{'pk': og.pk, 'total_harga': og.total_harga, 'status': aggregat_status(o), orders: [{order}, {order}, {order}, ...]}, ...]
    order_groups = []
    for og in order_group:
        og_dict = {}
        orders = orders.filter(order_group = og)
        og_dict['pk'] = og.pk
        og_dict['total_harga'] = og.total_harga
        og_dict['status'] = aggregat_status(orders)

        orders_list = []
        for o in orders:
            orders_list.append({'food_name': o.makanan.nama, 'quantity': o.quantity, 'status': o.status, 'id': o.pk})
        og_dict['orders'] = orders_list
        order_groups.append(og_dict)

        context = {
            'order_groups': order_groups,
        }
        print(context)

    return JsonResponse(context)

# def order_id_generator(og):
#     orderID = og.user.username.upper()[:5] + og.toko.name.upper()[:5]  # ???
#     date_added = og.date_added.split()
#     date = date_added[0][:11]
#     orderID += date.replace("-", "")
#     checksum = 0
#     for i in orderID:
#         checksum += ord(i)
#
#     orderID += (checksum % 10)
#     return orderID

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