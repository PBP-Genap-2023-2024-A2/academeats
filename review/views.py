import json
from django.shortcuts import render, redirect
from django.urls import reverse
from review.forms import ReviewForm, ReplyForm
from review.models import Review, Order, Makanan, User
from toko.models import Toko
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from utils.decorators import penjual_only, pembeli_only


# Create your views here.

@pembeli_only
def create_review(request, makanan_id):
    try:
        makanan_dipilih = Makanan.objects.get(pk=makanan_id)
    except Makanan.DoesNotExist:
        return render(request, "error.html", {"message": "Order does not exist."})
    try:
        form = ReviewForm(request.POST or None)
    except Review.DoesNotExist:
        form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        review = form.save(commit=False)
        review.makanan = makanan_dipilih
        review.save()
        if request.user.profile.role == 'penjual':
            return redirect(reverse('review:show_review_penjual', args=[makanan_id]))
        return redirect(reverse('review:show_review_pembeli', args=[makanan_id]))

    context = {'form': form}
    return render(request, "create_review.html", context)

def create_review_JSON(request, makanan_id):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_review = Review.objects.create(
            user = request.user,
            makanan = Makanan.objects.get(pk=makanan_id),
            komentar = data["komentar"],
            nilai = int(data["nilai"]),
            reply = data["reply"]
        )
        new_review.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@penjual_only
def show_review_penjual(request, makanan_id):
    try:
        makanan_dipilih = Makanan.objects.get(pk=makanan_id)
    except Makanan.DoesNotExist:
        return render(request, "error.html", {"message": "Makanan does not exist."})
    toko_dipilih = Toko.objects.filter(user=request.user)
    for toko in toko_dipilih:
        if toko == makanan_dipilih.toko:
            break
    else:
        return render(request, "403.html", {})
    
    reviews = Review.objects.filter(makanan=makanan_dipilih)
    context = {
        'reviews': reviews,
        'makanan': makanan_dipilih,
        'toko': toko_dipilih
    }
    return render(request, "main.html", context)

@pembeli_only
def show_review_pembeli(request, makanan_id):
    try:
       makanan_dipilih = Makanan.objects.get(pk=makanan_id)
    except Makanan.DoesNotExist:
        return render(request, "error.html", {"message": "Makanan does not exist."})
    reviews = Review.objects.filter(makanan=makanan_dipilih)
    context = {
        'reviews': reviews,
        'makanan': makanan_dipilih
    }
    return render(request, "main.html", context)

def show_review_JSON(request, makanan_id):
    try:
        makanan_dipilih = Makanan.objects.get(pk=makanan_id)
    except Makanan.DoesNotExist:
        return render(request, "error.html", {"message": "Toko does not exist."})
    reviews = Review.objects.filter(makanan=makanan_dipilih)
    reviews_list = list(reviews.values())
    makanan_dict = model_to_dict(makanan_dipilih)
    context = {
        'reviews': reviews_list,
        'makanan': makanan_dict
    }
    return JsonResponse(context)

@penjual_only
def reply_review(request, review_id):
    # Get review berdasarkan ID
    review = Review.objects.get(pk = review_id)

    # Set book sebagai instance dari form
    form = ReplyForm(request.POST or None, instance=review)
    user = request.user
    toko = Toko.objects.get(user=user)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('review:show_review_penjual', args=[review.makanan.id]))

    context = {
                'form': form,
                'toko': toko
                }
    return render(request, "reply_review.html", context)



def reply_review_JSON(request, review_id):
    # Get review berdasarkan ID
    review = Review.objects.get(pk = review_id)

    # Set review sebagai instance dari form
    form = ReplyForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('review:show_review_JSON', args=[review.makanan.id]))

    context = {
                'form': form
                }
    return JsonResponse(context)