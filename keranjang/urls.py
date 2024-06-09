from django.urls import path
from keranjang import views

app_name = 'keranjang'

urlpatterns = [
    path('', views.show_main, name='show-main'),
    path('get-item/', views.get_item, name='get-item'),
    path('add-item', views.add_item, name='add-item'),
    path('delete-item/<int:keranjang_id>/', views.delete_item, name='delete-item'),
    path('checkout-cart/', views.checkout_cart, name='checkout-cart'),
    path('cek-stok/<int:keranjang_id>', views.cek_stok, name='cek-stok'),
    path('update-jumlah/<int:keranjang_id>/', views.update_jumlah, name='update-jumlah'),
    path('cek-jumlah-item/', views.cek_jumlah_item, name='cek-jumlah-item'),

    # * FLUTTER API * #
    path('api/v1/get-keranjang-item/<str:username>/', views.get_users_cart_items, name='get-keranjang-item'),
    path('api/v1/tambah-item/', views.flutter_add_item_to_cart, name='flutter_add_item_to_cart'),
]
