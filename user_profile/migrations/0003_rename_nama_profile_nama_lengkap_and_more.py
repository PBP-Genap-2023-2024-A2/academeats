# Generated by Django 5.0.3 on 2024-04-01 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_profile_pfp_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='nama',
            new_name='nama_lengkap',
        ),
        migrations.AddField(
            model_name='profile',
            name='nama_panggilan',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
