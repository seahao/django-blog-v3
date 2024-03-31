from django.urls import path
from blogging.views import PostListView, PostDetailView, add_modelform

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
    path("add/", add_modelform, name="add_post"),
]
