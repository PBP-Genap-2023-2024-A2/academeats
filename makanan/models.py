from django.core.validators import MinValueValidator
from django.db import models

from toko.models import Toko


class Makanan(models.Model):
    nama = models.CharField(max_length=250)
    harga = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    stok = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=500)
