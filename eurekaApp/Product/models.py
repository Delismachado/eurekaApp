from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    