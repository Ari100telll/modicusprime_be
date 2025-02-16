import pytest
from django.contrib.auth import get_user_model

from ..selectors import get_user_by_username
from .factories import UserFactory

pytestmark = pytest.mark.django_db
User = get_user_model()


class TestUsersSelectors:
    expected_users_count = 2

    @pytest.mark.parametrize(
        "username, expected_username, result",
        [
            ("expected_username", "expected_username", True),
            ("unexpected_username", "expected_username", False),
        ],
    )
    def test_get_users_by_username(self, username, expected_username, result):
        user = UserFactory(username=username)

        expected_user = get_user_by_username(username=expected_username)

        assert (expected_user == user) is result
