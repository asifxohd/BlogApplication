from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Blog
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

class BlogAPITestCase(TestCase):
    """
    Test case for the Blog API
    """

    def setUp(self):
        """
        Set up test data and client authentication
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.client.force_authenticate(user=self.user)

        self.blog = Blog.objects.create(
            title='Test Blog',
            short_description='A short description',
            content='This is the content of the test blog.',
            author=self.user
        )

    def test_create_blog(self):
        """
        Test blog creation functionality
        """
        url = reverse('blog-list-create')
        data = {
            'title': 'New Blog',
            'short_description': 'A new blog post',
            'content': 'This is the content of the new blog post.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 2)

    def test_list_blogs(self):
        """
        Test blog listing functionality
        """
        url = reverse('blog-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_my_blogs(self):
        """
        Test retrieving blogs created by the authenticated user
        """
        url = reverse('blog-get-my-blogs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_individual_blog(self):
        """
        Test retrieving a specific blog by its ID
        """
        url = reverse('blog-deatils', kwargs={'id': self.blog.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Blog')

    def test_update_blog(self):
        """
        Test updating a specific blog's details
        """
        url = reverse('update-blog', kwargs={'pk': self.blog.id})
        data = {'title': 'Updated Blog Title'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, 'Updated Blog Title')

    def test_delete_blog(self):
        """
        Test deleting a specific blog
        """
        url = reverse('my-blog-delete', kwargs={'pk': self.blog.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Blog.objects.count(), 0)

    def test_user_profile(self):
        """
        Test retrieving the authenticated user's profile
        """
        url = reverse('user-profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_update_user_profile(self):
        """
        Test updating the authenticated user's profile
        """
        url = reverse('user-profile')
        data = {'username': 'updateduser'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
