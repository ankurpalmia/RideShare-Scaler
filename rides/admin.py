from django.contrib import admin

from rides.models import Payment, Ride


admin.site.register(Ride)
admin.site.register(Payment)
