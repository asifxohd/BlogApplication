from django.urls import path
from .views import (
    BlogCreateView,
    ListingMyBlogAPIView,
    IndividualBlogFetchingView,
    UserProfileAPIView,
    DeleteMyBlogAPIView,
    BlogUpdateView
)

urlpatterns = [
    path("blogs/", BlogCreateView.as_view(), name="blog-list-create"),
    path("get-my-blogs/", ListingMyBlogAPIView.as_view(), name="blog-get-my-blogs"),
    path("get-blog/<int:id>", IndividualBlogFetchingView.as_view(), name="blog-deatils"),
    path("user-profile/", UserProfileAPIView.as_view(), name="user-profile"),
    path("my-blogs/<int:pk>/", DeleteMyBlogAPIView.as_view(), name="my-blog-delete"),
    path('update-blog/<int:pk>/', BlogUpdateView.as_view(), name='update-blog'),

]
