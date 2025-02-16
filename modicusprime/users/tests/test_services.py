import pytest
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from modicusprime.users.services import create_user
from modicusprime.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db
User = get_user_model()


class TestUsersServices:
    def test_create_user(self):
        user = create_user(
            username="username",
            email="email",
            password="password",
            first_name="first_name",
            last_name="last_name",
        )

        assert User.objects.get(username="username") == user

    def test_create_user_with_existing_username(self):
        UserFactory(username="username")

        with pytest.raises(ValidationError):
            create_user(
                username="username",
                email="email",
                password="password",
                first_name="first_name",
                last_name="last_name",
            )
