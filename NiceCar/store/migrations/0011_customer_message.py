# Generated by Django 5.1.1 on 2024-09-11 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='message',
            field=models.TextField(blank=True, default=False, null=True),
        ),
    ]
