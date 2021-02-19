from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.db.utils import IntegrityError

from backend.Utils.user_validation import verify_user_login
from backend.models import Community



def create_new(request):
    """
    Create a new community.
    :param request: session request
    :return: 201 Community created
             400 Bad request
             401 Unauthorized
             409 Conflict
    """
    try:
        user_instance = verify_user_login(request)
    except PermissionDenied:
        return JsonResponse("Unauthorized - Login required", status=401,
                            safe=False)

    if ("name" in request.DATA
    and "desc" in request.DATA):
        try:
            Community.objects.create(
                user=user_instance,
                name=request.DATA["name"],
                description=request.DATA["desc"]
            )
            return JsonResponse("Community created", status=201, safe=False)
        except IntegrityError:
            return JsonResponse("Conflict - Name is already in use", status=409,
                                safe=False)

    return JsonResponse("Bad request - Name and description are required",
                        status=400, safe=False)
