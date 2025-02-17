from typing import List

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from rest_framework.exceptions import ValidationError

from modicusprime.workspaces.models import Document, Workspace

User = get_user_model()


def remove_contributors_from_workspace(workspace: Workspace, contributors: List[User]):
    document_ct = ContentType.objects.get_for_model(Document)
    workspace_ct = ContentType.objects.get_for_model(Workspace)
    if workspace.user in contributors:
        raise ValidationError("You can't remove the owner of the workspace")

    # Todo reafactore to make 1 request.
    for contributor in contributors:
        permissions_filter_query = Q(
            content_type=document_ct,
            object_id__in=Document.objects.filter(workspace_id=workspace.id).values_list("id", flat=True),
        ) | Q(content_type=workspace_ct, object_id=workspace.id)
        contributor.instances_permissions.filter(permissions_filter_query).delete()

    workspace.contributors.remove(*contributors)
