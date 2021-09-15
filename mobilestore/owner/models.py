from django.db import models
from datetime import date, timedelta

edd = date.today()+timedelta(days=5)


# Create your models here.
class Mobiles(models.Model):
    mobile_name = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100, unique=True)
    company = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.mobile_name


class Order(models.Model):
    products = models.ForeignKey(Mobiles, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    address = models.CharField(max_length=120)
    options = (
        ('Delivered', 'Delivered'),
        ('intransit', 'intransit'),
        ('ordered', 'ordered'),
        ('cancelled', 'cancelled'),
    )
    phone = models.CharField(max_length=12, null=True)
    status = models.CharField(max_length=20, choices=options, default='ordered')
    expected_delivery_date = models.DateField(null=True, default=edd)
