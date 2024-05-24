from django.urls import path
from review.views import show_review, reply_review, create_review, show_review_JSON, reply_review_JSON, create_review_JSON

appname = 'review'

urlpatterns = [
    path('<int:makanan_id>/', show_review, name='show_review'),
    path('create/<int:makanan_id>/', create_review, name='create_review'),
    path('reply/<int:review_id>/', reply_review, name='reply_review'),
    path('show-review-json/<int:makanan_id>/', show_review_JSON, name='show_review_JSON'),
    path('create-review-json/<int:makanan_id>/', create_review_JSON, name='create_review_JSON'),
    path('reply-review-json/<int:review_id>/', reply_review_JSON, name='reply_review_JSON'),
]
