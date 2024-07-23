from django.contrib import admin

# Register your models here.

from .models import Property, Reservation

admin.site.register(Property)
admin.site.register(Reservation)
