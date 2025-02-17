import uuid
from typing import Optional

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ValidationError

from modicusprime.states.models import StateDefinition, Transition
from modicusprime.workspaces.models import Document

User = get_user_model()


def get_workspace_from_generic_instance(
    *,
    content_type: ContentType,
    object_id: uuid.UUID,
) -> Optional[User]:
    instance = get_generic_instance(content_type=content_type, object_id=object_id)
    if isinstance(instance, Document):
        return instance.workspace
    return instance


def get_generic_instance(
    *,
    content_type: ContentType,
    object_id: uuid.UUID,
):
    model_class = content_type.model_class()
    instance = model_class.objects.filter(id=object_id).first()

    if not instance:
        raise ValidationError("Instance not found")

    return instance


def get_available_transitions_by_state(
    *,
    current_stage: StateDefinition
):
    return Transition.objects.filter(from_state=current_stage)
