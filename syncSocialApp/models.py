from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # add additional fields in here
    friends = models.ManyToManyField("self", blank=True)
    dates_free = models.TextField(blank=True)
