# Generated by Django 4.2.10 on 2024-03-01 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domo_api', '0003_devices_dots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dots',
            old_name='dattime',
            new_name='datTime',
        ),
        migrations.RenameField(
            model_name='dots',
            old_name='devicde',
            new_name='device_id',
        ),
    ]
