from rest_framework.generics import CreateAPIView

from customers.serializers import RequestRideSerializer


class RequestRideView(CreateAPIView):
    """
    View to request ride and create ride instance
    """
    serializer_class = RequestRideSerializer
