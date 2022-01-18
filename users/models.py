from django.db import models


class User(models.Model):
    """
    Model class for User details
    """
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique=True)
    current_ride = models.OneToOneField("rides.Ride", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
