from functools import wraps

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import redirect_to_login
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


def has_profile_only(function=None, user_role=None,
                     create_profile_url='user-profile:create-profile',
                     redirect_field_name=REDIRECT_FIELD_NAME):
    def auth(u):
        if not u.is_authenticated:
            return False

        profile = Profile.objects.get(user=u)

        return profile.role == Profile.Role.PENJUAL or profile.role == Profile.Role.PEMBELI

    actual_decorator = user_passes_test(
        auth,
        login_url=create_profile_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
