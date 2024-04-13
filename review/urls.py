from django.urls import path
from review.views import show_review

appname = 'review'

urlpatterns = [
    path('', show_review, name='show_review')
]
