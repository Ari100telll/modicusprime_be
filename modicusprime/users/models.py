from django.contrib.auth.models import AbstractUser

from modicusprime.utils.base_models import BaseUUIDModel


class User(AbstractUser, BaseUUIDModel):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.email} {self.first_name} {self.last_name}"
