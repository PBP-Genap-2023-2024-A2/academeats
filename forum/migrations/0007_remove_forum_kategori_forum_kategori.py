# Generated by Django 5.0.3 on 2024-04-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_rename_category_kategori_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='kategori',
        ),
        migrations.AddField(
            model_name='forum',
            name='kategori',
            field=models.ManyToManyField(to='forum.kategori'),
        ),
    ]
