from django.urls import path

from rides.views import RequestRideView, RidesView


urlpatterns = [
    path("", RidesView.as_view(), name="Rides"),
    path("request/", RequestRideView.as_view(), name="Request Ride")

]
