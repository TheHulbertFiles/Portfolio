from django.shortcuts import render, get_object_or_404

from .models import Post
from Global.models import Social

# Variables
soc = Social.objects

# URL Requests
def blog(request):

    posts = Post.objects
    context = {'soc':soc, 'posts':posts}

    return render(request, 'blog/blog.html', context)

def post_detail(request, Post_id):

    post = get_object_or_404(Post, pk=Post_id)
    context = {'soc':soc, 'post':post}

    return render(request, 'blog/post.html', context)