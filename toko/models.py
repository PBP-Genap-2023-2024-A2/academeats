from django.db import models

from user_profile.models import UserProfile


# Model Toko
class Toko(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
