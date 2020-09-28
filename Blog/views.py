from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
def blog(request):
    posts = Post.objects
    return render(request, 'blog/blog.html', {'posts':posts})

def detail(request, Post_id):
    post = get_object_or_404(Post, pk=Post_id)
    return render(request, 'blog/detail.html', {'post':post})