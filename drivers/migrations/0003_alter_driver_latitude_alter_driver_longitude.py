# Generated by Django 4.0.1 on 2022-01-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_vehicle_driver_license_number_driver_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]