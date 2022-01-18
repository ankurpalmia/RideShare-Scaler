from django.urls import path

from customers.views import RequestRideView


urlpatterns = [
    path("request_ride/", RequestRideView.as_view(), name="Rides")
]
