# Generated by Django 5.0.3 on 2024-04-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_alter_review_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reply',
            field=models.TextField(default='(Belum ada balasan dari penjual)'),
        ),
    ]
