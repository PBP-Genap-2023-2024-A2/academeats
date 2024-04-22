# Generated by Django 5.0.3 on 2024-04-22 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_toko'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('orderID', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderID',
        ),
        migrations.AddField(
            model_name='order',
            name='order_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.ordergroup'),
            preserve_default=False,
        ),
    ]