from django.views.decorators.csrf import csrf_exempt

from backend.Controllers import user_controller, post_creator
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
        POST=post_creator.create_post,
        args=[community_id],
    )
