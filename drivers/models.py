from django.db import models

from users.models import User


class Vehicle(models.Model):
    """
    Model class for Vehicle details
    """
    model = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.model}: {self.registration_number}"


class Driver(User):
    """
    Model class for Driver details
    -> latitude, longitude
    """
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    license_number = models.CharField(max_length=10, unique=True)
    vehicle = models.OneToOneField("drivers.Vehicle", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}: ({self.latitude}, {self.longitude})"
