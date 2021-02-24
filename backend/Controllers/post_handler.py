from django.http import JsonResponse

from SoftwareDev import settings
from backend.Utils.community_validation import (
    check_if_valid,
)
from backend.Utils.paginators import json_paginator
from backend.Utils.points_handler import adjust_points
from backend.Utils.post_validation import check_valid_post
from backend.models import (
    Post,
    Community,
    PostLike,
    PostComment,
    PostCommentLike,
    CommunityMember,
)


def create_post(request, community_id):
    """
    Create a post.
    :param request: session request.
    :param community_id: id of the community.
    :return: 201 - Post has been created.
             400 - Bad request.
             401 - Unauthorized.
             403 - Not member of the community
             404 - Not Found - Community not found.
    """
    if (
        "title" in request.DATA
        and "description" in request.DATA
        and "post_type" in request.DATA
    ):
        try:
            user_instance, comm_instance, comm_member = check_if_valid(
                request, community_id
            )
        except ValueError:
            return check_if_valid(request, community_id)
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


def show_posts(request, community_id):
    """
    Show posts.
    :param request: session request.
    :param community_id: id of the community.
    :return: 200 - Posts has been returned.
             400 - Bad request.
             401 - Unauthorized.
             403 - Not member of the community
             404 - Not Found - Community not found.
    """
    try:  # Check if valid request
        user_instance, comm_instance, comm_member = check_if_valid(
            request, community_id
        )
    except ValueError:
        return check_if_valid(request, community_id)
    # Return pagination data
    store = Post.objects.filter(community=comm_instance).order_by("-created_at")
    return JsonResponse(
        json_paginator(request, store, lambda d: d.serialize(request)),
        status=200,
        safe=False,
    )


def show_post(request, community_id, post_id):
    """
    Show a particular post with paginated comments
    :param request: session request.
    :param community_id: id of the community.
    :param post_id: id of the post.
    :return: 200 - Post has been returned.
             400 - Bad request.
             401 - Unauthorized.
             403 - Not member of the community
             404 - Not Found - Post not found.
    """
    try:  # Check if valid request
        user_instance, comm_instance, _ = check_if_valid(request, community_id)
    except ValueError:
        return check_if_valid(request, community_id)
    # Return pagination data
    post_instance = check_valid_post(comm_instance, post_id)
    if post_instance is None:
        return JsonResponse("Post does not exist", status=404, safe=False)
    final_instance = {"post": post_instance.serialize()}
    post_comments = PostComment.objects.filter(post=post_instance).order_by(
        "-is_approved", "-created_at"
    )
    final_instance["comments"] = json_paginator(
        request, post_comments, lambda d: d.serialize()
    )
    return JsonResponse(
        final_instance,
        status=200,
        safe=False,
    )


def like_post(request, community_id, post_id):
    """
    Like a post.
    :param request: session request.
    :param community_id: id of community.
    :param post_id: id of post.
    :return: 200 - post liked.
             401 - permission denied.
             404 - post not found.
             409 - conflict.
    """

    # Check if community and post exists.
    try:
        community = Community.objects.get(id=community_id)
        post = Post.objects.get(id=post_id, community=community)
    except:
        return JsonResponse("Not Found - Post does not exist.", status=404, safe=False)

    user = request.user
    if CommunityMember.objects.filter(user=user, community=community).exists():
        if not PostLike.objects.filter(user=user, post=post).exists():

            # Create like and add points to the post creator.
            PostLike.objects.create(user=user, post=post)
            adjust_points(
                user=post.user,
                points=settings.LIKE_POST_PTS,
                community=community,
                post=post,
            )
            return JsonResponse("OK - Post liked.", status=200, safe=False)

        return JsonResponse("Conflict - Post is already liked.", status=409, safe=False)
    return JsonResponse(
        "Unauthorized - User is not part of community.", status=401, safe=False
    )


def unlike_post(request, community_id, post_id):
    """
    Unlike a post.
    :param request: session request.
    :param community_id: id of community.
    :param post_id: id of post.
    :return: 200 - post unliked.
             401 - permission denied.
             404 - post not found.
    """

    # Check if community and post exists.
    try:
        community = Community.objects.get(id=community_id)
        post = Post.objects.get(id=post_id, community=community)
    except:
        return JsonResponse("Not Found - Post does not exist.", status=404, safe=False)

    # Try to find like and delete it and subtract points from the post creator.
    user = request.user
    try:
        PostLike.objects.get(user=user, post=post).delete()
        adjust_points(
            user=post.user,
            points=-settings.LIKE_POST_PTS,
            community=community,
            post=post,
        )
        return JsonResponse("OK - Post unliked.", status=200, safe=False)
    except:
        return JsonResponse("Not Found - Like does not exist.", status=404, safe=False)
