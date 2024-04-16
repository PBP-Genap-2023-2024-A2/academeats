from django.db import models
from django.contrib.auth.models import User
from makanan.models import Makanan


# Model Item Keranjang
class ItemKeranjang(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    jumlah = models.IntegerField(default=0)
