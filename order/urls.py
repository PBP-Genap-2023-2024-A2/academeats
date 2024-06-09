from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('toko/<int:toko_id>', views.show_main_penjual, name='show_main_penjual'),
    path('', views.show_main_pembeli, name='show_main_pembeli'),
    path('edit_status_penjual/', views.edit_status_penjual, name='edit_status_penjual'),
    path('edit_status_batal/<int:og_id>', views.edit_status_batal, name='edit_status_batal'),
    path('return_stok/<int:og_id>', views.return_stok, name='return_stok'),

    # * FLUTTER API * #
    path('show_main_penjual_json/<int:id>', views.show_main_penjual_json, name='show_main_penjual_json'),
    path('api/v1/order_group/<int:id>', views.flutter_get_og_by_id, name='flutter_get_og_by_id'),
    path('api/v1/<int:toko_id>/orders', views.flutter_get_order, name='flutter_get_order'),
    path('api/v1/flutter_edit_status', views.flutter_edit_status, name='flutter_edit_status'),
    path('api/v1/flutter_get_og_by_user/<str:username>/', views.flutter_get_og_by_user, name='flutter_get_og_by_user'),

    # * TESTING PURPOSE * #
    path('get_order_status/<int:id>', views.order_status, name='order_status'),
    path('api/v1/flutter_get_og_by_user/test/<int:id>/', views.flutter_get_og_by_user_test, name='flutter_get_og_by_user_test')
]
