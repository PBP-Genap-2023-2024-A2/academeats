from django.db import models
from django.contrib.auth.models import User
from makanan.models import Makanan


# Model Keranjang
class Keranjang(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class ItemKeranjang(models.Model):
    keranjang = models.ForeignKey(Keranjang, on_delete=models.CASCADE)
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    jumlah = models.IntegerField(default=0)
