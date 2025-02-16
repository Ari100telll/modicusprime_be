from django.urls import path

from modicusprime.users.api.views import UsersCreateListApi

app_name = "users"

urlpatterns = [
    path("", UsersCreateListApi.as_view(), name="user-create-list"),
]
