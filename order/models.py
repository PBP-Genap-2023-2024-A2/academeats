from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from makanan.models import Makanan

class Order(models.Model):
    # ENUM FOR ORDER STATUS
    class StatusPesanan(models.TextChoices):
        DIPESAN = "dipesan", "Dipesan"
        DIPROSES = "diproses", "Diproses"
        SELESAI = "selesai", "Selesai"

    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderID = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0)])
    status = models.CharField(
        max_length=8,
        choices=StatusPesanan.choices
    )