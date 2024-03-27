from django.shortcuts import redirect
from django.urls import path

from user_profile import views

urlpatterns = [
    path('profile/<slug:username>', views.profile_page, name='profile'),
    path('register/', views.register, name='register'),
    path('create-profile/', views.create_profile, name='create-profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete/<slug:username>', views.delete_acc, name='delete')  # FOR DEVELOPMENT PURPOSE ONLY!
]