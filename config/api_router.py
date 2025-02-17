from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "api"
urlpatterns = [
    path("users/", include("modicusprime.users.urls", namespace="users")),
    path("token/", include("modicusprime.tokens.urls", namespace="tokens")),
    path("states/", include("modicusprime.states.urls", namespace="states")),
    path("workspaces/", include("modicusprime.workspaces.urls", namespace="workspaces")),
    path("permissions/", include("modicusprime.permissions.urls", namespace="permissions")),
]
urlpatterns += router.urls
