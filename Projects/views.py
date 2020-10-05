from django.shortcuts import render, get_object_or_404

from .models import Project
from Global.models import Social

# Variables
soc = Social.objects

# URL Requests
def projects(request):

    proj = Project.objects
    context = {'soc':soc, 'proj':proj}

    return render(request, 'projects/projects.html', context)

def project_detail(request, Project_id):

    proj = get_object_or_404(Project, pk=Project_id)
    context = {'soc':soc, 'proj':proj}

    return render(request, 'projects/project_detail.html', context)