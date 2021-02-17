from django.http import HttpResponse
from django.urls import path, include
from backend import views

# Create your API urls here.


urlpatterns = [
    path("", lambda _: HttpResponse("", status=200)),
    path("login", views.login),
    path("logout", views.logout),
    path("users", views.users),
]
