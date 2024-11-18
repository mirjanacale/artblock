from django.shortcuts import get_object_or_404, render

from block.models import Post

def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'template/details.html', {'post': post})
