from django.contrib import admin
from .models import Passenger, Ship, Schedule, Booking, Payment

admin.site.register(Passenger)
admin.site.register(Ship)
admin.site.register(Schedule)
admin.site.register(Booking)
admin.site.register(Payment)
