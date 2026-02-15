from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path("posts/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="new_comment"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="edit_comment"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete_comment"),
]






from django.urls import path
from .views import PostByTagListView

urlpatterns = [
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts_by_tag"),
    # other URL patterns...
]






from django.urls import path
from . import views

urlpatterns = [
    path("posts/<int:post_id>/comments/new/", views.new_comment, name="new_comment"),
    path("comments/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
    path("comments/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
]
