import random

from django.shortcuts import render
from django.http import JsonResponse
from .models import Sps


# Create your views here.
def index(request):
    # 没有考虑主键不连续
    # length = Sps.objects.all().count()
    # randomer = random.randint(1,length)
    # elem = Sps.objects.get(id=randomer)

    # 两次计算去随机,参考https://baijiahao.baidu.com/s?id=1585226879867105430&wfr=spider&for=pc
    length = Sps.objects.all().count()
    random_index = random.randint(0, length - 1)
    elem = Sps.objects.all()[random_index]
    return JsonResponse({
            "song": elem.song,
            "content": elem.content,
        })