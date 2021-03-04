from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import JsonResponse

from backend.Utils.paginators import json_paginator
from backend.Utils.points_handler import get_graphs
from backend.Utils.user_validation import (
    validate_user_data,
    validate_password,
    generate_share_code,
    verify_user_login,
)
from backend.models import User, Post


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
            request,
            username=request.DATA["email"],
            password=request.DATA["password"],
        )
        if user is not None:
            login(request, user)
            return JsonResponse("OK - User logged in.", status=200, safe=False)
        return JsonResponse(
            "Not Found - User not found.", status=404, safe=False
        )
    return JsonResponse(
        "Bad Request - Please provide the required json body.",
        status=400,
        safe=False,
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
        new_user = User.objects.create_user(
            email=request.DATA["email"],
            password=request.DATA["password"],
            username=request.DATA["username"],
            first_name=request.DATA["first_name"],
            last_name=request.DATA["last_name"],
            teacher_request=request.DATA["is_teacher"].lower() == "true",
        )

        if "description" in request.DATA:
            new_user.description = request.DATA["description"]

        return JsonResponse("Created - User created.", status=201, safe=False)

    return JsonResponse(
        "Bad Request - Please provide the required json body.",
        status=400,
        safe=False,
    )


def get_feed(request):
    """
    Get the logged in user feed. The feed includes all the posts in the communities the
    user is part of ordered chronologically.
    :param request: session request.
    :return: 200 - list of paginated Posts.
             401 - login required.
    """
    user = request.user

    # Get feed data and paginate it.
    feed = Post.objects.filter(community__communitymember__user=user).order_by(
        "-created_at"
    )

    # Check for filter phrase.
    phrase = request.GET.get("phrase")
    if phrase is not None:
        if phrase != "" and not phrase.isspace():
            for term in phrase.split():
                feed = feed.filter(Q(title__icontains=term))
        else:
            feed = feed.none()

    return JsonResponse(
        json_paginator(request, feed, lambda d: d.serialize(request)),
        status=200,
    )


def update_me(request):
    """
    Update users given correct fields.
    :param request: session request.
    :return: 200 - user updated.
             400 - bad request.
             401 - login required.
    """
    user = request.user
    password_updated = False
    if "password" in request.DATA and "password_repeat" in request.DATA:
        update_password = validate_password(
            request.DATA["password"], request.DATA["password_repeat"]
        )
        if update_password:
            return JsonResponse(
                "Bad Request - " + update_password, status=400, safe=False
            )

        # Update password.
        user.set_password(request.DATA["password"])
        user.save()
        password_updated = True

    elif (
        "email" in request.DATA
        and "first_name" in request.DATA
        and "last_name" in request.DATA
        and "email" in request.DATA
        and "hide_leaderboard" in request.DATA
        and "username" in request.DATA
        and "description" in request.DATA
    ):
        update_valid = validate_user_data(
            request.DATA["first_name"],
            request.DATA["last_name"],
            request.DATA["email"],
            request.DATA["username"],
        )
        if update_valid:
            return JsonResponse(
                "Bad Request - " + update_valid, status=400, safe=False
            )

        # Update user.
        user.first_name = request.DATA["first_name"]
        user.last_name = request.DATA["last_name"]
        user.email = request.DATA["email"]
        user.username = request.DATA["username"]
        user.hide_leaderboard = request.DATA["hide_leaderboard"]
        user.description = request.DATA["description"]
        user.save()

    if not password_updated:
        return JsonResponse("Bad Request - Bad fields.", status=400, safe=False)
    return JsonResponse("OK - User updated.", status=200, safe=False)


def get_user(request, user_id):
    """
    Endpoint for profile given a user id.
    :param request: session request.
    :param user_id: id of user.
    :return: 200 - user profile.
             401 - login required.
             404 - user not found.
    """

    try:
        get_user = User.objects.get(id=user_id)
    except:
        return JsonResponse(
            "Not Found - User does not exist.", status=404, safe=False
        )

    # Check for share code.
    valid_sc = False
    if get_user.share_code:
        if request.GET.get("sharecode") == get_user.share_code:
            valid_sc = True

    if not valid_sc:
        try:
            verify_user_login(request)
        except PermissionDenied:
            return JsonResponse(
                "Unauthorized - Login required.", status=401, safe=False
            )

    response = get_user.serialize()
    response["graphs"] = get_graphs(get_user)
    return JsonResponse(response, status=200)


def lb_serializer(data):
    user = data["user"]
    rank = data["rank"]
    return user.serialize_leaderboard(rank)


def get_leaderboard(request):
    """
    Get the leaderboard; a (paginated) list of all users ordered by ranking
    :param request: session request.
    :return: 200 OK
             401 Unauthorized
    """

    includedUsers = User.objects.filter(hide_leaderboard=False, is_staff=False)

    # ordered list of points, index denoting leaderboard position (rank)
    # distinct values means that everyone with the same points has the same rank
    rankings = []
    for item in includedUsers.values("points").distinct().order_by("-points"):
        rankings.append(item["points"])

    includedUsers = includedUsers.order_by("-points")

    paginationData = []
    for user in includedUsers:
        # rank is the index of the users points +1 (converting from 0-indexing)
        data = {"user": user, "rank": rankings.index(user.points) + 1}
        paginationData.append(data)

    return JsonResponse(
        json_paginator(request, paginationData, lb_serializer),
        status=200,
    )


def get_share_code(request):
    """
    Get the logged in user code.
    :param request: session request.
    """
    user = request.user
    return JsonResponse({"code": user.share_code}, status=200)


def update_share_code(request):
    """
    Update the share code and return it.
    :param request: session request.
    """
    user = request.user
    user.share_code = generate_share_code(6)
    user.save()
    return JsonResponse({"code": user.share_code}, status=200)
