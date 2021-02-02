from django.contrib import admin
from .models import Order, WashType, CarType, CarWasher, Car, Customer

admin.site.register(Order)
admin.site.register(WashType)
admin.site.register(CarType)
admin.site.register(CarWasher)
admin.site.register(Car)
admin.site.register(Customer)
