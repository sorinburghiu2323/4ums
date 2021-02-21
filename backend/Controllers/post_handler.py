from django.http import JsonResponse

from backend.Utils.community_validation import (
    check_if_valid,
)
from backend.Utils.paginators import json_paginator
from backend.models import Post


def create_post(request, community_id):
    """
    Create a post.
    :param request: session request.
    :param community_id: id of the community.
    :return: 201 - Post has been created.
             400 - Bad request.
             401 - Unauthorized.
             404 - Not Found - Community not found.
    """
    if (
        "title" in request.DATA
        and "description" in request.DATA
        and "post_type" in request.DATA
    ):
        try:
            user_instance, comm_instance, comm_member = check_if_valid(
                request, community_id
            )
        except ValueError:
            return check_if_valid(request, community_id)
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
    """
    Create a post.
    :param request: session request.
    :param community_id: id of the community.
    :return: 201 - Post has been created.
             400 - Bad request.
             401 - Unauthorized.
             404 - Not Found - Community not found.
    """
    try:  # Check if valid request
        user_instance, comm_instance, comm_member = check_if_valid(
            request, community_id
        )
    except ValueError:
        return check_if_valid(request, community_id)
    # Return pagination data
    store = Post.objects.filter(community=comm_instance).order_by("-created_at")
    return JsonResponse(json_paginator(request, store), status=200, safe=False)
