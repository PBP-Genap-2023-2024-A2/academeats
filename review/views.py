from django.shortcuts import render, redirect
from review.forms import ReviewForm
from review.models import Review
# Create your views here.

def create_review(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_review.html", context)

def show_review(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }

    return render(request, "main.html", context)