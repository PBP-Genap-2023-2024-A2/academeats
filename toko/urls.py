from django.urls import path
from toko import views


urlpatterns = [
    path('<int:toko_id>', views.info_toko, name='info_toko'),
    path('manage', views.manage_toko, name='manage'),
    path('manage/<int:toko_id>', views.manage_toko, name='manage'),
    path('create', views.create_toko, name='create_toko'),
    path('<int:toko_id>/tambah-makanan', views.tambah_makanan, name='tambah_makanan'),
]
