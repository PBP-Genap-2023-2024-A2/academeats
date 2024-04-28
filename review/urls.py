from django.urls import path
from review.views import show_review_penjual, reply_review, create_review, show_review_pembeli

appname = 'review'

urlpatterns = [
    path('<int:makanan_id>/penjual', show_review_penjual, name='show_review_penjual'),
    path('create/<int:makanan_id>/', create_review, name='create_review'),
    path('reply/<int:review_id>/', reply_review, name='reply_review'),
    path('<int:makanan_id>/pembeli', show_review_pembeli, name='show_review_pembeli'),
]
