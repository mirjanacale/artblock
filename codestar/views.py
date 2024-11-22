from django.shortcuts import get_object_or_404, redirect, render
from block.forms import CommentForm
from block.models import Post, Category

def details(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE )
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

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    
    return render(request, 'core/category.html', context={'category': category,'posts':posts })

def search(request):
    query = request.GET.get('query','')
    
    posts = Post.objects.filter(title__icontains=query)
    
    return render(request, 'codestar/search.html', context={'posts': posts})
      
