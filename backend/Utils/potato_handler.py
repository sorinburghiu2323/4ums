from backend.models import *
from django.http import JsonResponse


def get_potatoes(request):
    """
    Get method for potatoes.

    :param request: Session request
    :return: List of all potatoes
    """

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


def check_potato(potato_object):
    """
    Validate a potato dict object.
    Rules: - needs "name", "is_sweet", "quantity"
           - "name" must be unique in the database

    :param potato_object: Dict of potato to be created
    :return: False - Validation passed
             Any JsonResponse - Validation failed
    """
    if "name" in potato_object and "is_sweet" in potato_object and "quantity" in potato_object:
        if not Potato.objects.filter(name=potato_object["name"]).exists():
            return False
        else:
            return JsonResponse("Conflict - Name attribute must be unique.", status=409, safe=False)
    else:
        return JsonResponse("Bad Request - Fields for potato missing.", status=400, safe=False)


def post_potato(request):
    """
    Post a list of potatoes to be created.

    :param request: Session request
    :return: 201 - Created
             4xx - An error has occurred
    """

    if "potatoes" in request.DATA:
        if type(request.DATA["potatoes"]) is list:

            # Validate each potato object BEFORE creating it.
            for potato_object in request.DATA["potatoes"]:
                potato_status = check_potato(potato_object)
                if not potato_status:
                    continue  # If False, potato is validated, so check next potato.
                return potato_status

            # Once validation is successful, create the potatoes.
            for potato_object in request.DATA["potatoes"]:
                new_potato = Potato.objects.create(
                    name=potato_object["name"],
                    is_sweet=potato_object["is_sweet"],
                    quantity=potato_object["quantity"],
                )
            return JsonResponse("Created - Potatoes created.", status=201, safe=False)
    return JsonResponse("Bad Request - 'potatoes' list missing", status=400, safe=False)
