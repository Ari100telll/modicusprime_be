from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from modicusprime.states.models import (
    StateDefinition,
    StatesGroup,
    Transition,
    TransitionRequest,
    TransitionRequestActionLog,
)

User = get_user_model()


class StateOutputSerializer(serializers.ModelSerializer):
    group = serializers.CharField()

    class Meta:
        model = StateDefinition
        fields = "__all__"


class StateInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    key = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    color = serializers.CharField(required=False)
    # Todo Change to image field ot url fild
    icon = serializers.CharField(required=False)
    group = serializers.PrimaryKeyRelatedField(queryset=StatesGroup.objects.all())


class StatesGroupOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatesGroup
        fields = "__all__"


class StatesGroupInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)


class TransitionOutputSerializer(serializers.ModelSerializer):
    from_state = StateOutputSerializer()
    to_state = StateOutputSerializer()

    class Meta:
        model = Transition
        fields = "__all__"


class TransitionInputSerializer(serializers.Serializer):
    requires_signature = serializers.BooleanField(default=False)
    from_state = serializers.PrimaryKeyRelatedField(
        queryset=StateDefinition.objects.all(), required=False, allow_null=True
    )
    to_state = serializers.PrimaryKeyRelatedField(queryset=StateDefinition.objects.all())


class TransitionRequestOutputSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = TransitionRequest
        fields = "__all__"

    def get_content_type(self, obj):
        return obj.content_type.model if obj.content_type else None


class TransitionRequestInputSerializer(serializers.Serializer):
    transition = serializers.PrimaryKeyRelatedField(queryset=Transition.objects.all())
    meta = serializers.JSONField(required=False)
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.filter(model__in=["document", "workspace"]), slug_field="model"
    )
    object_id = serializers.UUIDField()


class TransitionRequestActionLogOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransitionRequestActionLog
        fields = "__all__"
