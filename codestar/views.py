from django.shortcuts import get_object_or_404, redirect, render
from block.forms import CommentForm
from block.models import Post

def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post_details', slug=post.slug)
    else:
        form = CommentForm()
    
    return render(request, 'core/details.html', context={'post': post, 'form': form})
