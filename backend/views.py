from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from backend.Utils.http_method_handler import handleMethods
from backend.Utils import potato_handler

# Create your views here.


@csrf_exempt
def potato_view(request):
    return handleMethods(
        request,
        GET=potato_handler.get_potatoes,
        PUT=potato_handler.post_potato,
    )
