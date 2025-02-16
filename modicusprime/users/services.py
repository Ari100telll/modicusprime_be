from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from modicusprime.users.selectors import get_user_by_username

User = get_user_model()


def create_user(*, username: str, email: str, password: str, first_name: str, last_name: str) -> User:
    if get_user_by_username(username=username):
        raise ValidationError(f"User with username {username} already exists")

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )

    return user
