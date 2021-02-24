from django.http import JsonResponse

from SoftwareDev import settings

from backend.Utils.points_handler import adjust_points

from backend.models import (
    Community,
    CommunityMember,
    Post,
    PostComment,
    PostCommentLike,
)


def make_comment(request, community_id, post_id):
    """
    Add a comment.
    :param request: session request
    :param community_id: id of community that the post is in
    :param post_id: id of the post being commented on
    :return: 201 Created
             401 Unauthorized
             400 Bad request
             404 Not found
    """

    try:
        comm_instance = Community.objects.get(pk=community_id)
    except Community.DoesNotExist:
        return JsonResponse(
            f'Not found - No community with id "{community_id}" exists.',
            status=404,
            safe=False,
        )

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse(
            f'Not found - No post with id "{post_id}" exists (in community with id "{community_id}").',
            status=404,
            safe=False,
        )

    user = request.user

    if not CommunityMember.objects.filter(community=comm_instance, user=user).exists():
        return JsonResponse(
            "Unauthorized - User is not a member of that community.",
            status=401,
            safe=False,
        )

    if "comment" not in request.DATA:
        return JsonResponse(
            "Bad request - Must include comment string.", status=400, safe=False
        )

    new_comment = PostComment.objects.create(
        user=user, post=post, comment=request.DATA["comment"]
    )
    adjust_points(
        points=settings.MAKE_COMMENT_PTS,
        user=user,
        community=comm_instance,
        post=post,
        comment=new_comment,
    )

    return JsonResponse("Comment created", status=200, safe=False)


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
        post = Post.objects.get(id=post_id, community=community)
        comment = PostComment.objects.get(id=comment_id, post=post)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )

    user = request.user
    if CommunityMember.objects.filter(user=user, community=community).exists():
        if not PostCommentLike.objects.filter(user=user, post_comment=comment).exists():

            # Create like and add points to the comment creator.
            PostCommentLike.objects.create(user=user, post_comment=comment)
            adjust_points(
                user=comment.user,
                points=settings.LIKE_COMMENT_PTS,
                community=community,
                post=post,
                comment=comment,
            )
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
        post = Post.objects.get(id=post_id, community=community)
        comment = PostComment.objects.get(id=comment_id, post=post)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )

    # Try to find like and delete it and subtract points from the post creator.
    user = request.user
    try:
        PostCommentLike.objects.get(user=user, post_comment=comment).delete()
        adjust_points(
            user=comment.user,
            points=-settings.LIKE_COMMENT_PTS,
            community=community,
            post=post,
            comment=comment,
        )
        return JsonResponse("OK - Comment unliked.", status=200, safe=False)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )


def approve_comment(request, community_id, post_id, comment_id):
    """
    Approve a comment.
    :param request: session request.
    :param community_id: id of community.
    :param post_id: id of post.
    :param comment_id: id of comment.
    :return: 200 - comment approved.
             401 - permission denied.
             404 - comment not found.
             409 - conflict.
    """

    # Check if community, post and comment exists.
    try:
        community = Community.objects.get(id=community_id)
        post = Post.objects.get(id=post_id, community=community)
        comment = PostComment.objects.get(id=comment_id, post=post)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )

    user = request.user
    if (
        CommunityMember.objects.filter(user=user, community=community).exists()
        and Post.objects.filter(id=post_id, user=user, post_type="question").exists()
    ):
        if not PostComment.objects.filter(post=post, is_approved=True).exists():

            # Approve comment and add points to creator and post creator.
            comment.is_approved = True
            comment.save()
            adjust_points(
                user=user,
                points=settings.CHOOSE_CORRECT_ANSWER_PTS,
                community=community,
                post=post,
                comment=comment,
            )
            adjust_points(
                user=comment.user,
                points=settings.CORRECT_ANSWER_PTS,
                community=community,
                post=post,
                comment=comment,
            )
            return JsonResponse("OK - Comment approved.", status=200, safe=False)

        return JsonResponse(
            "Conflict - A comment has already been approved.", status=409, safe=False
        )
    return JsonResponse("Unauthorized - Permission denied.", status=401, safe=False)


def disapprove_comment(request, community_id, post_id, comment_id):
    """
    Disapprove a comment.
    :param request: session request.
    :param community_id: id of community.
    :param post_id: id of post.
    :param comment_id: id of comment.
    :return: 200 - comment disapproved.
             401 - permission denied.
             404 - comment not found.
    """

    # Check if community, post and comment exists.
    try:
        community = Community.objects.get(id=community_id)
        post = Post.objects.get(id=post_id, community=community)
        comment = PostComment.objects.get(id=comment_id, post=post)
    except:
        return JsonResponse(
            "Not Found - Comment does not exist.", status=404, safe=False
        )

    user = request.user
    if (
        CommunityMember.objects.filter(user=user, community=community).exists()
        and Post.objects.filter(id=post_id, user=user, post_type="question").exists()
    ):
        if PostComment.objects.filter(id=comment_id, is_approved=True).exists():

            # Approve comment and adjust points to creator and post creator.
            comment.is_approved = False
            comment.save()
            adjust_points(
                user=user,
                points=-settings.CHOOSE_CORRECT_ANSWER_PTS,
                community=community,
                post=post,
                comment=comment,
            )
            adjust_points(
                user=comment.user,
                points=-settings.CORRECT_ANSWER_PTS,
                community=community,
                post=post,
                comment=comment,
            )
            return JsonResponse("OK - Comment disapproved.", status=200, safe=False)

        return JsonResponse(
            "Conflict - This comment is not approved to be disapproved.",
            status=404,
            safe=False,
        )
    return JsonResponse("Unauthorized - Permission denied.", status=401, safe=False)
