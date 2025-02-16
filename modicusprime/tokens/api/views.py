from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenViewBase

User = get_user_model()


@extend_schema_view(
    post=extend_schema(
        summary="Obtain User Token",
        tags=["Auth"],
    )
)
class LoginApi(TokenViewBase):
    """API to obtain a user token."""

    serializer_class = TokenObtainPairSerializer


@extend_schema_view(
    post=extend_schema(
        summary="Refresh User Token",
        tags=["Auth"],
    )
)
class RefreshApi(TokenViewBase):
    """API to refresh a user token."""

    serializer_class = TokenRefreshSerializer
