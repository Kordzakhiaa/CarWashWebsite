from django.db import models


class CarWasher(models.Model):
    name = models.CharField(max_length=200,)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    # car = models.OneToOneField(Car, max_length=200, on_delete=models.CASCADE)
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(models.Model):
    TYPES = (
        ('crossover', 'crossover'),
        ('sedan', 'sedan'),
        ('hatchback', 'hatchback')
    )

    car_type = models.CharField(max_length=200, null=False, choices=TYPES)
    license_plate = models.CharField(max_length=30, null=False)
    car_owner = models.OneToOneField(
        Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.car_type}, {self.license_plate}"


class Order(models.Model):
    order_start_date = models.DateTimeField(verbose_name="Order Start Date")
    order_end_date = models.DateTimeField(verbose_name="Order End Date")
    washer = models.ForeignKey(CarWasher, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
