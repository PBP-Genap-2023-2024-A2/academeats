from django.urls import path
from toko.views import create_toko, info_toko


urlpatterns = [
    path('', create_toko),
    path('<int:id>', info_toko)


]