# Generated by Django 5.1.1 on 2024-10-13 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_productimage_delete_carimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.rent')),
            ],
        ),
    ]
