from django.db import models


class Payment(models.Model):
    """
    Model class for Payment details
    """
    PENDING = "Pending"
    COMPLETED = "Completed"

    STATUS_CHOICES = (
        (PENDING, PENDING), (COMPLETED, COMPLETED)
    )

    amount = models.FloatField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default=PENDING)
    ride = models.OneToOneField("rides.Ride", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ride}: {self.amount}, {self.status}"


class Ride(models.Model):
    """
    Model class for Ride details
    """
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    ONGOING = "Ongoing"

    RIDE_STATUS_CHOICES = (
        (PENDING, PENDING),
        (ONGOING, ONGOING),
        (COMPLETED, COMPLETED),
        (CANCELLED, CANCELLED),
    )

    status = models.CharField(choices=RIDE_STATUS_CHOICES, max_length=10, default=PENDING)
    driver = models.ForeignKey("drivers.Driver", on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    starting_location = models.CharField(max_length=20)
    end_location = models.CharField(max_length=20)
    distance_covered = models.FloatField(null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.driver}, {self.customer} -> {self.status}"
