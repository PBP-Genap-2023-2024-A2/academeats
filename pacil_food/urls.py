"""
URL configuration for pacil_food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
