from django.contrib.auth import get_user_model
from factory import Faker
from factory.django import DjangoModelFactory

from modicusprime.utils.factories_common import (
    generate_unique_email,
    generate_unique_username,
)

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    last_name = Faker("last_name")
    first_name = Faker("first_name")
    email = generate_unique_email()
    username = generate_unique_username()
    password = "argon2$argon2i$v=19$m=512,t=2,p=2$Ymx5ZndMaVJIVDVo$JJ60fd762Swcpew7oXezBQ"

    @classmethod
    def create(cls, **kwargs) -> User:
        password = kwargs.pop("password", None)
        user = super().create(**kwargs)
        if password is not None:
            user.set_password(password)
            user.save()
        return user
