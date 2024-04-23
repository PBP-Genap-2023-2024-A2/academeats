from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from makanan.models import Makanan
from toko.models import Toko


class OrderGroup(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    orderID = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_harga = models.FloatField()

class Order(models.Model):
    # ENUM FOR ORDER STATUS
    class StatusPesanan(models.TextChoices):
        DIPESAN = "DIPESAN"
        DIPROSES = "DIPROSES"
        SELESAI = "SELESAI"
        DIBATALKAN = "DIBATALKAN"

    order_group = models.ForeignKey(OrderGroup, on_delete=models.CASCADE)
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    status = models.CharField(
        default = StatusPesanan.DIPESAN,
        max_length= 10,
        choices=StatusPesanan.choices
    )
