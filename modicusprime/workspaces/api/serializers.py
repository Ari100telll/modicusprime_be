from django.contrib.auth import get_user_model
from rest_framework import serializers

from modicusprime.states.api.serializers import StateOutputSerializer
from modicusprime.states.models import Transition
from modicusprime.workspaces.models import Document, Workspace

User = get_user_model()


class WorkspacesOutputSerializer(serializers.ModelSerializer):
    state = StateOutputSerializer()

    class Meta:
        model = Workspace
        fields = "__all__"


class WorkspaceInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.JSONField()
    contributors = serializers.ListSerializer(
        child=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()), required=False
    )
    state = serializers.PrimaryKeyRelatedField(queryset=Transition.objects.all(), required=False)


class WorkspaceEditInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    description = serializers.JSONField(required=False)


class WorkspaceContributorsRemoveInputSerializer(serializers.Serializer):
    contributors = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()))


class DocumentsOutputSerializer(serializers.ModelSerializer):
    state = StateOutputSerializer()

    class Meta:
        model = Document
        fields = "__all__"


class DocumentInputSerializer(serializers.Serializer):
    workspace = serializers.PrimaryKeyRelatedField(queryset=Workspace.objects.all())
    title = serializers.CharField()
    file = serializers.FileField()
    state = serializers.PrimaryKeyRelatedField(queryset=Transition.objects.all(), required=False)
