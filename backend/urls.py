from django.urls import path, include
from backend import views

urlpatterns = [
    path("potato", views.potato_view),
]
