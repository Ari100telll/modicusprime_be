import uuid

from django.db.models import DateTimeField, Model, UUIDField


class BaseUUIDModel(Model):
    """Base model with UUID as primary key."""

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
