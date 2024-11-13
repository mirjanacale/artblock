from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_block(request):
    return HttpResponse("<h1>MyBlock<h1>")


