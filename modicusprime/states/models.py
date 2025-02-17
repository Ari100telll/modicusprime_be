from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import ForeignKey, UUIDField

from modicusprime.utils.base_models import BaseUUIDModel

User = get_user_model()


# User is able to create states groups
class StatesGroup(BaseUUIDModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# User is able to create state definitions
class StateDefinition(BaseUUIDModel):
    group = models.ForeignKey(StatesGroup, on_delete=models.CASCADE, related_name="definitions")
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.group.name}: {self.name}"


# User is able to define allowed transitions between states
class Transition(BaseUUIDModel):
    requires_signature = models.BooleanField(default=False)

    from_state = models.ForeignKey(
        StateDefinition, on_delete=models.CASCADE, related_name="from_transitions", null=True, blank=True
    )
    to_state = models.ForeignKey(StateDefinition, on_delete=models.CASCADE, related_name="to_transitions")

    def __str__(self):
        return (
            f"{self.from_state.name if self.from_state else '-'} -> "
            f"{self.to_state.name} (RS: {self.requires_signature})"
        )

    class Meta:
        unique_together = ("from_state", "to_state")


# User is able to request transitions
class TransitionRequest(BaseUUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transition_requests")
    transition = models.ForeignKey(Transition, on_delete=models.CASCADE, related_name="requests")
    meta = models.JSONField(blank=True, null=True)
    is_obsolete = models.BooleanField(default=False)

    content_type = ForeignKey(ContentType, on_delete=models.CASCADE, related_name="transition_requests")
    object_id = UUIDField(max_length=255, blank=True, null=True, db_index=True)
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return f"{self.user} | {self.transition} | {self.content_object}"


class TransitionRequestActionLog(BaseUUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transition_request_actions")
    previous_state = models.JSONField(blank=True, null=True)
    new_state = models.JSONField(blank=True, null=True)

    object_id = UUIDField(max_length=255, blank=True, null=True, db_index=True)
    meta = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} | {self.meta}"
