from django.http import HttpResponse
from django.urls import path

from backend import views

# Create your API urls here.


urlpatterns = [
    path("", lambda _: HttpResponse("", status=200)),
    path("login", views.login),
    path("logout", views.logout),
    path("communities/<int:community_id>/post", views.create_post),
    path("users", views.users),
]
