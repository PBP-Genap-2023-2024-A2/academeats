from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from order.models import Order
from makanan.models import Makanan
from user_profile.models import UserProfile


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE, null=True)

    nilai = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=0)
    komentar = models.TextField(null=True, default="-")
    reply = models.TextField(null=True)

