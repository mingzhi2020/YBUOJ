from django.http import HttpResponse
from django.shortcuts import render


def index(request):
        #return render(request, '首页',locals())
        return HttpResponse(content="首页")