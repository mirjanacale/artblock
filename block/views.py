from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from .models import About

# Create your views here.
def my_block(request):
    return HttpResponse("<h1>MyBlock<h1>")

def frontpage(request):
    post = Post.objects.filter(status=Post.ACTIVE)

    return render(request, 'core/frontpage.html', {'posts': post})

def about(request): 
    about_instances = About.objects.all()
    
    return render(request, 'core/about.html', {'about': about})
