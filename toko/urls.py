from django.urls import path
from toko import views


urlpatterns = [
    path('', views.show_toko, name='show_toko'),
    path('<int:toko_id>', views.info_toko, name='info_toko'),
    path('manage', views.manage_toko, name='manage'),
    path('manage/<int:toko_id>', views.manage_toko, name='manage'),
    path('create', views.create_toko, name='create_toko'),
    path('<int:toko_id>/tambah-makanan', views.tambah_makanan, name='tambah_makanan'),

    # * FLUTTER API * #
    path('api/v1/', views.flutter_get_all_toko, name='flutter_get_all_toko'),
    path('api/v1/<int:id>/', views.flutter_get_toko_by_id, name='flutter_get_toko_by_id'),
]
