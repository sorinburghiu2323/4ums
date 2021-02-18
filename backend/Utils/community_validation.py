from django.shortcuts import get_object_or_404

from backend.models import Community


def get_community(community_id):
    """
    Verify that a community with a given id exists.
    :param community_id: id of test community
    :return: Community instance
    :return: 404 error if doesn't exist
    """
    return get_object_or_404(Community, pk=community_id)
