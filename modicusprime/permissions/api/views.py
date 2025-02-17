from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from modicusprime.permissions.api.serializers import (
    InstancePermissionInputSerializer,
    InstancePermissionsOutputSerializer,
)
from modicusprime.permissions.models import InstancePermission
from modicusprime.permissions.services import create_instance_premission
from modicusprime.utils.pegination_common import CommonPagination


#  Todo check ownership to see permissions
class InstancePermissionsCreateListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = InstancePermission.objects.all()
    serializer_class = InstancePermissionsOutputSerializer
    pagination_class = CommonPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user__id", "object_id"]

    def post(self, request):
        """Create a new instance permission."""
        serializer = InstancePermissionInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Todo Add created by for permission or logging
        instance_permission = create_instance_premission(**serializer.validated_data, creator=request.user)
        data = self.serializer_class(instance_permission).data
        return Response(data, status=HTTP_201_CREATED)


# Todo add edit exists permision
# Todo add deleting exists permision
