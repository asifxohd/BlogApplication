from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    UserRegistrationSerializer,
    CustomTokenObtainPairSerializer,
    UserProfileUpdateSerializer,
)
from .models import CustomUser


class UserRegistrationView(generics.CreateAPIView):
    """
    View for user registration
    """

    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    View for obtaining JWT token pair
    """

    serializer_class = CustomTokenObtainPairSerializer


class UserProfileUpdateView(generics.UpdateAPIView):
    """
    View for updating the authenticated user's profile information
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Return the current authenticated user
        """
        return self.request.user
