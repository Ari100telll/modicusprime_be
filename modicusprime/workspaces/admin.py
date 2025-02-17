from django.contrib import admin

from modicusprime.workspaces.models import Document, Workspace

# Register your models here.

admin.site.register(Workspace)
admin.site.register(Document)
