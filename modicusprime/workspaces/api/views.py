from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from modicusprime.states.api.serializers import TransitionOutputSerializer
from modicusprime.utils.common import model_update
from modicusprime.utils.pegination_common import CommonPagination
from modicusprime.workspaces.api.serializers import (
    DocumentInputSerializer,
    DocumentsOutputSerializer,
    WorkspaceContributorsRemoveInputSerializer,
    WorkspaceEditInputSerializer,
    WorkspaceInputSerializer,
    WorkspacesOutputSerializer,
)
from modicusprime.workspaces.models import Document, Workspace
from modicusprime.workspaces.selectors import get_available_transitions_by_state
from modicusprime.workspaces.services import remove_contributors_from_workspace

# Create your views here.


class WorkspacesCreateListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkspacesOutputSerializer
    pagination_class = CommonPagination

    def get_queryset(self):
        return Workspace.objects.filter(user=self.request.user)

    def post(self, request):
        """Create a new workspace."""
        serializer = WorkspaceInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        workspace = Workspace.objects.create(**serializer.validated_data, user=request.user)
        data = self.serializer_class(workspace).data
        return Response(data, status=HTTP_201_CREATED)


class WorkspaceEditDeleteApi(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, workspace_id):
        """Delete a workspace."""
        workspace = get_object_or_404(Workspace, id=workspace_id)
        workspace.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def patch(self, request, workspace_id):
        """Edit a workspace."""
        workspace = get_object_or_404(Workspace, id=workspace_id)
        serializer = WorkspaceEditInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        workspace, _ = model_update(data=serializer.validated_data, instance=workspace)
        data = WorkspacesOutputSerializer(workspace).data
        return Response(data)


class WorkspaceContributorsRemoveApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, workspace_id):
        """Remove a contributor from a workspace."""
        workspace = get_object_or_404(Workspace, id=workspace_id, user=request.user)
        serializer = WorkspaceContributorsRemoveInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        remove_contributors_from_workspace(workspace=workspace, contributors=serializer.validated_data["contributors"])
        return Response(status=HTTP_204_NO_CONTENT)


class WorkspaceAvailableTransitionsListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransitionOutputSerializer
    pagination_class = CommonPagination

    def get_queryset(self):
        workspace = get_object_or_404(Workspace, id=self.kwargs["workspace_id"])
        available_transitions = get_available_transitions_by_state(current_stage=workspace.state)
        return available_transitions


class DocumentsCreateListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentsOutputSerializer
    pagination_class = CommonPagination

    def get_queryset(self):
        return Document.objects.filter(workspace__user=self.request.user)

    def post(self, request):
        """Create a new document."""
        serializer = DocumentInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        workspace = Document.objects.create(**serializer.validated_data)
        data = self.serializer_class(workspace).data
        return Response(data, status=HTTP_201_CREATED)


class DocumentDeleteApi(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, document_id):
        """Delete a workspace."""
        workspace = get_object_or_404(Document, id=document_id)
        workspace.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class DocumentAvailableTransitionsListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransitionOutputSerializer
    pagination_class = CommonPagination

    def get_queryset(self):
        document = get_object_or_404(Document, id=self.kwargs["document_id"])
        available_transitions = get_available_transitions_by_state(current_stage=document.state)
        return available_transitions
