from django.db import models

# Create your models here.


class Emp(models.Model):
    name = models.CharField(max_length=200)
    emp_email = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=200)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=True)
    address = models.CharField(max_length=200)
