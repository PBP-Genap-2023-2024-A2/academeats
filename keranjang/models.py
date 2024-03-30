from django.db import models
from django.contrib.auth.models import User
from makanan.models import Makanan


# Model Keranjang
class Keranjang(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    foods = models.ManyToManyField(Makanan)
