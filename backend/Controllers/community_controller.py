from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.db.utils import IntegrityError

from backend.Utils.user_validation import verify_user_login
from backend.Utils.paginators import json_paginator
from backend.models import Community, CommunityMember


def create_new(request):
    """
    Create a new community.
    :param request: session request
    :return: 201 Community created
             400 Bad request
             401 Unauthorized
             409 Conflict
    """

    user_instance = request.user

    if "name" in request.DATA and "description" in request.DATA:
        try:
            new_community = Community.objects.create(
                user=user_instance,
                name=request.DATA["name"],
                description=request.DATA["description"],
            )
        except IntegrityError:
            return JsonResponse(
                "Conflict - Name is already in use", status=409, safe=False
            )

        CommunityMember.objects.create(user=user_instance, community=new_community)

        return JsonResponse("Community created", status=201, safe=False)

    else:
        return JsonResponse(
            "Bad request - Name and description are required", status=400, safe=False
        )


def list_communities(request):
    """
    Get a paginated list of communities.

    Must include 'type' in request body, which should be one of three values:
        - "all"     : all communities
        - "memberof": communities the user is a member of
        - "created" : communities the user created

    :param request: session request
    :return: 200 OK
             400 Bad request - {description of why the request is bad}
             401 Unauthorized - Login required
    """
    user = request.user
    if "type" not in request.DATA:
        return JsonResponse(
            "Bad request - List type is required", status=400, safe=False
        )

    list_type = request.DATA["type"]

    if list_type not in ["all", "created", "memberof"]:
        return JsonResponse(
            "Bad request - Type must be one of: 'all', 'created', 'memberof'",
            status=400,
            safe=False,
        )

    if list_type == "all":
        comms = list(Community.objects.all().order_by("-name"))
    elif list_type == "created":
        comms = Community.objects.filter(user=user).order_by("-name")
    elif list_type == "memberof":
        comm_mems = CommunityMember.objects.filter(user=user).order_by("-community")
        comms = [comm_mem.community for comm_mem in comm_mems]

    return JsonResponse(
        json_paginator(request, comms, lambda d: d.serialize_simple()), status=200
    )
