from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


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
        "Bad Request - Please provide the required body.", status=400, safe=False
    )


def user_logout(request):
    """
    Log out a user.
    :param request: session request.
    :return: 200 - user logged out.
    """
    logout(request)
    return JsonResponse("OK - User logged out.", status=200, safe=False)
