from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from backend.Controllers import user_controller
from backend.Utils.http_method_handler import handle_methods
from django.http import HttpResponse


# AUTH VIEWS


@csrf_exempt
def login(request):
    return handle_methods(
        request,
        POST=user_controller.user_login,
    )


@csrf_exempt
def logout(request):
    return handle_methods(
        request,
        POST=user_controller.user_logout,
    )
