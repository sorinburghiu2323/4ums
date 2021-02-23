import json

from django.test import TestCase

from backend.Utils.user_validation import validate_user_data, validate_password
from backend.models import User, Community, CommunityMember


class UserValidationTesting(TestCase):
    """
    Test user validation cases.
    """

    def test_user_data_validator(self):
        """
        Test validate_user_data(..) function.
        """

        # Test case from when validation passes.
        test_validation = validate_user_data(
            first_name="John",
            last_name="Smith",
            email="johns@gmail.com",
            username="unique_username",
        )
        self.assertEqual(test_validation, False)

        # Test case for when email returns a string error.
        test_validation_wrong = validate_user_data(
            first_name="John",
            last_name="Smith",
            email="not_an_email_address",
            username="unique_username",
        )
        self.assertEqual(
            test_validation_wrong, "Email cannot be empty and must be valid."
        )

    def test_password_validator(self):
        """
        Test validate_password(..) function.
        """

        # Test validation a adequate password.
        password_validation = validate_password(
            password="Password1!",
            password_repeat="Password1!",
        )
        self.assertEqual(password_validation, False)

        # Test validating 2 different passwords.
        password_validation_wrong = validate_password(
            password="Password1!",
            password_repeat="not_the_same_password",
        )
        self.assertEqual(password_validation_wrong, "Passwords did not match.")


class CommunityListEndpointTest(TestCase):
    def getWithData(self, url, data):
        json_data = json.dumps(data)
        return self.client.generic(
            "GET", url, data=json_data.encode(), content_type="application/json"
        )

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

        response = self.getWithData("/api/communities", {"type": "banana"})
        self.assertEqual(400, response.status_code)

    def test_get_valid_all(self):
        """Test that the endpoint returns the expected list."""

        Community.objects.create(
            user=self.user, name="lorem", description="lorem ipsum ..."
        )
        other_user = User.objects.create(
            username="bob", email="bob@4ums.co.uk", password="opensaysame"
        )
        Community.objects.create(
            user=other_user, name="bobgang", description="Bob's gang (cool kids only)"
        )

        response = self.getWithData("/api/communities", {"type": "all"})
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content.decode())
        expected = [
            {"id": 2, "name": "bobgang", "description": "Bob's gang (cool kids only)"},
            {
                "id": 1,
                "name": "lorem",
                "description": "lorem ipsum ...",
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
            user=other_user, name="bobgang", description="Bob's gang (cool kids only)"
        )

        response = self.getWithData("/api/communities", {"type": "created"})
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content.decode())

        expected = {"id": 1, "name": "lorem", "description": "lorem ipsum ..."}

        self.assertEqual(1, len(result["data"]))
        self.assertEqual(expected, result["data"][0])

    def test_get_valid_member(self):
        """Test that the endpooint returns the expected list."""

        comm_instance1 = Community.objects.create(
            user=self.user, name="lorem", description="lorem ipsum ..."
        )
        CommunityMember.objects.create(user=self.user, community=comm_instance1)
        other_user = User.objects.create(
            username="bob", email="bob@4ums.co.uk", password="opensaysame"
        )
        comm_instance2 = Community.objects.create(
            user=other_user, name="bobgang", description="Bob's gang (cool kids only)"
        )

        # check that only one community (lorem) is returned
        response = self.getWithData("/api/communities", {"type": "memberof"})
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content.decode())
        expected = {"id": 1, "name": "lorem", "description": "lorem ipsum ..."}

        self.assertEqual(1, len(result["data"]))
        self.assertEqual(expected, result["data"][0])

        # add the user as a member of the other community (bobgang)
        CommunityMember.objects.create(user=self.user, community=comm_instance2)

        # check that both are returned
        response = self.getWithData("/api/communities", {"type": "memberof"})
        self.assertEqual(200, response.status_code)

        result = json.loads(response.content.decode())
        expected = [
            {"id": 2, "name": "bobgang", "description": "Bob's gang (cool kids only)"},
            {
                "id": 1,
                "name": "lorem",
                "description": "lorem ipsum ...",
            },
        ]

        self.assertEqual(2, len(result["data"]))
        self.assertEqual(expected, result["data"])
