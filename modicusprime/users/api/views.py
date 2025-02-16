from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from modicusprime.users.api.serializers import UserInputSerializer, UserOutputSerializer
from modicusprime.users.services import create_user
from modicusprime.utils.pegination_common import CommonPagination

User = get_user_model()


@extend_schema_view(
    get=extend_schema(
        summary="List all users",
        tags=["User"],
    ),
    post=extend_schema(
        summary="Create User", request=UserInputSerializer, responses={200: UserOutputSerializer}, tags=["User"]
    ),
)
class UsersCreateListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserOutputSerializer
    pagination_class = CommonPagination

    def post(self, request):
        """Create a new user."""
        serializer = UserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(**serializer.validated_data)
        data = self.serializer_class(user).data
        return Response(data, status=HTTP_201_CREATED)
