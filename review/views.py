from django.shortcuts import render, redirect
from django.urls import reverse
from review.forms import ReviewForm, ReplyForm
from review.models import Review, Order, Makanan
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.

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
        return redirect(reverse('review:show_review', args=[makanan_id]))

    context = {'form': form}
    return render(request, "create_review.html", context)

def show_review(request, makanan_id):
    try:
       makanan_dipilih = Makanan.objects.get(pk=makanan_id)
    except Makanan.DoesNotExist:
        return render(request, "error.html", {"message": "Toko does not exist."})
    reviews = Review.objects.filter(makanan=makanan_dipilih)
    context = {
        'reviews': reviews,
        'makanan': makanan_dipilih
    }
    return render(request, "main.html", context)


def reply_review(request, review_id):
    # Get review berdasarkan ID
    review = Review.objects.get(pk = review_id)

    # Set book sebagai instance dari form
    form = ReplyForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('review:show_review', args=[review.makanan.id]))

    context = {'form': form}
    return render(request, "reply_review.html", context)
    