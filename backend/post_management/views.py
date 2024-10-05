from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from .serializers import BlogSerializer, CustomUserSerializer
from .models import Blog
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class BlogPagination(PageNumberPagination):
    """
    Pagination class for paginating blog results.
    
    - **page_size**: Default number of results per page is 6.
    - **page_size_query_param**: Allows specifying the page size in the query parameters.
    - **max_page_size**: Maximum allowed page size is 100.
    """
    page_size = 6
    page_size_query_param = 'page_size' 
    max_page_size = 100  


class BlogCreateView(generics.ListCreateAPIView):
    """
    API view for listing all blogs and creating a new blog.
    
    **GET** /blogs/ - Returns a list of all blogs ordered by creation date.

    **POST** /blogs/ - Creates a new blog with the authenticated user as the author.
    
    **Responses:**
    - 200: Successfully retrieved the list of blogs.
    - 201: Blog created successfully.
    - 400: Bad Request. Validation errors may occur.
    - 403: Forbidden. User not authenticated.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BlogPagination
    
    def get_queryset(self):
        """
        Return all blogs ordered by creation date.
        """
        return Blog.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        """
        Save the blog with the current user as the author.
        """
        serializer.save(author=self.request.user)
        

class ListingMyBlogAPIView(generics.ListAPIView):
    """
    API view for listing blogs authored by the authenticated user.

    **GET** /my-blogs/ - Returns a list of blogs authored by the authenticated user,
    ordered by creation date.

    **Responses:**
    - 200: Successfully retrieved the list of blogs.
    - 403: Forbidden. User not authenticated.
    """
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BlogPagination

    def get_queryset(self):
        """
        Return blogs authored by the current user, ordered by creation date.
        """
        return Blog.objects.filter(author=self.request.user).order_by('-created_at')


class IndividualBlogFetchingView(generics.RetrieveAPIView):
    """
    API view for fetching an individual blog post.

    **GET** /blogs/{id}/ - Returns the blog post with the specified ID.

    **Responses:**
    - 200: Successfully retrieved the blog post.
    - 404: Not Found. The blog post does not exist.
    - 403: Forbidden. User not authenticated.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    
class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating the authenticated user's profile.

    **GET** /user-profile/ - Returns the profile of the authenticated user.

    **PUT** /user-profile/ - Updates the profile of the authenticated user.

    **Responses:**
    - 200: Profile updated successfully.
    - 401: Unauthorized. User not authenticated.
    - 403: Forbidden. User does not have permission to update.
    - 400: Bad Request. Validation errors may occur.
    """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Return the current authenticated user.
        """
        return self.request.user
    
class DeleteMyBlogAPIView(generics.DestroyAPIView):
    """
    API view for deleting a blog authored by the authenticated user.

    **DELETE** /my-blogs/{id}/ - Deletes the specified blog if authored by the authenticated user.

    **Responses:**
    - 204: Successfully deleted the blog.
    - 404: Not Found. The blog does not exist.
    - 403: Forbidden. You do not have permission to delete this blog.
    """
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return blogs authored by the current user.
        """
        return Blog.objects.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        """
        Delete the specified blog if authored by the authenticated user.
        """
        blog = self.get_object()
        if blog.author != request.user:
            return Response({"detail": "You do not have permission to delete this blog."}, status=status.HTTP_403_FORBIDDEN)
        
        return super().delete(request, *args, **kwargs)
    

class BlogUpdateView(generics.UpdateAPIView):
    """
    API view for updating a blog authored by the authenticated user.

    **PUT** /blogs/{id}/ - Updates the specified blog if authored by the authenticated user.

    **Responses:**
    - 200: Blog updated successfully.
    - 404: Not Found. The blog does not exist.
    - 403: Forbidden. User does not have permission to update this blog.
    - 400: Bad Request. Validation errors may occur.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return blogs authored by the current user.
        """
        return Blog.objects.filter(author=self.request.user)

    def perform_update(self, serializer):
        """
        Update the blog instance, maintaining the existing image if not provided.
        """
        instance = serializer.save()

        if not serializer.validated_data.get('image'):
            instance.image = instance.image
            instance.save()
