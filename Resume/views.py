from django.shortcuts import render, get_object_or_404, get_list_or_404

from Global.models import Social

# Variables
soc = Social.objects

# URL Requests
def resume(request):
    context = {'soc':soc}
    return render(request, 'resume/resume.html', context)