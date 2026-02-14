from django.urls import path
from . import views

urlpatterns = [
    path("posts/<int:post_id>/comments/new/", views.new_comment, name="new_comment"),
    path("comments/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
    path("comments/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
]
