from django.views.decorators.csrf import csrf_exempt

from backend.Controllers import (
    community_controller,
    user_controller,
    post_handler,
    comment_controller,
)
from backend.Utils.http_method_handler import handle_methods
from backend.Utils.user_validation import user_login_required


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
def users(request):
    return handle_methods(
        request,
        POST=user_controller.user_register,
    )


@csrf_exempt
def posts(request, community_id):
    return handle_methods(
        request,
        POST=post_handler.create_post,
        GET=post_handler.show_posts,
        args=[community_id],
    )


@csrf_exempt
def post(request, community_id, post_id):
    return handle_methods(
        request,
        GET=post_handler.show_post,
        args=[community_id, post_id],
    )


@csrf_exempt
def feed(request):
    return handle_methods(
        request,
        GET=user_controller.get_feed,
    )


@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def communities(request):
    return handle_methods(
        request,
        POST=community_controller.create_new,
        GET=community_controller.list_communities,
    )


@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def post_likes(request, community_id, post_id):
    return handle_methods(
        request,
        POST=post_handler.like_post,
        DELETE=post_handler.unlike_post,
        args=[community_id, post_id],
    )


@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def comment_likes(request, community_id, post_id, comment_id):
    return handle_methods(
        request,
        POST=comment_controller.like_comment,
        DELETE=comment_controller.unlike_comment,
        args=[community_id, post_id, comment_id],
    )


@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def community(request, community_id):
    return handle_methods(
        request,
        POST=community_controller.join_community,
        GET=community_controller.get_community,
        args=[community_id],
    )


@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def community_leave(request, community_id):
    return handle_methods(
        request,
        POST=community_controller.leave_community,
        args=[community_id],
    )


@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def comments(request, community_id, post_id):
    return handle_methods(
        request,
        POST=comment_controller.make_comment,
        args=[community_id, post_id],
    )


@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def comment_approve(request, community_id, post_id, comment_id):
    return handle_methods(
        request,
        POST=comment_controller.approve_comment,
        DELETE=comment_controller.disapprove_comment,
        args=[community_id, post_id, comment_id],
    )


@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def users_me(request):
    return handle_methods(
        request,
        GET=user_controller.get_user(request, request.user.id),
        PUT=user_controller.update_me,
    )


@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def users_individual(request, user_id):
    return handle_methods(
        request,
        GET=user_controller.get_user,
        args=[user_id],
    )

@user_login_required("Unauthorized - Login required.")
@csrf_exempt
def leaderboard(request):
    return handle_methods(request, GET=user_controller.get_leaderboard)
