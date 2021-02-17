from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from backend.Utils.user_validation import validate_user_data, validate_password
from backend.models import User


def user_login(request):
    """
    Login a user using email and password.
    :param request: session request.
    :return: 200 - user has logged in.
             400 - bad request.
             404 - user not found.
    """
    if "email" in request.DATA and "password" in request.DATA:
        user = authenticate(
            request, username=request.DATA["email"], password=request.DATA["password"]
        )
        if user is not None:
            login(request, user)
            return JsonResponse("OK - User logged in.", status=200, safe=False)
        return JsonResponse("Not Found - User not found.", status=404, safe=False)
    return JsonResponse(
        "Bad Request - Please provide the required json body.", status=400, safe=False
    )


def user_logout(request):
    """
    Log out a user.
    :param request: session request.
    :return: 200 - user logged out.
    """
    logout(request)
    return JsonResponse("OK - User logged out.", status=200, safe=False)


def user_register(request):
    """
    Register new user endpoint. User data is validated before creation.
    :param request: session request.
    :return: 201 - user created.
             400 - bad request with description.
    """
    if (
        "email" in request.DATA
        and "username" in request.DATA
        and "password" in request.DATA
        and "first_name" in request.DATA
        and "last_name" in request.DATA
        and "is_teacher" in request.DATA
        and "password_repeat" in request.DATA
    ):

        # Validate user data.
        user_validation = validate_user_data(
            request.DATA["first_name"],
            request.DATA["last_name"],
            request.DATA["email"],
            request.DATA["username"],
        )
        if user_validation:
            return JsonResponse(
                "Bad Request - " + user_validation, status=400, safe=False
            )

        # Validate user password.
        password_validation = validate_password(
            request.DATA["password"], request.DATA["password_repeat"]
        )
        if password_validation:
            return JsonResponse(
                "Bad Request - " + password_validation, status=400, safe=False
            )

        # Create user.
        User.objects.create_user(
            email=request.DATA["email"],
            password=request.DATA["password"],
            username=request.DATA["username"],
            first_name=request.DATA["first_name"],
            last_name=request.DATA["last_name"],
            teacher_request=True
            if request.DATA["is_teacher"].lower() == "true"
            else False,
        )
        return JsonResponse("Created - User created.", status=201, safe=False)

    return JsonResponse(
        "Bad Request - Please provide the required json body.", status=400, safe=False
    )
