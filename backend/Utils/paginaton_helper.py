import json

from django.core import serializers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def format_json(request, store):
    pages = Paginator(store, 25)
    page_number = request.GET.get("page")
    try:
        page_obj = pages.get_page(page_number)
    except PageNotAnInteger:
        page_obj = pages.page(1)
    except EmptyPage:
        page_obj = pages.page(pages.num_pages)
    serialized_data = json.loads(serializers.serialize("json", page_obj.object_list))
    page_data = {
        "previous_page": page_obj.has_previous()
        and page_obj.previous_page_number()
        or None,
        "next_page": page_obj.has_next() and page_obj.next_page_number() or None,
        "data": serialized_data,
    }
    return page_data
