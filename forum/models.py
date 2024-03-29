from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Forum(models.Model):

    nama = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    pesan = models.TextField()

