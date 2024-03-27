from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    # ENUM FOR ROLE
    # Digunakan untuk user agar hanya dapat memilih antara role penjual atau pembeli
    class Role(models.TextChoices):
        PENJUAL = "penjual", "Penjual"
        PEMBELI = "pembeli", "Pembeli"

    # One-to-one relationship with user model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    # Additional fields for user
    nama = models.CharField(max_length=255)
    bio = models.TextField()
    saldo = models.FloatField(default=0)
    role = models.CharField(
        max_length=7,
        choices=Role.choices
    )
    pfp_url = models.TextField(
        default="https://i.quotev.com/hiaa3fa55smq.jpg"
    )


# this method to generate profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# this method to update profile when user is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
