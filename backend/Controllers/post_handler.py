from django.http import JsonResponse

from SoftwareDev import settings
from backend.Utils.community_validation import (
    check_if_valid,
)
from backend.Utils.paginators import json_paginator
from backend.models import (
    Post,
    Community,
    PostLike,
    PointsGained,
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


def show_post(request, community_id):
    """
    Create a post.
    :param request: session request.
    :param community_id: id of the community.
    :return: 200 - Post has been created.
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
        post = Post.objects.get(id=post_id)
    except:
        return JsonResponse("Not Found - Post does not exist.", status=404, safe=False)

    user = request.user
    if CommunityMember.objects.filter(user=user, community=community).exists():
        if not PostLike.objects.filter(user=user, post=post).exists():

            # Create like and add points to the post creator.
            PostLike.objects.create(user=user, post=post)
            PointsGained.objects.create(
                user=post.user,
                community=community,
                post=post,
                points=settings.LIKE_POST_PTS,
            )
            post.user.points += settings.LIKE_POST_PTS
            post.user.save()
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
        post = Post.objects.get(id=post_id)
    except:
        return JsonResponse("Not Found - Post does not exist.", status=404, safe=False)

    # Try to find like and delete it and subtract points from the post creator.
    user = request.user
    try:
        PostLike.objects.get(user=user, post=post).delete()
        PointsGained.objects.create(
            user=post.user,
            community=community,
            post=post,
            points=-settings.LIKE_POST_PTS,
        )
        post.user.points -= settings.LIKE_POST_PTS
        post.user.save()
        return JsonResponse("OK - Post unliked.", status=200, safe=False)
    except:
        return JsonResponse("Not Found - Like does not exist.", status=404, safe=False)


def like_comment(request, community_id, post_id, comment_id):
    """
    Like a comment.
    :param request: session request.
    :param community_id: id of community.
    :param post_id: id of post.
    :param comment_id: id of comment.
    :return: 200 - comment liked.
             401 - permission denied.
             404 - comment not found.
             409 - conflict.
    """

    # Check if community, post and comment exists.
    try:
        community = Community.objects.get(id=community_id)
        post = Post.objects.get(id=post_id)
        comment = PostComment.objects.get(id=comment_id)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )

    user = request.user
    if CommunityMember.objects.filter(user=user, community=community).exists():
        if not PostCommentLike.objects.filter(user=user, post_comment=comment).exists():

            # Create like and add points to the comment creator.
            PostCommentLike.objects.create(user=user, post_comment=comment)
            PointsGained.objects.create(
                user=comment.user,
                community=community,
                post=post,
                comment=comment,
                points=settings.LIKE_COMMENT_PTS,
            )
            comment.user.points += settings.LIKE_COMMENT_PTS
            comment.user.save()
            return JsonResponse("OK - Comment liked.", status=200, safe=False)

        return JsonResponse(
            "Conflict - Comment is already liked.", status=409, safe=False
        )
    return JsonResponse(
        "Unauthorized - User is not part of community.", status=401, safe=False
    )


def unlike_comment(request, community_id, post_id, comment_id):
    """
    Unlike a comment.
    :param request: session request.
    :param community_id: id of community.
    :param post_id: id of post.
    :param comment_id: id of comment.
    :return: 200 - comment liked.
             401 - permission denied.
             404 - comment not found.
    """

    # Check if community, post and comment exists.
    try:
        community = Community.objects.get(id=community_id)
        post = Post.objects.get(id=post_id)
        comment = PostComment.objects.get(id=comment_id)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )

    # Try to find like and delete it and subtract points from the post creator.
    user = request.user
    try:
        PostCommentLike.objects.get(user=user, post_comment=comment).delete()
        PointsGained.objects.create(
            user=comment.user,
            community=community,
            post=post,
            comment=comment,
            points=-settings.LIKE_COMMENT_PTS,
        )
        comment.user.points -= settings.LIKE_COMMENT_PTS
        comment.user.save()
        return JsonResponse("OK - Comment unliked.", status=200, safe=False)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )
