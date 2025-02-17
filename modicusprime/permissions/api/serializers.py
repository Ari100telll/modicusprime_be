from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from modicusprime.permissions.models import InstancePermission
from modicusprime.states.models import Transition
from modicusprime.workspaces.api.serializers import (
    DocumentsOutputSerializer,
    WorkspacesOutputSerializer,
)
from modicusprime.workspaces.models import Document, Workspace

User = get_user_model()


class InstancePermissionsOutputSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()
    related_object = serializers.SerializerMethodField()

    class Meta:
        model = InstancePermission
        fields = "__all__"

    def get_content_type(self, obj):
        return obj.content_type.model if obj.content_type else None

    def get_related_object(self, obj):
        if obj.content_type.model == "document":
            document = Document.objects.filter(id=obj.object_id).first()
            return DocumentsOutputSerializer(instance=document).data
        elif obj.content_type.model == "workspace":
            workspace = Workspace.objects.filter(id=obj.object_id).first()
            return WorkspacesOutputSerializer(instance=workspace).data
        return None


class InstancePermissionInputSerializer(serializers.Serializer):

    is_edit_allowed = serializers.BooleanField(default=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    transactions = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=Transition.objects.all()), required=False
    )
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.filter(model__in=["document", "workspace"]), slug_field="model"
    )
    object_id = serializers.UUIDField()
