
from rest_framework import generics, status,permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .serializers import SignupSerializer, UpdateUserSerializer, UserSerializer, UserWithTokenSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token_serializer = UserWithTokenSerializer(user)
            return Response(token_serializer.data)
        return Response({'detail': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class GetUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UpdateUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user