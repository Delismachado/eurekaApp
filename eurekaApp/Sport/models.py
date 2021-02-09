from django.db import models

# Create your models here.


class Sport(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    sport_type = models.CharField(max_length=100, null=False)
