from django.db import models
from makanan.models import Makanan
from user_profile.models import UserProfile


class ItemKeranjang(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    jumlah = models.IntegerField(default=1)
