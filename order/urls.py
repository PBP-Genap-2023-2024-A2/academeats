from django.urls import path
from order.views import show_main_penjual, show_main_pembeli, edit_status_penjual, edit_status_batal

app_name = 'order'

urlpatterns = [
    path('toko/<int:toko_id>', show_main_penjual, name='show_main_penjual'),
    path('', show_main_pembeli, name='show_main_pembeli'),
    path('edit_status_penjual/', edit_status_penjual, name='edit_status_penjual'),
    path('edit_status_batal/<int:og_id>', edit_status_batal, name='edit_status_batal'),
]
