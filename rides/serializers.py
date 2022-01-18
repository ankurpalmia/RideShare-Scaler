from rest_framework import serializers

from drivers.services import get_nearest_driver
from rides.models import Ride, Payment


class RequestRideSerializer(serializers.Serializer):
    """
    Serializer for Requesting Ride
    """
    starting_location = serializers.CharField()
    end_location = serializers.CharField()
    customer_id = serializers.IntegerField()

    def _validate_location(self, location):
        lat_long = location.split(",")
        if len(lat_long) != 2:
            raise serializers.ValidationError("Starting location should be of form: (<int>, <int>)")

    def validate_starting_location(self, value):
        self._validate_location(value)
        return value

    def validate_end_location(self, value):
        self._validate_location(value)
        return value

    def validate(self, attrs):
        if attrs["starting_location"] == attrs["end_location"]:
            raise serializers.ValidationError("Starting and End locations cannot be same")
        return attrs

    def create(self, validated_data):
        lat_long = validated_data["starting_location"].split(", ")
        starting_latitude = int(lat_long[0])
        starting_longitude = int(lat_long[1])
        driver = get_nearest_driver(starting_latitude, starting_longitude)
        print("\nDriver: ", driver)
        if not driver:
            raise serializers.ValidationError("Driver not found")
        self.ride = Ride.objects.get_or_create(
            driver = driver,
            customer_id = validated_data["customer_id"],
            starting_location=validated_data["starting_location"],
            end_location=validated_data["end_location"],
        )
        driver.current_ride = self.ride
        driver.save()
        return self.ride

    def to_representation(self, instance):
        super().to_representation(instance)
        ride_serializer = RideSerializer(self.ride)
        return ride_serializer.data


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer for Payment details
    """
    class Meta:
        model = Payment
        fields = "__all__"


class RideSerializer(serializers.ModelSerializer):
    """
    Serializer class for Ride details
    """
    payment = PaymentSerializer()

    class Meta:
        model = Ride
        fields = "__all__"
