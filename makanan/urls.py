from django.contrib import admin
from django.urls import path, include
from makanan import views

urlpatterns = [
    path('<int:makanan_id>/', views.detail_makanan, name="detail"),
    path('<int:makanan_id>/edit', views.edit_makanan, name='edit')
]
