from django.core.paginator import Paginator, EmptyPage


def json_paginator(request, data_to_paginate: list) -> dict:
    """
    Paginate a list of Post instances given a certain page to return.
    If `page` parameter if over the amount of pages, last page is returned.

    How to use:
    1. Pass in the filtered data you want to use at 'data_to_paginate', this can be anything of type:
        data_to_paginate = Example.objects.filter(color=red)

    :param data_to_paginate: list of instances to paginate.
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
        data_to_paginate = paginator.page(int(request.DATA["page"]))
    except EmptyPage:
        data_to_paginate = paginator.page(paginator.num_pages)
    except:
        data_to_paginate = paginator.page(1)
    data = []
    for dp in data_to_paginate:
        data.append(dp.serialize(request))
    return {
        "total_pages": paginator.num_pages,
        "previous_page": data_to_paginate.has_previous()
        and data_to_paginate.previous_page_number()
        or None,
        "next_page": data_to_paginate.has_next()
        and data_to_paginate.next_page_number()
        or None,
        "data": data,
    }
