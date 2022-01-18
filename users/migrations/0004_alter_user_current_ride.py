# Generated by Django 4.0.1 on 2022-01-18 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_alter_payment_amount_alter_payment_status_and_more'),
        ('users', '0003_user_current_ride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='current_ride',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rides.ride'),
        ),
    ]