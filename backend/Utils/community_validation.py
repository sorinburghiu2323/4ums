from django.shortcuts import get_object_or_404

from backend.models import Community, CommunityMember


def get_community(community_id):
    """
    Verify that a community with a given id exists.
    :param community_id: id of test community
    :return: Community instance
    :return: 404 error if doesn't exist
    """
    return get_object_or_404(Community, pk=community_id)


def check_member(community_instance, user_instance):
    """
    Verify that the user is a member of a particular community
    :param community_instance: instance of community to check
    :param user_instance: instance of user to check
    :return: Community instance
    :return: 404 error if doesn't exist
    """
    return get_object_or_404(
        CommunityMember, user=user_instance, community=community_instance
    )
