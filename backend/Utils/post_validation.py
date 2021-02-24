from backend.models import Post


def check_valid_post(comm_instance, post_id):
    try:
        return Post.objects.get(id=post_id, community=comm_instance)
    except Post.DoesNotExist:
        return None
