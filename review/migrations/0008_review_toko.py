# Generated by Django 5.0.3 on 2024-04-22 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_alter_review_nilai_alter_review_reply'),
        ('toko', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='toko',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='toko.toko'),
        ),
    ]