from backend.models import *
from django.http import JsonResponse


def get_potatoes(request):

    # Get all potatoes and convert and serialize them.
    all_potatoes = Potato.objects.all()
    potato_list = []
    for potato in all_potatoes:
        potato_list.append(potato.serialize())

    # Create response variable.
    potatoes = {
        "potatoes": potato_list,
    }

    return JsonResponse(potatoes, status=200)


def post_potato(request):
    pass
