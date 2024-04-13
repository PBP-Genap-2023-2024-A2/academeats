from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from order.models import Order

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)
    nilai = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)], default=0)
    komentar = models.TextField()
    reply = models.TextField(null=True)