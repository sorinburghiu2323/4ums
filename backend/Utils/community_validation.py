from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

from backend.Utils.user_validation import verify_user_login
from backend.models import Community, CommunityMember


def get_community(community_id):
    """
    Verify that a community with a given id exists.
    :param community_id: id of test community
    :return: Community instance
    :return: 404 error if doesn't exist
    """
    try:
        return Community.objects.get(pk=community_id)
    except Community.DoesNotExist:
        return


def check_member(community_instance, user_instance):
    """
    Verify that the user is a member of a particular community
    :param community_instance: instance of community to check
    :param user_instance: instance of user to check
    :return: Community instance
    :return: 404 error if doesn't exist
    """
    try:
        return CommunityMember.objects.get(
            user=user_instance, community=community_instance
        )
    except CommunityMember.DoesNotExist:
        return


def check_if_valid(request, community_id):
    """
    Checks if user is logged in and if the community exists
    and the user is a member of both.
    :param request: session request.
    :param community_id: id of the community.
    :return: 201 - Posts have been sent.
             400 - Bad request.
             401 - Unauthorized.
             404 - Not Found - Community not found.
    """
    comm_instance = get_community(community_id)
    if comm_instance is None:
        return JsonResponse("Community does not exist", status=404, safe=False)
    try:
        user_instance = verify_user_login(request)  # Verify that the user exists
    except PermissionDenied:
        return JsonResponse("Unauthorized - Login required.", status=401, safe=False)
    comm_member = check_member(community_id, user_instance)
    if comm_member is None:
        return JsonResponse("User not member of that community", status=401, safe=False)
    return user_instance, comm_instance, comm_member
