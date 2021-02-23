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
