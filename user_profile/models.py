from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import ValidationError
from django.db import models, transaction

# class Profile(models.Model):
#     pass


class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, nomor_hp, password=None, **extra_fields):
        if not email:
            raise ValueError('Email harus diisi!')
        if not username:
            raise ValueError('Username harus diisi!')
        if not nomor_hp:
            raise ValueError('Nomor telepon harus diisi!')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, nomor_hp=nomor_hp, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, nomor_hp, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if (extra_fields.get('is_staff') is not True) \
                or (extra_fields.get('is_superuser') is not True):
            raise ValueError('Superuser harus memiliki is_staff dan is_superuser yang bernilai True!')

        return self.create_user(email, username, nomor_hp, password, **extra_fields)


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('penjual', 'Penjual'),
        ('pembeli', 'Pembeli')
    )

    # Untuk autentikasi
    email = models.EmailField(unique=True)
    nomor_hp = models.CharField(max_length=14, unique=True)
    username = models.CharField(max_length=150, unique=True)

    nama_lengkap = models.CharField(max_length=255)
    nama_panggilan = models.CharField(max_length=255)
    bio = models.TextField()
    saldo = models.FloatField(default=0)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)
    pfp_url = models.TextField(
        default="https://i.quotev.com/hiaa3fa55smq.jpg"
    )

    objects = UserProfileManager()

    REQUIRED_FIELDS = ['email', 'nomor_hp']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profile_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profile_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

    def deduct_balance(self, amt):
        if amt <= 0:
            raise ValidationError("Harus positif!")

        if self.saldo < amt:
            raise ValidationError("Saldo tidak cukup!")

        with transaction.atomic():
            self.saldo -= amt
            self.save(update_fields=['balance'])
