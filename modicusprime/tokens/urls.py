from django.urls import path

from modicusprime.tokens.api.views import LoginApi, RefreshApi

app_name = "tokens"

urlpatterns = [
    path("login/", LoginApi.as_view(), name="login"),
    path("refresh/", RefreshApi.as_view(), name="refresh"),

]
