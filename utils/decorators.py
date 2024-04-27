from functools import wraps

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user_profile.models import Profile


def penjual_only(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user-profile:login'))

        profile = request.user.profile
        if profile.role == Profile.Role.PENJUAL:
            return function(request, *args, **kwargs)
        else:
            return render(request, '403.html', {})

    return wrapper


def pembeli_only(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user-profile:login'))

        profile = request.user.profile
        if profile.role == Profile.Role.PEMBELI:
            return function(request, *args, **kwargs)
        else:
            return render(request, '403.html', {})

    return wrapper
