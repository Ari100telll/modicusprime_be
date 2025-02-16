import pytest
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

from modicusprime.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db
User = get_user_model()


class TestUsersAPI:
    USER_LIST_CREATE_ROUTE = "api:users:user-create-list"
    expected_users_count = 4

    def test_users_list(self, api_client_with_credentials):
        api_client, _ = api_client_with_credentials
        UserFactory.create_batch(size=self.expected_users_count)

        response = api_client.get(
            reverse(
                self.USER_LIST_CREATE_ROUTE,
            )
        )

        assert response.status_code == 200
        assert response.json()["count"] == self.expected_users_count + 1

    def test_users_create(self, api_client_with_credentials):
        api_client, _ = api_client_with_credentials
        user_data = {
            "username": "username",
            "email": "test@example.com",
            "password": "password",
            "first_name": "first_name",
            "last_name": "last_name",
        }

        response = api_client.post(
            reverse(
                self.USER_LIST_CREATE_ROUTE,
            ),
            data=user_data,
            format="json",
        )

        assert response.status_code == 201
        assert User.objects.filter(username=user_data["username"]).exists()
