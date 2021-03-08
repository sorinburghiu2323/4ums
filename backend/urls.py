from django.http import HttpResponse
from django.urls import path

from backend import views


urlpatterns = [
    path("", lambda _: HttpResponse("", status=200)),
    # Auth.
    path("login", views.login),
    path("logout", views.logout),
    path("login/passwordreset", views.reset_password),
    path("login/sendreset", views.send_email),
    # Users.
    path("users", views.users),
    path("users/feed", views.feed),
    path("users/me", views.users_me),
    path("users/leaderboard", views.leaderboard),
    path("users/<int:user_id>", views.users_individual),
    # Communities.
    path("communities", views.communities),
    path("communities/<int:community_id>", views.community),
    path("communities/<int:community_id>/leave", views.community_leave),
    # Posts.
    path("communities/<int:community_id>/posts", views.posts),
    path("communities/<int:community_id>/posts/<int:post_id>", views.post),
    path(
        "communities/<int:community_id>/posts/<int:post_id>/likes",
        views.post_likes,
    ),
    # Comments.
    path(
        "communities/<int:community_id>/posts/<int:post_id>/comments",
        views.comments,
    ),
    path(
        "communities/<int:community_id>/posts/<int:post_id>/comments/<int:comment_id>/likes",
        views.comment_likes,
    ),
    path(
        "communities/<int:community_id>/posts/<int:post_id>/comments/<int:comment_id>/approve",
        views.comment_approve,
    ),
]
