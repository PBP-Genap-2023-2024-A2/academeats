from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('main.urls', 'main'), namespace='main')),
    path('u/', include(('user_profile.urls', 'user_profile'), namespace='user-profile')),
    path('toko/', include(('toko.urls', 'toko'), namespace='toko')),
    path('makanan/', include(('makanan.urls', 'makanan'), namespace='makanan')),
    path('keranjang/', include(('keranjang.urls', 'keranjang'), namespace='keranjang')),
    path('order/', include(('order.urls', 'order'), namespace='order')),
    path('review/', include(('review.urls', 'review'), namespace='review')),
    path('forum/', include(('forum.urls', 'forum'), namespace='forum')),
    path('admin/', admin.site.urls),
    ]
