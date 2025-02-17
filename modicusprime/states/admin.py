from django.contrib import admin

from modicusprime.states.models import (
    StateDefinition,
    StatesGroup,
    Transition,
    TransitionRequest,
    TransitionRequestActionLog,
)

# Register your models here.

admin.site.register(StatesGroup)
admin.site.register(StateDefinition)
admin.site.register(Transition)
admin.site.register(TransitionRequest)
admin.site.register(TransitionRequestActionLog)
