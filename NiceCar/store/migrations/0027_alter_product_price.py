# Generated by Django 5.0.7 on 2024-12-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
