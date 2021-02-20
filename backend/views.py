from django.views.decorators.csrf import csrf_exempt

from backend.Controllers import user_controller, post_handler
from backend.Utils.http_method_handler import handle_methods


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


@csrf_exempt
def create_post(request, community_id):
    return handle_methods(
        request,
        POST=post_handler.create_post,
        GET=post_handler.show_post,
        args=[community_id],
    )


# USER VIEWS


@csrf_exempt
def users(request):
    return handle_methods(
        request,
        POST=user_controller.user_register,
    )


@csrf_exempt
def feed(request):
    return handle_methods(
        request,
        GET=user_controller.get_feed,
    )
