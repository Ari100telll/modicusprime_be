from typing import Optional

from django.contrib.auth import get_user_model

User = get_user_model()


def get_user_by_username(*, username: str) -> Optional[User]:
    """Return a user by username."""
    return User.objects.filter(username=username).first()
