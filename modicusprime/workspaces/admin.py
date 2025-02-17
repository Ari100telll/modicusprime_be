from django.contrib import admin

from modicusprime.workspaces.models import Workspace, Document

# Register your models here.

admin.site.register(Workspace)
admin.site.register(Document)
