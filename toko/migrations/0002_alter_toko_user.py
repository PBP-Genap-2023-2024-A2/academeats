# Generated by Django 5.0.4 on 2024-06-02 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0001_initial'),
        ('user_profile', '0006_userprofile_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toko',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile'),
        ),
    ]
