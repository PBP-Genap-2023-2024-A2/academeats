from django.contrib import admin
from django.urls import path, include
from makanan.views import tambah_makanan


urlpatterns = [
   path('',tambah_makanan,name="index")
    ]