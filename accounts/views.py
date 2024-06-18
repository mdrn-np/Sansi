from rest_framework import generics, permissions, views
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import GetJWTTokenSerializer, RegisterSerializer, AccountSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


# Login user
class GetUserToken(views.APIView):
    serializer_class = GetJWTTokenSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = GetJWTTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=HTTP_200_OK)


# Register user
class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": serializer.data,
            },
            status=HTTP_201_CREATED,
        )


class ReadUpdateUser(generics.RetrieveUpdateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
