
from backend.models import User

def get_leaderboard_info():
    """Get the leaderboard; each user sorted by points. Including their rank."""

    includedUsers = Users.objects.filter(hide_leaderboard=False, is_staff=False)

    # ordered list of points, index denoting leaderboard position (rank)
    # distinct values means that everyone with the same points has the same rank
    rankings = []
    for item in includedUsers.values("points").distinct().order_by("-points"):
        rankings.append(item["points"])

    includedUsers = includedUsers.order_by("-points")

    paginationData = []
    for user in includedUsers:
        # rank is the index of the users points +1 (converting from 0-indexing)
        data = {'user': user, 'rank': rankings.index(user.points) + 1}
        paginationaData.append(data)

    return paginationData
