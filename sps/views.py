import random

from django.shortcuts import render
from django.http import JsonResponse
from .models import Sps


# Create your views here.
def index(request):
    length = Sps.objects.all().count()
    randomer = random.randint(1,length)
    elem = Sps.objects.get(id=randomer)
    return JsonResponse({
            "song": elem.song,
            "content": elem.content,
        })