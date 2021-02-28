from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.db.utils import IntegrityError

from SoftwareDev import settings
from backend.Utils.points_handler import adjust_points
from backend.Utils.user_validation import verify_user_login
from backend.Utils.paginators import json_paginator
from backend.models import Community, CommunityMember, PointsGained


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


def join_community(request, community_id):
    """
    Join an existing community.
    :param request: session request
    :param community_id: id of community to join
    :return: 200 Joined successfully
             401 Unauthorized
             404 Not found
             409 Conflict
    """
    if not Community.objects.filter(pk=community_id).exists():
        return JsonResponse(
            f'Not found - No community with the id "{community_id}" exists',
            status=404,
            safe=False,
        )

    comm_instance = Community.objects.get(pk=community_id)
    user = request.user

    if CommunityMember.objects.filter(community=comm_instance, user=user).exists():
        return JsonResponse(
            "Conflict - The user is already a member of that community",
            status=409,
            safe=False,
        )

    CommunityMember.objects.create(community=comm_instance, user=user)
    adjust_points(
        user=comm_instance.user,
        points=settings.JOIN_COMMUNITY_PTS,
        community=comm_instance,
    )

    return JsonResponse("Joined successfully", status=200, safe=False)


def leave_community(request, community_id):
    """
    Leave a community
    :param request: session request.
    :param community_id: id of community to leave.
    :return: 200 OK
             401 Unauthorized
             404 Not found
             409 Conflict
    """

    try:
        comm_instance = Community.objects.get(pk=community_id)
    except Community.DoesNotExist:
        return JsonResponse(
            f'Not found - No community with the id "{community_id}" exists',
            status=404,
            safe=False,
        )

    user = request.user

    try:
        comm_member_instance = CommunityMember.objects.get(
            community=comm_instance, user=user
        )
    except CommunityMember.DoesNotExist:
        return JsonResponse(
            "Conflict - The user is not part of that community", status=409, safe=False
        )

    comm_member_instance.delete()
    return JsonResponse("User has left the community", status=200, safe=False)


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
    list_type = request.GET.get("type")
    print(list_type)
    if list_type not in ["all", "created", "memberof"]:
        return JsonResponse(
            "Bad request - Type must be one of: 'all', 'created', 'memberof'",
            status=400,
            safe=False,
        )

    if list_type == "all":
        comms = list(Community.objects.all().order_by("name"))
    elif list_type == "created":
        comms = Community.objects.filter(user=user).order_by("name")
    elif list_type == "memberof":
        comm_mems = CommunityMember.objects.filter(user=user).order_by(
            "community__name"
        )
        comms = [comm_mem.community for comm_mem in comm_mems]

    return JsonResponse(
        json_paginator(request, comms, lambda d: d.serialize_simple()), status=200
    )


def get_community(request, community_id):
    """
    Get a single community.
    :param request: session request
    :param community_id: id of the community to get
    :return: 200 OK
             401 Unauthorized
             404 Not found
    """
    try:
        comm_instance = Community.objects.get(pk=community_id)
    except Community.DoesNotExist:
        return JsonResponse(
            f'Not found - No community with the id "{community_id}" exists',
            status=404,
            safe=False,
        )

    return JsonResponse(comm_instance.serialize(), status=200, safe=True)
