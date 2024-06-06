from django.contrib import admin
from django.urls import path, include
from makanan import views

urlpatterns = [
    path('<int:makanan_id>/', views.detail_makanan, name="detail"),
    path('<int:makanan_id>/edit', views.edit_makanan, name='edit'),
    path('<int:makanan_id>/main', views.show_makanan, name='main'),
    path('<int:makanan_id>/detail-json', views.detail_makanan_json, name="detail-json"),
    path('<int:makanan_id>/detail-review-json', views.detail_review_makanan_json, name="delete"),
]
