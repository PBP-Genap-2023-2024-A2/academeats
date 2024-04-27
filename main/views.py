from django.shortcuts import render

from user_profile.models import Profile
from utils.decorators import penjual_only


@penjual_only
def index(request):
    return not_found(request)


def not_found(request):
    return render(request, '404.html', {})
