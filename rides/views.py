from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.exceptions import ValidationError

from customers.models import Customer
from drivers.models import Driver
from rides.serializers import RequestRideSerializer, RideSerializer


class RequestRideView(CreateAPIView):
    """
    View to request ride and create ride instance
    """
    serializer_class = RequestRideSerializer


class RidesView(ListAPIView):
    """
    View class to return list of rides
    """
    MODEL_MAP = {"Driver": Driver, "Customer": Customer}

    serializer_class = RideSerializer
    # pagination_class = CustomPagination

    def get_queryset(self):
        model = self.request.GET.get("model")
        if not model or model not in self.MODEL_MAP.keys():
            raise ValidationError("Invalid model name")
        id = self.request.GET.get("id")
        if not id:
            raise ValidationError("id not present")
        user = self.MODEL_MAP[model].objects.filter(id=id)
        if not user:
            raise ValidationError(f"{model} with given id not found")
        return user.first().ride_set.all()
