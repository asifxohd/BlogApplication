from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser

class APITestCase(TestCase):
    """
    Test case for user registration, login, and profile update APIs
    """

    def setUp(self):
        """
        Set up test client and initial test data
        """
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.login_url = reverse('token-obtain-pair')
        self.profile_update_url = reverse('profile-update')
        
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    def test_user_registration(self):
        """
        Test user registration functionality
        """
        new_user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(self.register_url, new_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(username='newuser').exists())

    def test_user_login(self):
        """
        Test user login functionality
        """
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_profile_update(self):
        """
        Test authenticated user profile update functionality
        """
        self.client.force_authenticate(user=self.user)
        
        update_data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com'
        }
        response = self.client.patch(self.profile_update_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updateduser@example.com')

    def test_profile_update_unauthenticated(self):
        """
        Test profile update without authentication
        """
        update_data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com'
        }
        response = self.client.patch(self.profile_update_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
