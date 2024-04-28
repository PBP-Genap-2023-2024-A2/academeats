from django.shortcuts import redirect
from django.urls import path

from user_profile import views

urlpatterns = [
    path('<slug:username>', views.profile_page, name='profile'),
    path('register/', views.register, name='register'),
    path('create-profile/', views.create_profile, name='create-profile'),
    path('edit-profile/<slug:username>', views.edit_profile, name='edit-profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('json/', views.show_json_saldo, name='show-json'),
    path('profile/<slug:username>/top-up', views.top_up, name='top-up'),
    path('delete/<slug:username>', views.delete_acc, name='delete')  # FOR DEVELOPMENT PURPOSE ONLY!
]