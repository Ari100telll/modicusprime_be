from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from modicusprime.states.api.serializers import (
    StateInputSerializer,
    StateOutputSerializer,
    StatesGroupInputSerializer,
    StatesGroupOutputSerializer,
    TransitionInputSerializer,
    TransitionOutputSerializer,
    TransitionRequestActionLogOutputSerializer,
    TransitionRequestInputSerializer,
    TransitionRequestOutputSerializer,
)
from modicusprime.states.models import (
    StateDefinition,
    StatesGroup,
    Transition,
    TransitionRequest,
    TransitionRequestActionLog,
)
from modicusprime.states.services import create_transition, create_transition_request
from modicusprime.utils.pegination_common import CommonPagination

# Create your views here.


class StatesCreateListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StateDefinition.objects.all()
    serializer_class = StateOutputSerializer
    pagination_class = CommonPagination

    def post(self, request):
        """Create a new state defenition."""
        serializer = StateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        state = StateDefinition.objects.create(**serializer.validated_data)
        data = self.serializer_class(state).data
        return Response(data, status=HTTP_201_CREATED)


class StatesDeleteApi(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, state_id):
        """Delete a state defenition."""
        state = get_object_or_404(StateDefinition, id=state_id)
        state.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class StatesGroupsCreateListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StatesGroup.objects.all()
    serializer_class = StatesGroupOutputSerializer
    pagination_class = CommonPagination

    def post(self, request):
        """Create a new state group."""
        serializer = StatesGroupInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        state = StatesGroup.objects.create(**serializer.validated_data)
        data = self.serializer_class(state).data
        return Response(data, status=HTTP_201_CREATED)


class StatesGroupsDeleteApi(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, state_group_id):
        """Delete a state group."""
        state = get_object_or_404(StatesGroup, id=state_group_id)
        state.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class TransitionCreateListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Transition.objects.all()
    serializer_class = TransitionOutputSerializer
    pagination_class = CommonPagination

    def post(self, request):
        """Create a new transition."""
        serializer = TransitionInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transition = create_transition(**serializer.validated_data)
        data = self.serializer_class(transition).data
        return Response(data, status=HTTP_201_CREATED)


class TransitionDeleteApi(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, transition_id):
        """Delete a transition."""
        transition = get_object_or_404(Transition, id=transition_id)
        transition.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class TransitionRequestCreateListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransitionRequestOutputSerializer
    pagination_class = CommonPagination

    def get_queryset(self):
        return TransitionRequest.objects.filter(user=self.request.user)

    def post(self, request):
        """Create a new transition request."""
        serializer = TransitionRequestInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transition_request = create_transition_request(**serializer.validated_data, user=request.user)
        data = self.serializer_class(transition_request).data
        return Response(data, status=HTTP_201_CREATED)


class TransitionRequestListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TransitionRequestActionLog.objects.all()
    serializer_class = TransitionRequestActionLogOutputSerializer
    pagination_class = CommonPagination
