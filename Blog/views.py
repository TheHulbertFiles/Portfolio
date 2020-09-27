from django.shortcuts import render

# URL Requests
def blog(request):
    return render(request, 'blog/blog.html')
