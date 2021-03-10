import json

from django.test import TestCase

from backend.models import User, Community, CommunityMember


class CommunityListEndpointTest(TestCase):
    """
    Test community get endpoints.
    """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testy", email="test@4ums.co.uk", password="abc"
        )
        success = self.client.login(username="test@4ums.co.uk", password="abc")
        assert success

    def test_auth_401(self):
        """Test that the endpoint requires login."""

        self.client.logout()  # setUp includes login

        response = self.client.get("/api/communities")
        self.assertEqual(401, response.status_code)

    def test_get_400(self):
        """Test that the endpoint requires "type" in the body."""

        response = self.client.get("/api/communities")
        self.assertEqual(400, response.status_code)

    def test_get_invalid_400(self):
        """Test that the endpoint requires "type" to be a specific value."""

        response = self.client.get("/api/communities", {"type": "banana"})
        self.assertEqual(400, response.status_code)

    def test_get_valid_other(self):
        """Test that the endpoint returns the expected list."""

        Community.objects.create(
            user=self.user, name="lorem", description="lorem ipsum ..."
        )
        other_user = User.objects.create(
            username="bob", email="bob@4ums.co.uk", password="opensaysame"
        )
        Community.objects.create(
            user=other_user,
            name="bobgang",
            description="Bob's gang (cool kids only)",
        )

        response = self.client.get("/api/communities", {"type": "other"})
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content.decode())
        expected = [
            {
                "id": 2,
                "name": "bobgang",
                "description": "Bob's gang (cool kids only)",
                "colour": None,
            },
            {
                "id": 1,
                "name": "lorem",
                "description": "lorem ipsum ...",
                "colour": None,
            },
        ]

        self.assertEqual(2, len(result["data"]))
        self.assertEqual(expected, result["data"])

    def test_get_valid_created(self):
        """Test that the endpoint returns the expected list."""

        Community.objects.create(
            user=self.user, name="lorem", description="lorem ipsum ..."
        )
        other_user = User.objects.create(
            username="bob", email="bob@4ums.co.uk", password="opensaysame"
        )
        Community.objects.create(
            user=other_user,
            name="bobgang",
            description="Bob's gang (cool kids only)",
        )

        response = self.client.get("/api/communities", {"type": "created"})
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content.decode())

        expected = {
            "id": 1,
            "name": "lorem",
            "description": "lorem ipsum ...",
            "colour": None,
        }

        self.assertEqual(1, len(result["data"]))
        self.assertEqual(expected, result["data"][0])

    def test_get_valid_member(self):
        """Test that the endpoint returns the expected list."""

        comm_instance1 = Community.objects.create(
            user=self.user, name="lorem", description="lorem ipsum ..."
        )
        CommunityMember.objects.create(user=self.user, community=comm_instance1)
        other_user = User.objects.create(
            username="bob", email="bob@4ums.co.uk", password="opensaysame"
        )
        comm_instance2 = Community.objects.create(
            user=other_user,
            name="bobgang",
            description="Bob's gang (cool kids only)",
        )

        # check that only one community (lorem) is returned
        response = self.client.get("/api/communities", {"type": "memberof"})
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content.decode())
        expected = {
            "id": 1,
            "name": "lorem",
            "description": "lorem ipsum ...",
            "colour": None,
        }

        self.assertEqual(1, len(result["data"]))
        self.assertEqual(expected, result["data"][0])

        # add the user as a member of the other community (bobgang)
        CommunityMember.objects.create(user=self.user, community=comm_instance2)

        # check that both are returned
        response = self.client.get("/api/communities", {"type": "memberof"})
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content.decode())
        expected = [
            {
                "id": 2,
                "name": "bobgang",
                "description": "Bob's gang (cool kids only)",
                "colour": None,
            },
            {
                "id": 1,
                "name": "lorem",
                "description": "lorem ipsum ...",
                "colour": None,
            },
        ]

        self.assertEqual(2, len(result["data"]))
        self.assertEqual(expected, result["data"])
