from django.core.validators import MinValueValidator
from django.db import models

from toko.models import Toko


class Kategori(models.Model):
    nama = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nama


class Makanan(models.Model):
    nama = models.CharField(max_length=250)
    harga = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    deskripsi = models.TextField()
    stok = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    kategori = models.ForeignKey(Kategori, null=True, on_delete=models.RESTRICT)
    img_url = models.CharField(max_length=500)
