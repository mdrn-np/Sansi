from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import PermissionDenied
from .permissions import IsOwner
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = TodoSerializer
    permission_classes = [IsOwner]
    lookup_field = "pk"
    lookup_url_kwarg = "id"
    lookup_value_regex = "[0-9]+"

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Authentication credentials were not provided.")
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=True, methods=["post"])
    def complete(self, request, id=None):
        todo = Todo.objects.get(pk=id)
        todo.completed = not todo.completed
        todo.save()
        return Response(
            {"status": "todo marked as complete"}, status=status.HTTP_200_OK
        )
