import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from modicusprime.users.tests.factories import UserFactory

FROZEN_TIME_IN_TESTS = "2025-01-01 12:00:00"

User = get_user_model()


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture()
def api_client():
    api_client = APIClient()
    return api_client


@pytest.fixture()
def api_client_with_credentials(user, api_client):
    api_client.force_authenticate(user=user)
    return api_client, user
