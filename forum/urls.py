from django.urls import path

from forum import views

urlpatterns = [
    path('', views.forum_home, name='home'),
    path("create/", views.create_new_forum, name='create'),
    path("<int:forum_id>/", views.forum_page, name='page'),
    path("delete/<int:forum_id>", views.delete_forum, name='delete'),
    path("get-replies/<int:forum_id>", views.get_all_replies, name='get-replies'),
    path("edit/<int:forum_id>", views.edit_forum, name='edit'),
    path("buat-pesan/<int:forum_id>/<int:reply_to>", views.buat_pesan, name='buat-pesan')
]
