from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    customer_id = models.CharField(default="", max_length=255, unique=True)

    def __str__(self):
        return self.customer_id
