from django.db import models
from pets.constants import SPECIES_CHOICES, COUNTRY_CHOICES
from django.contrib.auth.models import User


class Pet(models.Model):
    name = models.CharField(null=False, max_length=100)
    species = models.CharField(null=False, choices=SPECIES_CHOICES, max_length=10)
    country_of_origin = models.CharField(null=False, choices=COUNTRY_CHOICES, max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
