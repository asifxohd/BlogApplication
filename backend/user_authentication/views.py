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
    User Registration API.
    
    This endpoint allows a new user to register.

    **POST** /register/
    
    Request Body:
    - **username**: The desired username (string, required).
    - **email**: The user's email address (string, required).
    - **password**: The user's password (string, required).
    
    Responses:
    - **201**: User created successfully.
    - **400**: Bad Request. Validation errors may occur.
    """
    
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Obtain JWT Token Pair API.
    
    This endpoint allows users to obtain a pair of access and refresh tokens.

    **POST** /token/
    
    Request Body:
    - **username**: The user's username (string, required).
    - **password**: The user's password (string, required).
    
    Responses:
    - **200**: Token pair obtained successfully.
    - **401**: Unauthorized. Invalid credentials.
    """
    
    serializer_class = CustomTokenObtainPairSerializer


class UserProfileUpdateView(generics.UpdateAPIView):
    """
    User Profile Update API.
    
    This endpoint allows the authenticated user to update their profile information.

    **PUT** /user-profile/
    
    Request Body:
    - **username**: The new username (string, required).
    - **email**: The new email address (string, required).
    
    Responses:
    - **200**: Profile updated successfully.
    - **401**: Unauthorized. User not authenticated.
    - **403**: Forbidden. User does not have permission to update.
    - **400**: Bad Request. Validation errors may occur.
    """
    
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Return the current authenticated user.
        """
        return self.request.user
