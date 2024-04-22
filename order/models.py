from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from makanan.models import Makanan
from toko.models import Toko

class Order(models.Model):
    # ENUM FOR ORDER STATUS
    class StatusPesanan(models.TextChoices):
        DIPESAN = "dipesan", "Dipesan"
        DIPROSES = "diproses", "Diproses"
        SELESAI = "selesai", "Selesai"
        DIBATALKAN = "dibatalkan", "Dibatalkan"

    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    orderID = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        default = StatusPesanan.DIPESAN,
        max_length= 10,
        choices=StatusPesanan.choices
    )
