from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    Serializer,
)

User = get_user_model()


class UserOutputSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "created_at",
            "updated_at",
        ]


class UserInputSerializer(Serializer):
    username = CharField()
    email = EmailField()
    password = CharField()
    first_name = CharField()
    last_name = CharField()
