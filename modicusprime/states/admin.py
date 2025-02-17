from django.contrib import admin

from modicusprime.states.models import StatesGroup, StateDefinition, Transition

# Register your models here.

admin.site.register(StatesGroup)
admin.site.register(StateDefinition)
admin.site.register(Transition)
