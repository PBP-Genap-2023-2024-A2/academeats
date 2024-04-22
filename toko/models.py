from django.contrib.auth.models import User
from django.db import models


# Model Toko
class Toko(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name