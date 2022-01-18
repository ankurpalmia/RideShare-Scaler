from rest_framework.viewsets import ModelViewSet

from drivers.models import Driver
from drivers.serializers import DriverSerializer


class DriverViewSet(ModelViewSet):
    """
    View set for the driver details
    """
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
