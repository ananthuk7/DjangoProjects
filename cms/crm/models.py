from django.db import models


# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=100)
    edept = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    exp = models.PositiveIntegerField()

    def __str__(self):
        return self.ename