from django.db import models
from django.utils.translation import ugettext_lazy as _


class CarWasher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WashType(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name of wash type"))
    percentage = models.IntegerField(verbose_name=_("Base price percentage"), default=100)

    def __str__(self):
        return self.name


class CarType(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Car-Type'), unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, null=True)
    license_plate = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.license_plate}"

 
class Order(models.Model):
    STATUS = [
        ('In Process', 'In Process'),
        ('Cancelled', 'Cancelled'),
        ('Finished', 'Finished'),
    ]
    car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name='orders', default=None)
    washer = models.ForeignKey(CarWasher, on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    wash_type = models.ForeignKey(WashType, on_delete=models.PROTECT, related_name='orders', default=None)
    order_price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=_("Price"), default=None, blank=True)
    created_date = models.DateTimeField(auto_now=True, verbose_name=_("Created Date"))
    order_start_date = models.DateTimeField(verbose_name=_("Start time"))
    order_end_date = models.DateTimeField(verbose_name=_("End time"))
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return f"{self.customer}'s car {self.car} using {str(self.wash_type).lower()} washing package"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.order_price = self.car.car_type.price * self.wash_type.percentage / 100
        super(Order, self).save(*args, **kwargs)
