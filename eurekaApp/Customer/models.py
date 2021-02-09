from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
