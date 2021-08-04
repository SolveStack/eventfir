from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    price_rank = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])
