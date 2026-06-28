from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you want for your custom user model
    Mobile_No = models.CharField(max_length=15, blank=True, null=True)
    


# Create your models here.
