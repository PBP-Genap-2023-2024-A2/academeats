# Generated by Django 5.0.3 on 2024-04-23 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordergroup',
            name='orderID',
        ),
    ]
