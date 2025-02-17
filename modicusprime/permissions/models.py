from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import (
    CASCADE,
    BooleanField,
    ForeignKey,
    ManyToManyField,
    UUIDField,
)

from modicusprime.states.models import Transition
from modicusprime.utils.base_models import BaseUUIDModel

# Create your models here.

User = get_user_model()


class InstancePermission(BaseUUIDModel):
    user = ForeignKey(User, on_delete=CASCADE, related_name="instances_permissions")

    # Example of other permissions
    is_edit_allowed = BooleanField(default=False)
    transactions = ManyToManyField(Transition, related_name="instances_permissions")

    content_type = ForeignKey(ContentType, on_delete=CASCADE, related_name="instances_permissions")
    object_id = UUIDField(max_length=255, blank=True, null=True, db_index=True)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        db_table = "instance_permission"
        verbose_name = "Instance Permission"
        verbose_name_plural = "Instance Permissions"

    def __str__(self):
        return f"{self.user} | {self.object_id}"
