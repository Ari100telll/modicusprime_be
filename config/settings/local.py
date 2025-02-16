from .base import *  # noqa

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "pet-openly-imp.ngrok-free.app"]
DOMAIN_NAME = env.str("DOMAIN_NAME", default="127.0.0.1:8000")
