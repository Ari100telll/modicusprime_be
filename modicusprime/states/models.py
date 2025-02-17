from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# User is able to create states groups
class StatesGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# User is able to create state definitions
class StateDefinition(models.Model):
    group = models.ForeignKey(
        StatesGroup, on_delete=models.CASCADE, related_name="definitions"
    )
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)


# User is able to define allowed transitions between states
class Transition(models.Model):
    requires_signature = models.BooleanField(default=False)

    from_state = models.ForeignKey(
        StateDefinition, on_delete=models.CASCADE, related_name="from_transitions"
    )
    to_state = models.ForeignKey(
        StateDefinition, on_delete=models.CASCADE, related_name="to_transitions"
    )


# User is able to request transitions
class TransitionRequest(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transition_requests"
    )
    transition = models.ForeignKey(
        Transition, on_delete=models.CASCADE, related_name="requests"
    )
    meta = models.JSONField(blank=True, null=True)
    is_obsolete = models.BooleanField(default=False)

    class Meta:
        abstract = True
