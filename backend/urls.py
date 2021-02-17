from django.urls import path, include
from backend import views

# Create your API urls here.


urlpatterns = [
    path("helloworld", views.helloworld_page),
    path("login", views.login),
    path("logout", views.logout),
]
