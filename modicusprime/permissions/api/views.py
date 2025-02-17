from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from modicusprime.permissions.api.serializers import InstancePermissionsOutputSerializer, \
    InstancePermissionInputSerializer
from modicusprime.permissions.models import InstancePermission
from modicusprime.permissions.services import create_instance_premission
from modicusprime.utils.pegination_common import CommonPagination


# Create your views here.
class InstancePermissionsCreateListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = InstancePermission.objects.all()
    serializer_class = InstancePermissionsOutputSerializer
    pagination_class = CommonPagination

    def post(self, request):
        """Create a new instance permission."""
        serializer = InstancePermissionInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance_permission = create_instance_premission(**serializer.validated_data, creator=request.user)
        data = self.serializer_class(instance_permission).data
        return Response(data, status=HTTP_201_CREATED)
