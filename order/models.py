from django.db import models
from django.contrib.auth.models import User


class UserOrder(models.Model):
    pembeli = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


class Order(models.Model):

    # ENUM FOR ORDER STATUS
    class StatusPesanan(models.TextChoices):
        DIPESAN = "dipesan", "Dipesan"
        DIPROSES = "diproses", "Diproses"
        SELESAI = "selesai", "Selesai"

    # makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    orderID = models.CharField
    quantity = models.IntegerField
    status = models.CharField(
        max_length=8,
        choices=StatusPesanan.choices
    )
