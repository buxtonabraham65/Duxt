# Generated by Django 5.1.1 on 2024-09-15 13:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_carcontactform'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarContactForm',
            new_name='CarContact',
        ),
    ]
