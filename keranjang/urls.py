from django.urls import path
from keranjang import views

app_name = 'keranjang'

urlpatterns = [
    path('', views.show_main, name='show-main'),
    path('get-item/', views.get_item, name='get-item'),
    path('add-item', views.add_item, name='add-item'),
    path('delete-item/<int:keranjang_id>', views.delete_item, name='delete-item'),
    path('checkout-cart/', views.checkout_cart, name='checkout-cart'),
    path('cek-stok/<int:keranjang_id>', views.cek_stok, name='cek_stok')
]
