from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from serializers.user_profile_serializers import UserSerializer
from user_profile.forms import DaftarForm
from user_profile.models import UserProfile


# Fungsi untuk melakukan register user
# Return: HttpResponse
def register(request):

    if request.method == 'POST':
        form = DaftarForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(request, user)

            return HttpResponseRedirect(reverse('user-profile:create-profile'))

        messages.error(request, form.errors)

    return render(request, 'register.html')


@login_required(login_url='login')
def create_profile(request):
    pass

    # if request.method == "POST":
    #     form = ProfileForm(request.POST, instance=request.user.profile)
    #
    #     if form.is_valid():
    #         profile = form.save(commit=False)
    #         request.user.profile = profile
    #         request.user.save()
    #
    #         return HttpResponseRedirect(reverse('user_profile:login'))
    #
    #     messages.error(request, form.errors)
    #
    # return render(request, 'create_profile.html')


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
    # profile = Profile.objects.get(user=user)
    #
    # return render(request, 'profile.html', context={'profile': profile})


def edit_profile(request, username):
    pass
    # user = User.objects.get(username=username)
    # # profile = Profile.objects.get(user=user)
    #
    # if request.method == "POST":
    #     form = ProfileForm(request.POST, instance=profile)
    #
    #     if form.is_valid():
    #         profile = form.save(commit=False)
    #         profile.save()
    #
    #         return HttpResponseRedirect(reverse('user-profile:profile', args=[username]))
    #
    #     return HttpResponseRedirect(reverse('user-profile:profile', args=[username]))
    #
    #
    #
    # return render(request, 'edit_profile.html', context={'profile': profile, 'user': user})

def show_json_saldo(request):
    data_saldo = request.user.profile.saldo
    return JsonResponse({'saldo': data_saldo})

def top_up(request, username):
    pass
    # user = User.objects.get(username=username)
    # profile = Profile.objects.get(user=user)
    #
    # if request.method == 'POST':
    #     jumlah = request.POST.get('jumlah')
    #     jumlah = jumlah.replace('.', '')
    #     profile.saldo += (int(jumlah) - 1000)
    #     profile.save()
    #
    #     return HttpResponseRedirect(reverse('user-profile:profile', args=[username]))
    #
    # return render(request, 'top_up.html', context={'profile': profile, 'user': user})


# WARNING!! FOR DEVELOPMENT PURPOSE ONLY!
@csrf_exempt
def delete_acc(request, username):
    try:
        u = UserProfile.objects.get(username=username)
        u.delete()

    except UserProfile.DoesNotExist:
        pass

    return redirect('user-profile:register')


# * FOR FLUTTER ONLY!! * #

# * FLUTTER AUTHENTICATION SYSTEM * #

@csrf_exempt
def flutter_daftar(request):

    if request.method == "POST":
        form = DaftarForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return JsonResponse(UserSerializer(user).data, status=200)

        errors = {field: error.get_json_data() for field, error in form.errors.items()}
        return JsonResponse({'success': False, 'errors': errors}, status=400)

    return HttpResponseNotFound()


@csrf_exempt
def flutter_masuk(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'success': True}, status=200)

            return JsonResponse({'success': False, 'message': 'Akun telah dinonaktifkan'}, status=401)

        return JsonResponse({'success': False, 'message': 'Username atau kata sandi salah.'}, status=401)

    return HttpResponseNotFound()


@csrf_exempt
def flutter_logout(request):

    if request.method == "POST":
        try:
            logout(request)
            return JsonResponse({'success': True, 'message': 'Sukses logout'}, status=200)
        except:
            return JsonResponse({'success': False}, status=401)

    return HttpResponseNotFound()


# * FLUTTER DEV API * #

@csrf_exempt
def flutter_user_info(request):

    if request.method == "GET":
        username = request.GET.get('username')

        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Pengguna tidak ditemukan!'}, status=401)

        return JsonResponse({'success': True, 'user': UserSerializer(user).data}, status=200)

    return HttpResponseNotFound()
