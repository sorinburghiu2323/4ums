from django.core.paginator import Paginator, EmptyPage

from backend.models import Post


def post_paginator(posts: [Post], page: int):
    """
    Paginate a list of Post instances given a certain page to return.
    If `page` parameter if over the amount of pages, last page is returned.
    :param posts: list of Post instances to paginate.
    :param page: page number wanted to be returned.
    :return: dict as follows:
                {
                    "total_pages": x,
                    "current_page": y,
                    "posts": post_list (serialised),
                }
    """
    POSTS_PER_PAGE = 20  # Amount of posts that can fit in a page.
    paginator = Paginator(posts, POSTS_PER_PAGE)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    post_list = []
    for post in posts:
        post_list.append(post.serialize())
    return {
        "total_pages": paginator.num_pages,
        "current_page": page if page < paginator.num_pages else paginator.num_pages,
        "posts": post_list,
    }
