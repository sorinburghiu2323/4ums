import re

from django.core.exceptions import PermissionDenied

from backend.models import User


def verify_user_login(request):
    """
    Verify that the user is logged in. Run this function before any endpoint that requires a user to be logged in.
    Example use:

        try:
            user = verify_user_login(request)
            # Perform actions that require a user.
        except PermissionDenied:
            return JsonResponse("Unauthorized - Login required.", status=401, safe=False)

    :param request: session request
    :return: user - User instance.
    :raise: PermissionDenied - user is not logged in.
    """
    user = request.user
    if user.is_authenticated:
        return user
    raise PermissionDenied("Account does not exist.")


def validate_user_data(first_name, last_name, email, username):
    """
    Check if user data for registering is adequate. Return string message otherwise.
    :param first_name: string - user's first name.
    :param last_name: string - user's last name.
    :param email: string - user's email.
    :param username: string - user's username.
    :return: False - data is valid.
             {any string} - user can't be created.
    """
    if first_name.isspace() or first_name == "" or len(first_name) > 64:
        return "First name cannot be empty or too large."
    if last_name.isspace() or last_name == "" or len(last_name) > 64:
        return "First name cannot be empty or too large."
    if "@" not in email:
        return "Email cannot be empty and must be valid."
    if User.objects.filter(email=email).exists():
        return "Email is already in use."
    if username.isspace() or username == "" or len(username) > 64 or not re.search("[a-z]", username.lower()):
        return "Username cannot be empty or too large."
    if User.objects.filter(username=username).exists():
        return "An account with this username already exists."
    return False


def validate_password(password, password_repeat=None):
    """
    Validate user password.
    :param password: password as string
    :param password_repeat: repeat password
    :return: False - valid password
    """
    if password_repeat:
        if password != password_repeat:
            return "Passwords did not match."
    flag = False
    if len(password) < 8:
        flag = True
    elif not re.search("[a-z]", password):
        flag = True
    elif not re.search("[A-Z]", password):
        flag = True
    elif not re.search("[0-9]", password):
        flag = True
    elif re.search("\s", password):
        flag = True
    if flag:
        return (
            "Password must contain at least a lower case, an upper case, a number, no spaces "
            "and be at least 9 characters."
        )
    return False
