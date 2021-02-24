from django.http import HttpResponse
from django.urls import path

from backend import views

# Create your API urls here.


urlpatterns = [
    path("", lambda _: HttpResponse("", status=200)),
    path("login", views.login),
    path("logout", views.logout),
    path("communities/<int:community_id>/posts/<int:post_id>", views.post),
    path("communities/<int:community_id>/posts", views.posts),
    path("users", views.users),
    path("users/feed", views.feed),
    path("communities", views.communities),
    path("communities/<int:community_id>/posts/<int:post_id>/likes", views.post_likes),
    path("communities/<int:community_id>/post/<int:post_id>/comments", views.comments),
    path(
        "communities/<int:community_id>/posts/<int:post_id>/comments/<int:comment_id>/likes",
        views.comment_likes,
    ),
    path("communities/<int:community_id>", views.community),
]
