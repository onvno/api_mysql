import random

from django.http import JsonResponse
from .models import Note

# Create your views here.
def index(request):
    length = Note.objects.all().count()
    print('length:', length)
    randomer = random.randint(1,length)
    elem = Note.objects.get(id=randomer)
    return JsonResponse({
            "title": elem.title,
            "body": elem.body,
        })