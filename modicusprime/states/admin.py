from django.contrib import admin

from modicusprime.states.models import (
    StateDefinition,
    StatesGroup,
    Transition,
    TransitionRequest,
)

# Register your models here.

admin.site.register(StatesGroup)
admin.site.register(StateDefinition)
admin.site.register(Transition)
admin.site.register(TransitionRequest)
