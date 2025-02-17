from django.urls import path

from modicusprime.states.api.views import (
    StatesCreateListApi,
    StatesDeleteApi,
    StatesGroupsCreateListApi,
    StatesGroupsDeleteApi,
    TransitionCreateListApi,
    TransitionDeleteApi,
    TransitionRequestCreateListApi,
)

app_name = "states"

urlpatterns = [
    path("", StatesCreateListApi.as_view(), name="states-create-list"),
    path("<uuid:state_id>/", StatesDeleteApi.as_view(), name="state-delete"),
    path("groups/", StatesGroupsCreateListApi.as_view(), name="state-groups-create-list"),
    path("groups/<uuid:state_group_id>/", StatesGroupsDeleteApi.as_view(), name="state-groups-delete"),
    path("transitions/", TransitionCreateListApi.as_view(), name="transitions-create-list"),
    path("transitions/<uuid:transition_id>/", TransitionDeleteApi.as_view(), name="transitions-delete"),
    path("transitions-requests/", TransitionRequestCreateListApi.as_view(), name="transitions-requests-create-list"),
]
