from random import randint

from factory import Sequence
from faker import Faker as RealFaker


def generate_unique_username() -> Sequence:
    return Sequence(lambda n: RealFaker().text(randint(6, 14))[:-1].replace(" ", "") + str(n))


def generate_unique_email() -> Sequence:
    return Sequence(lambda n: f"{RealFaker().name().replace(' ', '').lower()}{n}@example.com")
