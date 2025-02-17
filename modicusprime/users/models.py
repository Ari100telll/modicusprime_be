from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _

from modicusprime.utils.base_models import BaseUUIDModel


class User(AbstractUser, BaseUUIDModel):
    email = EmailField(_("email address"), unique=True, blank=False)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.email} {self.first_name} {self.last_name}"
