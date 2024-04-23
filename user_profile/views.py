from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from user_profile.models import Profile
from user_profile.forms import ProfileForm, SignUpForm


# Fungsi untuk melakukan register user
# Return: HttpResponse
def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(request, user)

            return HttpResponseRedirect(reverse('user-profile:create-profile'))

        messages.error(request, form.errors)

    return render(request, 'register.html')


@login_required(login_url='login')
def create_profile(request):

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            profile = form.save(commit=False)
            request.user.profile = profile
            request.user.save()

            return HttpResponseRedirect(reverse('user_profile:login'))

        messages.error(request, form.errors)

    return render(request, 'create_profile.html')


# Fungsi untuk melakukan login user
# Return: HttpResponse
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:

            if user.profile is None:
                return HttpResponseRedirect(reverse('user-profile:create-profile'))

            login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
        else:
            messages.error(request, 'Sorry, incorrect username or password.')

    return render(request, 'login.html', {})


# Fungsi untuk melakukan logout user
# Return: HttpResponse
def logout_user(request):
    logout(request)
    return redirect('main:index')


# Fungsi untuk mendapatkan profile dari user sesuai user id yang diminta
# Return: profile user dalam bentuk html
@login_required(login_url='login')
def profile_page(request, username):

    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    return render(request, 'profile.html', context={'profile': profile})


def edit_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()

            return HttpResponseRedirect(reverse('user-profile:profile', args=[username]))
        
        return HttpResponseRedirect(reverse('user-profile:profile', args=[username]))
        
    

    return render(request, 'edit_profile.html', context={'profile': profile, 'user': user})

def show_json_saldo(request):
    data_saldo = request.user.profile.saldo
    return JsonResponse({'saldo': data_saldo})

def top_up(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        jumlah = request.POST.get('jumlah')
        jumlah = jumlah.replace('.', '') 
        profile.saldo += (int(jumlah) - 1000)
        profile.save()

        return HttpResponseRedirect(reverse('user-profile:profile', args=[username]))

    return render(request, 'top_up.html', context={'profile': profile, 'user': user})

# WARNING!! FOR DEVELOPMENT PURPOSE ONLY!
def delete_acc(request, username):
    try:
        u = User.objects.get(username=username)
        u.delete()

    except User.DoesNotExist:
        pass

    return redirect('user-profile:register')
