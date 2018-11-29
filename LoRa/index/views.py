# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_views(request):
    # return HttpResponse('fuck')
    return render(request,'lorazhu.html')

def login_views(request):
    return HttpResponse('这是index应用中的login视图')

def love_views(request):
    return render(request,'sheji.html')