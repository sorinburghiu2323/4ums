from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse

from backend.Utils.community_validation import get_community, check_member
from backend.Utils.user_validation import verify_user_login
from backend.models import Post


def create_post(request, community_id):
    """
    Create a post.
    :param request: session request.
    :param community_id: id of the community.
    :return: 201 - Post has been created.
             400 - Bad request.
             401 - Unauthorized.
             404 - Not Found - Community not found.
    """
    if (
        "title" in request.DATA
        and "description" in request.DATA
        and "post_type" in request.DATA
    ):
        try:
            user_instance = verify_user_login(request)  # Verify that the user exists
        except PermissionDenied:
            return JsonResponse(
                "Unauthorized - Login required.", status=401, safe=False
            )
        comm_instance = get_community(community_id)
        if comm_instance is None:
            return JsonResponse("Community does not exist", status=404, safe=False)

        comm_member = check_member(community_id, user_instance)
        if comm_member is None:
            return JsonResponse(
                "User not member of that community", status=401, safe=False
            )
        Post.objects.create(
            user=user_instance,
            title=request.DATA["title"],
            description=request.DATA["description"],
            post_type=request.DATA["post_type"],
            community=comm_instance,
        )
        return JsonResponse("Ok - Post has been created.", status=201, safe=False)
    return JsonResponse(
        "Bad Request - Please provide the required body.", status=400, safe=False
    )


def show_post(request, community_id):
    """
    Create a post.
    :param request: session request.
    :param community_id: id of the community.
    :return: 201 - Post has been created.
             400 - Bad request.
             401 - Unauthorized.
             404 - Not Found - Community not found.
    """
    try:
        user_instance = verify_user_login(request)  # Verify that the user exists
    except PermissionDenied:
        return JsonResponse(
            "Unauthorized - Login required.", status=401, safe=False
        )
    comm_instance = get_community(community_id)
    if comm_instance is None:
        return JsonResponse("Community does not exist", status=404, safe=False)
    comm_member = check_member(community_id, user_instance)
    if comm_member is None:
        return JsonResponse(
            "User not member of that community", status=401, safe=False
        )
    print(comm_instance.id)
    store = Post.objects.filter(community=comm_instance)
    pages = Paginator(store, 25)
    page_number = request.GET.get('page')
    try:
        page_obj = pages.get_page(page_number)
    except PageNotAnInteger:
        page_obj = pages.page(1)
    except EmptyPage:
        page_obj = pages.page(pages.num_pages)
    serialized_data = serializers.serialize('json', page_obj)
    serialized_data = serialized_data.strip('"')
    page_data = {
        'previous_page': page_obj.has_previous() and page_obj.previous_page_number() or None,
        'next_page': page_obj.has_next() and page_obj.next_page_number() or None,
        'data': str(serialized_data)
    }
    return JsonResponse(page_data, status=200, safe=False)
