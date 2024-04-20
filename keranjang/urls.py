from django.urls import path
from keranjang.views import show_main

app_name = 'keranjang'

urlpatterns = [
    path('keranjang/', show_main, name='show_main'),
]
