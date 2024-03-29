from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    # makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    order = models.ForeignKey(UserOrder, on_delete = models.CASCADE)
    orderID = models.CharField
    quantity = models.IntegerField
    status = models.CharField(
        max_length=8,
        choices=StatusPesanan.choices
    )

    # ENUM FOR ORDER STATUS
    class StatusPesanan(models.TextChoices):
        DIPESAN = "dipesan", "Dipesan", "DIPESAN"
        DIPROSES = "diproses", "Diproses", "DIPROSES"
        SELESAI = "selesai", "Selesai", "SELESAI"

class UserOrder(models.Model):
    pembeli = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )