import json

from django.test import TestCase

from backend.models import User, Community, Post, CommunityMember


class PostListEndpointTest(TestCase):
    """
    Test post get endpoints.
    """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testy", email="test@4ums.co.uk", password="abc"
        )
        self.community = Community.objects.create(name="New", description="Na")
        CommunityMember.objects.create(user=self.user, community=self.community)
        success = self.client.login(username="test@4ums.co.uk", password="abc")
        assert success

    def test_auth_401(self):
        """
        Test that the endpoint requires login.
        """
        self.client.logout()  # setUp includes login
        response = self.client.get("/api/communities/1/posts")
        self.assertEqual(401, response.status_code)

    def test_not_member_403(self):
        """
        Test 403 error case.
        """
        CommunityMember.objects.get(
            user=self.user, community=self.community
        ).delete()
        response = self.client.get("/api/communities/1/posts")
        self.assertEqual(403, response.status_code)

    def test_not_found_404(self):
        """
        Test 404 error case.
        """
        response = self.client.get("/api/communities/2/posts")
        self.assertEqual(404, response.status_code)

    def test_get_community_posts(self):
        """
        Test get community posts endpoint.
        """
        post_1 = Post.objects.create(
            user=self.user,
            community=self.community,
            title="Test",
            description="Hello",
            post_type="discussion",
            created_at="2021-03-10T12:54:56.291Z",
        )
        post_2 = Post.objects.create(
            user=self.user,
            community=self.community,
            title="Test2",
            description="hello",
            post_type="discussion",
            created_at="2021-03-10T12:54:56.291Z",
        )

        # Test 200 response.
        response = self.client.get("/api/communities/1/posts")
        self.assertEqual(200, response.status_code)

        expected = [
            post_1.serialize(response.wsgi_request),
            post_2.serialize(response.wsgi_request),
        ]
        result = json.loads(response.content.decode())

        self.assertEqual(2, len(result["data"]))
        self.assertEqual(expected, result["data"])
