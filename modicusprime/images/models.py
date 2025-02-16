from django.contrib.auth import get_user_model
from django.db import models

from modicusprime.utils.base_models import BaseUUIDModel
from typing import Type

User = get_user_model()


def image_path(instance: Type["Image"], _: str):
    return f"user_{instance.user.username}/images/{instance.id}"


class Image(BaseUUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_path)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
