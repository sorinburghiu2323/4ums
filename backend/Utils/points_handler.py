from django.db.models import Sum
from django.utils import timezone

from backend.models import User, Community, Post, PostComment, PointsGained


def adjust_points(
    user: User,
    points: int,
    community: Community = None,
    post: Post = None,
    comment: PostComment = None,
):
    """
    Method to create a PointsGained record and adjust the points of the user.
    :param user: User instance to adjust points for.
    :param points: Points to be added to the user's current total (this can be negative!).
    :param community: (optional) Community instance for record.
    :param post: (optional) Post instance for record.
    :param comment: (optional) Comment instance for record.
    """
    PointsGained.objects.create(
        user=user,
        points=points,
        community=community,
        post=post,
        comment=comment,
    )
    user.points += points
    user.save()


def graph_recent(points_gained: [PointsGained]):
    """
    Calculate the points gained in the last 4 weeks.
    :param points_gained: list of PointsGained instances.
    :return: graph list
    """
    now = timezone.now()
    w1, w2, w3, w4 = 0, 0, 0, 0  # Initialize variables for each week
    for pg in points_gained:
        days_difference = (now - pg.created_at).days
        if days_difference <= 7:
            w1 += pg.points
        elif days_difference <= 14:
            w2 += pg.points
        elif days_difference <= 21:
            w3 += pg.points
        elif days_difference <= 28:
            w4 += pg.points
    graph = [
        {
            "name": "Current week",
            "points": w1,
        },
        {
            "name": "Last week",
            "points": w2,
        },
        {
            "name": "Last 2 weeks",
            "points": w3,
        },
        {
            "name": "Last 3 weeks",
            "points": w4,
        },
    ]
    return graph


def graph_top_communities(points_gained: [PointsGained], user: User):
    """
    Calculate top 3 communities for a user.
    :param points_gained: list of PointsGained instances.
    :param user: User instance.
    :return: list with top 3 communities and points.
    """
    community_list = []
    communities = Community.objects.filter(
        communitymember__user=user
    )  # Get communities user is part of
    for comm in communities:
        comm_pts = points_gained.filter(community=comm).aggregate(Sum("points"))
        community_list.append(
            {
                "community": comm.serialize_simple(),
                "points": comm_pts["points__sum"] if comm_pts["points__sum"] else 0,
            }
        )
    communities_top = sorted(community_list, key=lambda k: -k["points"])[:3]
    return communities_top


def get_graphs(user: User):
    """
    Generate graph for user profile.
    :param user: User instance.
    :return: graph dict.
    """
    points_gained = PointsGained.objects.filter(user=user)
    graph_data = {
        "recent": graph_recent(points_gained),
        "top_communities": graph_top_communities(points_gained, user),
    }
    return graph_data
