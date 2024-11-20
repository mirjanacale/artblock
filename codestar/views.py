from django.shortcuts import get_object_or_404, render
from codestar.models import CommentForm

from block.models import Post

def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    form = CommentForm()
    return render(request, 'core/details.html', context={'post': post, 'form': form})
