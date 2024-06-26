# Generated by Django 5.0.3 on 2024-04-01 23:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_order_order_makanan_order_orderid_and_more'),
        ('review', '0002_alter_review_nilai'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='order',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='nilai',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
