from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nilai = models.IntegerField()
    komentar = models.TextField()