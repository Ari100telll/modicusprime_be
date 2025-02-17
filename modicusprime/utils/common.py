from typing import Any, Dict, Iterable, Optional, Tuple, TypeVar

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

DjangoModelType = TypeVar("DjangoModelType", bound=models.Model)


def model_update(
    *,
    instance: DjangoModelType,
    data: Dict[str, Any],
    fields: Optional[Iterable[str]] = None,
) -> Tuple[DjangoModelType, bool]:
    has_updated = False
    if fields is None:
        fields = data.keys()

    for field in fields:
        if field not in data:
            continue

        if getattr(instance, field) != data[field]:
            has_updated = True
            setattr(instance, field, data[field])

    if has_updated:
        instance.full_clean()
        instance.save(update_fields=fields)

    return instance, has_updated
