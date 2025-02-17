from typing import Type

from django.contrib.auth import get_user_model
from django.db import models

from modicusprime.states.models import StateDefinition
from modicusprime.utils.base_models import BaseUUIDModel

User = get_user_model()


def document_path(instance: Type["Document"], _: str):
    return f"user_{instance.workspace.name}/documents/{instance.title}"


class Workspace(BaseUUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workspaces")
    name = models.CharField(max_length=255)
    description = models.JSONField(blank=True, null=True)
    contributors = models.ManyToManyField(User, related_name="contributed_workspaces")
    state = models.ForeignKey(
        StateDefinition, on_delete=models.SET_NULL, related_name="workspaces", null=True, blank=True
    )


class Document(BaseUUIDModel):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name="documents")
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=document_path)
    state = models.ForeignKey(
        StateDefinition, on_delete=models.SET_NULL, related_name="documents", null=True, blank=True
    )


# Todo Add contributor
