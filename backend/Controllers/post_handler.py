from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

from backend.Utils.community_validation import get_community, check_member
from backend.Utils.user_validation import verify_user_login
from backend.models import Post


def create_post(request, community_id):
    """
    Create a post.
    :param request: session request.
    :param community_id: id of the community.
    :return: 201 - Post has been created.
             400 - Bad request.
             404 - Not Found - Community not found.
    """
    if (
        "title" in request.DATA
        and "description" in request.DATA
        and "post_type" in request.DATA
    ):
        try:
            user_instance = verify_user_login(request)  # Verify that the user exists
        except PermissionDenied:
            return JsonResponse(
                "Unauthorized - Login required.", status=401, safe=False
            )
        comm_instance = get_community(community_id)
        if comm_instance is None:
            return JsonResponse("Community does not exist", status=404, safe=False)

        comm_member = check_member(community_id, user_instance)
        if comm_member is None:
            return JsonResponse(
                "User not member of that community", status=401, safe=False
            )
        Post.objects.create(
            user=user_instance,
            title=request.DATA["title"],
            description=request.DATA["description"],
            post_type=request.DATA["post_type"],
            community=comm_instance,
        )
        return JsonResponse("Ok - Post has been created.", status=201, safe=False)
    return JsonResponse(
        "Bad Request - Please provide the required body.", status=400, safe=False
    )


def show_post(request, community_id):
    return JsonResponse("Ok - Post", status=200, safe=False)
