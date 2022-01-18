from rest_framework import serializers

from drivers.services import get_nearest_driver
from rides.models import Ride
from rides.serializers import RideSerializer


class RequestRideSerializer(serializers.Serializer):
    """
    Serializer for Requesting Ride
    """
    starting_location = serializers.CharField()
    end_location = serializers.CharField()
    customer_id = serializers.IntegerField()

    def _validate_location(self, location):
        lat_long = location.split(",")
        if len(lat_long) != 2 or not all(int(dir) for dir in lat_long):
            raise serializers.ValidationError("Starting location should be of form: (<int>, <int>)")

    def validate_starting_location(self, value):
        self._validate_location(value)

    def validate_end_location(self, value):
        self._validate_location(value)

    def validate(self, attrs):
        if attrs["starting_location"] == attrs["end_location"]:
            raise serializers.ValidationError("Starting and End locations cannot be same")

    def create(self, validated_data):
        starting_latitude, starting_longitude = validated_data["starting_location"].split(", ")
        driver = get_nearest_driver(starting_latitude, starting_longitude)
        if not driver:
            raise serializers.ValidationError("Driver not found")
        self.ride = Ride.objects.create(
            driver = driver,
            customer_id = self.context["customer_id"],
            starting_location=validated_data["starting_location"],
            end_location=validated_data["end_location"],
        )

    def to_representation(self, instance):
        super().to_representation(instance)
        return RideSerializer(self.ride)
