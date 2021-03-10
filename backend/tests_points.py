from django.test import TestCase

from backend.Utils.points_handler import (
    graph_recent,
    graph_top_communities,
    adjust_points,
)
from backend.models import PointsGained, User, Community, CommunityMember


class PointSystemTesting(TestCase):
    """
    Test the point system and graph generation.
    """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testy", email="test@4ums.co.uk", password="abc"
        )
        success = self.client.login(username="test@4ums.co.uk", password="abc")
        assert success

    def test_adjust_points(self):
        """
        Test adjust point functionality.
        """
        adjust_points(user=self.user, points=20)
        adjust_points(user=self.user, points=30)
        self.assertEqual(self.user.points, 50)

    def test_recent_graph(self):
        """
        Test for the most recent points graph.
        """
        point_list = [
            PointsGained.objects.create(user=self.user, points=20),
            PointsGained.objects.create(user=self.user, points=30),
        ]
        expected = [
            {
                "name": "Current week",
                "points": 50,
            },
            {
                "name": "Last week",
                "points": 0,
            },
            {
                "name": "Last 2 weeks",
                "points": 0,
            },
            {
                "name": "Last 3 weeks",
                "points": 0,
            },
        ]
        self.assertEqual(expected, graph_recent(point_list))

    def test_graph_top_communities(self):
        """
        Test for the top communities graph.
        """
        comm = Community.objects.create(
            user=self.user, name="lorem", description="lorem ipsum ..."
        )
        CommunityMember.objects.create(user=self.user, community=comm)
        PointsGained.objects.create(user=self.user, community=comm, points=20)
        PointsGained.objects.create(user=self.user, community=comm, points=30)
        point_list = PointsGained.objects.filter(user=self.user)
        expected = [
            {
                "community": comm.serialize_simple(),
                "points": 50,
            }
        ]
        self.assertEqual(expected, graph_top_communities(point_list, self.user))
