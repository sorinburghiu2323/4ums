from backend.models import Post


def check_valid_post(comm_instance, post_id):
    try:
        Post.objects.get(id=post_id, community=comm_instance)
        return True
    except Post.DoesNotExist:
        return False
