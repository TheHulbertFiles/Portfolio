from django.shortcuts import render

# URL Requests
def projects(request):
    return render(request, 'projects/projects.html')
