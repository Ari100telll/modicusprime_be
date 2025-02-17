import uuid

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ValidationError

from modicusprime.permissions.models import InstancePermission
from modicusprime.states.models import Transition
from modicusprime.workspaces.selectors import get_workspace_from_generic_instance

User = get_user_model()


def create_instance_premission(
    *,
    is_edit_allowed: bool,
    user: User,
    content_type: ContentType,
    object_id: uuid.UUID,
    transactions: list[Transition] = None,
    creator: User,
):
    workspace = get_workspace_from_generic_instance(content_type=content_type, object_id=object_id)
    if workspace.user != creator:
        raise ValidationError("You are not allowed to create permissions for this instance")

    if not workspace.contributors.filter(id=user.id).exists():
        raise ValidationError("User is not a contributor of the workspace")

    if InstancePermission.objects.filter(user=user, content_type=content_type, object_id=object_id).exists():
        raise ValidationError("Instance permission already exists")

    instance_permissions = InstancePermission.objects.create(
        is_edit_allowed=is_edit_allowed,
        user=user,
        content_type=content_type,
        object_id=object_id,
    )

    if transactions:
        instance_permissions.transactions.add(*transactions)

    return instance_permissions
