from django.core.exceptions import PermissionDenied


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
