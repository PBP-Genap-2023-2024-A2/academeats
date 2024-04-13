from django.urls import path
from review.views import show_review, reply_review, create_review

appname = 'review'

urlpatterns = [
    path('<int:order_id>/', show_review, name='show_review'),
    path('<int:order_id>/create/', create_review, name='create_review'),
    path('reply/<int:id>/', reply_review, name='reply_review')
]
