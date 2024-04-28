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

        try:
            profile = Profile.objects.get(user=request.user)
            if profile.role == Profile.Role.PENJUAL:
                return function(request, *args, **kwargs)
            else:
                return render(request, '403.html', {})

        except Profile.DoesNotExist:
            return HttpResponseRedirect(reverse('user-profile:create-profile'))

    return wrapper


def pembeli_only(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user-profile:login'))

        try:
            profile = Profile.objects.get(user=request.user)
            if profile.role == Profile.Role.PEMBELI:
                return function(request, *args, **kwargs)
            else:
                return render(request, '403.html', {})

        except Profile.DoesNotExist:
            return HttpResponseRedirect(reverse('user-profile:create-profile'))

    return wrapper


