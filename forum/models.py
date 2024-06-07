from django.contrib.auth.models import User
from django.db import models

from user_profile.models import UserProfile


# Create your models here.
class Kategori(models.Model):

    nama = models.CharField(max_length=20)


class Forum(models.Model):

    judul = models.CharField(max_length=50)
    deskripsi = models.TextField()
    kreator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    jumlah_pesan = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Message(models.Model):
    pengirim = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    pesan = models.TextField()
    membalas_ke = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
