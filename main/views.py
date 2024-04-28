from django.shortcuts import render

from user_profile.models import Profile
from utils.decorators import penjual_only, pembeli_only
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user
    if (user.profile.role == 'penjual'):
        return render(request, 'index_penjual.html', {'user' : user})
    return render(request, 'index_pembeli.html', {'user' : user})


def not_found(request):
    return render(request, '404.html', {})
