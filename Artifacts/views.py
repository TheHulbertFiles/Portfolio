from django.shortcuts import render

# URL Requests
def artifacts(request):
    return render(request, 'artifacts/artifacts.html')