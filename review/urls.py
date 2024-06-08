from django.urls import path
from review.views import reply_review, create_review, show_review_flutter, reply_review_flutter, create_review_flutter
from review.views import show_review_penjual, reply_review, create_review, show_review_pembeli

appname = 'review'

urlpatterns = [
    path('<int:makanan_id>/penjual/', show_review_penjual, name='show_review_penjual'),
    path('create/<int:makanan_id>/', create_review, name='create_review'),
    path('reply/<int:review_id>/', reply_review, name='reply_review'),
    path('<int:makanan_id>/pembeli/', show_review_pembeli, name='show_review_pembeli'),

    #for flutter 
    path('api/v1/', show_review_flutter, name='flutter_get_all_review'),
    path('api/v1/create/<int:makanan_id>', create_review_flutter, name='flutter_create_review'),
    path('api/v1/reply/<int:review_id>', reply_review_flutter, name='flutter_reply_review'),
]
