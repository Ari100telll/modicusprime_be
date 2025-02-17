from django.urls import path

from modicusprime.permissions.api.views import InstancePermissionsCreateListApi

app_name = "permissions"

urlpatterns = [
    path("", InstancePermissionsCreateListApi.as_view(), name="instanse-permissions-create-list"),
]
