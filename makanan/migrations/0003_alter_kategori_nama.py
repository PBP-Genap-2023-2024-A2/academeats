# Generated by Django 5.0.3 on 2024-04-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makanan', '0002_kategori_makanan_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='nama',
            field=models.CharField(max_length=20),
        ),
    ]
