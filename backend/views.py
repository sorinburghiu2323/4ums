from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from backend.Controllers import user_controller
from backend.Utils.http_method_handler import handle_methods
from django.http import HttpResponse

# Create your views here.


def get_helloworld(request):

    return HttpResponse("<html><body><p>hello world!</p></body></html>")


@csrf_exempt
def helloworld_page(request):
    return handle_methods(request, GET=get_helloworld)


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
