from django.db import models
from user_profile.models import User


# Model Keranjang
class Keranjang(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
