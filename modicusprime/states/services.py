import uuid
from typing import Optional

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ValidationError

from modicusprime.permissions.models import InstancePermission
from modicusprime.states.models import StateDefinition, Transition, TransitionRequest
from modicusprime.workspaces.selectors import get_generic_instance

User = get_user_model()


def create_transition(*, from_state: Optional[StateDefinition], to_state: StateDefinition, requires_signature: bool):
    if Transition.objects.filter(from_state=from_state, to_state=to_state).exists():
        raise ValidationError("Transition already exists")

    return Transition.objects.create(from_state=from_state, to_state=to_state, requires_signature=requires_signature)


def create_transition_request(
    *,
    user: User,
    transition: Transition,
    meta: dict = None,
    content_type: ContentType,
    object_id: uuid.UUID,
):
    instance = get_generic_instance(content_type=content_type, object_id=object_id)
    user_instance_permission = InstancePermission.objects.filter(
        user=user, content_type=content_type, object_id=object_id
    ).first()

    if not user_instance_permission or not user_instance_permission.transactions.filter(id=transition.id).exists():
        raise ValidationError("User is not allowed to request this transition")

    if instance.state != transition.from_state:
        raise ValidationError("Instance is not in the correct state to request this transition")

    if TransitionRequest.objects.filter(is_obsolete=False, content_type=content_type, object_id=object_id).exists():
        raise ValidationError("Transition request already exists for this instance")

    transaction_request = TransitionRequest.objects.create(
        user=user, transition=transition, meta=meta, content_type=content_type, object_id=object_id
    )

    if not transition.requires_signature:
        transaction_request.is_obsolete = True
        transaction_request.save()
        instance.state = transition.to_state
        instance.save()

    return transaction_request
