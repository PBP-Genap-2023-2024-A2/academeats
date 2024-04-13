from django.urls import path

from forum import views

urlpatterns = [
    path('', views.forum_home, name='home'),
    path("create/", views.create_new_forum, name='create-forum'),
    path("<int:forum_id>/", views.forum_page, name='page')
]
