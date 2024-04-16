from django.shortcuts import render
from keranjang.models import ItemKeranjang

def show_main(request):
    cart = ItemKeranjang.objects.filter(user=request.user)

    context = {
        'cart': cart,
    }

    return render(request, "main.html", context)

def add_food_to_cart(request, food_id):
    ItemKeranjang(user=request.user, makanan=food_id, jumlah=1).save()

    return

def remove_food_from_cart(request, id):
    ItemKeranjang.objects.get(pk = id).delete()

    return 

def checkout_cart(request, checkedout_foods):
    # checkedout_foods =                          # gimana cara dapatin semua id makanan2 yg di-checkout
    
    return
