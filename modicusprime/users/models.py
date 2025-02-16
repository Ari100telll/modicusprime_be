from django.contrib.auth.models import AbstractUser
from django.db import models

from modicusprime.utils.base_models import BaseUUIDModel


# Create your models here.

class User(AbstractUser, BaseUUIDModel):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.email} {self.first_name} {self.last_name}"
