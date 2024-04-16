from django.shortcuts import render, redirect
from django.urls import reverse
from review.forms import ReviewForm, ReplyForm
from review.models import Review, Order
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.

def create_review(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return render(request, "error.html", {"message": "Order does not exist."})
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        review = form.instance
        review.order = order
        review.save()
        return redirect(reverse('review:show_review'), args=[order_id])

    context = {'form': form}
    return render(request, "create_review.html", context)

def show_review(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return render(request, "error.html", {"message": "Order does not exist."})
    reviews = Review.objects.filter(order=order)
    context = {
        'reviews': reviews,
        'order': order
    }
    return render(request, "main.html", context)

def reply_review(request, id):
    progress = Review.objects.get(pk = id)
    form = ReplyForm(request.POST or None, instance=progress)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('review:show_review'))
    context = {'form': form}
    return render(request, "reply_review.html", context)