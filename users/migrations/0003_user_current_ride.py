# Generated by Django 4.0.1 on 2022-01-18 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_alter_payment_amount_alter_payment_status_and_more'),
        ('users', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='current_ride',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='rides.ride'),
        ),
    ]
