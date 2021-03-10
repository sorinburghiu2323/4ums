"""Unit tests for user validation functions."""

from django.test import TestCase

from backend.Utils.user_validation import validate_user_data, validate_password


class TestUserValidation(TestCase):
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
