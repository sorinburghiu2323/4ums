from django.core.paginator import Paginator, EmptyPage


def json_paginator(data_to_paginate: list, serialize: callable, request) -> dict:
    """
    Paginate a list of Post instances given a certain page to return.
    If `page` parameter if over the amount of pages, last page is returned.

    How to use:
    1. Pass in the filtered data you want to use at 'data_to_paginate', this can be anything of type:
        data_to_paginate = Example.objects.filter(color=red)
    2. Pass in the serialiser, e.g. "lambda d: d.serialise()"

    :param data_to_paginate: list of instances to paginate.
    :param serialize: function used to serialize each data item
    :param request: session request.
    :return: dict as follows:
                {
                    "total_pages": (int),
                    "previous_page": (int),
                    "next_page": (int),
                    "data": (serialised response),
                }
    """
    POSTS_PER_PAGE = 20  # Amount of posts that can fit in a page.
    paginator = Paginator(data_to_paginate, POSTS_PER_PAGE)
    try:
        posts = paginator.page(int(request.DATA["page"]))
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except:
        posts = paginator.page(1)
    data = []
    for dp in data_to_paginate:
        data.append(serialize(dp))
    return {
        "total_pages": paginator.num_pages,
        "previous_page": posts.has_previous() and posts.previous_page_number() or None,
        "next_page": posts.has_next() and posts.next_page_number() or None,
        "data": data,
    }
