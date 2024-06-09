from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from makanan.models import Makanan
from review.models import Review
from serializers.makanan_serializers import MakananSerializer
from toko.models import Toko
from makanan.forms import MakananForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from utils.decorators import has_profile_only, penjual_only


def home(request):
    makanan = Makanan.objects.all()

    paginator = Paginator(makanan, 15)

    page_number = request.GET.get("page") or 1
    items = paginator.get_page(page_number)

    top_makanan = makanan[:3]

    context = {
        'items': items,
        'top_makanan': top_makanan,
    }

    return render(request, 'home-page.html', context)


def detail_makanan(request, makanan_id):
    makanan = Makanan.objects.get(pk=makanan_id)
    reviews = Review.objects.filter(makanan=makanan)
    is_penjual = False

    try:
        pass
        # toko = Toko.objects.get(user=request.user)
        # if toko == makanan.toko:
        #     is_penjual = True
    except Toko.DoesNotExist:
        pass

    rating = 0
    count = 0

    for review in reviews:
        rating += review.nilai
        count += 1

    if count != 0:
        rating /= count

    context = {
        'makanan': makanan,
        'reviews': reviews,
        'rating': rating,
        'count': count,
        'is_penjual': is_penjual,
    }

    return render(request, "makanan-detail.html", context)


@csrf_exempt
def get_stok(request):
    makanan = Makanan.objects.get(pk=request.GET.get('makanan_id'))
    return render(request, 'get_stok.html', {'makanan': makanan})


@csrf_exempt
def show_makanan(request):
    makanan = Makanan.objects.all()

    context = {
        'name': request.user.username,
        'makanan': makanan

    }

    return render(request, 'main_makanan.html', context)


@csrf_exempt
def delete_makanan(request, makanan_id):
    try:
        makanan = Makanan.objects.get(pk=makanan_id)
        makanan.delete()
    except:
        return HttpResponseNotFound
    return HttpResponseRedirect(reverse('main:index'))


@penjual_only
def edit_makanan(request, makanan_id):
    makanan = Makanan.objects.get(pk=makanan_id)

    form = MakananForm(request.POST or None, instance=makanan)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('makanan:detail', args=[makanan.id]))

    context = {'form': form}
    return render(request, "edit_makanan.html", context)


# TES
def tes_get_all_makanan(request):
    makanan = Makanan.objects.all()

    return JsonResponse(MakananSerializer(makanan, many=True).data, status=200, safe=False)
