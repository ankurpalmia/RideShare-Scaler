from rest_framework import serializers

from drivers.models import Driver, Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    """
    Serializer for Vehicle details
    """
    class Meta:
        model = Vehicle
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    """
    Serializer for Driver details
    """
    vehicle = VehicleSerializer()
    phone = serializers.CharField(min_length=10, max_length=10)
    license_number = serializers.CharField(min_length=10, max_length=10)

    class Meta:
        model = Driver
        fields = ("name", "phone", "license_number", "vehicle")

    def create(self, validated_data):
        vehicle = validated_data.pop("vehicle")
        if vehicle:
            vehicle = Vehicle.objects.create(**vehicle)
        instance = Driver.objects.create(**validated_data, vehicle=vehicle)
        return instance
