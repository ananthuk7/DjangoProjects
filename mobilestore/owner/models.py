from django.db import models


# Create your models here.
class Mobiles(models.Model):
    mobile_name = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100, unique=True)
    company = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.mobile_name