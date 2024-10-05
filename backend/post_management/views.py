from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from .serializers import BlogSerializer, CustomUserSerializer
from .models import Blog
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class BlogPagination(PageNumberPagination):
    """
    Pagination class for paginating blog results
    """
    page_size = 6
    page_size_query_param = 'page_size' 
    max_page_size = 100  


class BlogCreateView(generics.ListCreateAPIView):
    """
    View for listing all blogs and creating a new blog
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BlogPagination
    
    def get_queryset(self):
        """
        Return all blogs ordered by creation date
        """
        return Blog.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        """
        Save the blog with the current user as the author
        """
        serializer.save(author=self.request.user)
        

class ListingMyBlogAPIView(generics.ListAPIView):
    """
    View for listing blogs authored by the authenticated user
    """
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BlogPagination

    def get_queryset(self):
        """
        Return blogs authored by the current user, ordered by creation date
        """
        return Blog.objects.filter(author=self.request.user).order_by('-created_at')


class IndividualBlogFetchingView(generics.RetrieveAPIView):
    """
    View for fetching an individual blog post
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    
class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    View for retrieving and updating the authenticated user's profile
    """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Return the current authenticated user
        """
        return self.request.user
    
class DeleteMyBlogAPIView(generics.DestroyAPIView):
    """
    View for deleting a blog authored by the authenticated user
    """
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return blogs authored by the current user
        """
        return Blog.objects.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        """
        Delete the specified blog if authored by the authenticated user
        """
        blog = self.get_object()
        if blog.author != request.user:
            return Response({"detail": "You do not have permission to delete this blog."}, status=status.HTTP_403_FORBIDDEN)
        
        return super().delete(request, *args, **kwargs)
    

class BlogUpdateView(generics.UpdateAPIView):
    """
    View for updating a blog authored by the authenticated user
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return blogs authored by the current user
        """
        return Blog.objects.filter(author=self.request.user)

    def perform_update(self, serializer):
        """
        Update the blog instance, maintaining the existing image if not provided
        """
        instance = serializer.save()

        if not serializer.validated_data.get('image'):
            instance.image = instance.image
            instance.save()
