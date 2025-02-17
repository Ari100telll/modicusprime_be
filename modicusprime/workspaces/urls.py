from django.urls import path

from modicusprime.workspaces.api.views import WorkspacesCreateListApi, DocumentsCreateListApi, DocumentDeleteApi, \
    WorkspaceDeleteApi, WorkspaceAvailableTransitionsListApi, DocumentAvailableTransitionsListApi

app_name = "workspaces"

urlpatterns = [
    path("", WorkspacesCreateListApi.as_view(), name="workspaces-create-list"),
    path("<uuid:workspace_id>/", WorkspaceDeleteApi.as_view(), name="workspaces-delete"),
    path(
        "<uuid:workspace_id>/available-transitions/",
        WorkspaceAvailableTransitionsListApi.as_view(),
        name="workspaces-available-transitions-list"
    ),
    path("documents/", DocumentsCreateListApi.as_view(), name="documents-create-list"),
    path("documents/<uuid:document_id>/", DocumentDeleteApi.as_view(), name="documents-delete"),
    path(
        "documents/<uuid:document_id>/available-transitions/",
        DocumentAvailableTransitionsListApi.as_view(),
        name="documents-available-transitions-list"
    ),
]
