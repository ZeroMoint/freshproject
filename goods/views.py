from django.shortcuts import render
from .models import GoodsInfo,TypeInfo

def index(request):
    return render(request, 'goods/index.html')

def detail(request):
    return render(request, 'goods/detail.html')

def list(request):
    return render(request, 'goods/list.html')


