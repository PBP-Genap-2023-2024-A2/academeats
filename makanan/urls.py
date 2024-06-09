from django.contrib import admin
from django.urls import path, include
from makanan import views

urlpatterns = [
    path('<int:makanan_id>/', views.detail_makanan, name="detail"),
    path('<int:makanan_id>/edit', views.edit_makanan, name='edit'),
    path('<int:makanan_id>/main', views.show_makanan, name='main'),

    # TES
    path("api/v1/", views.tes_get_all_makanan, name="tes_get_all_makanan"),
]
