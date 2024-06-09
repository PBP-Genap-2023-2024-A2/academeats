from django.shortcuts import render

from utils.decorators import penjual_only, pembeli_only

def index(request):
    # user = request.user
    # if user.is_authenticated:
    #     if (user.profile.role == 'penjual'):
    #         return render(request, 'index_penjual.html', {'user' : user})
    #     return render(request, 'index_pembeli.html', {'user' : user})
    # return render(request, 'index.html', {})
    return render(request, 'index.html', {})
    
def not_found(request):
    return render(request, '404.html', {})
