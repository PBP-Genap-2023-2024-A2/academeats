from django.shortcuts import render

from user_profile.models import Profile
from utils.decorators import penjual_only, pembeli_only

def index(request):
    return render(request, 'index.html', {})


def not_found(request):
    return render(request, '404.html', {})
