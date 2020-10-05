from django.shortcuts import render, get_object_or_404

from .models import Artifact
from Global.models import Social

# Variables
soc = Social.objects

# URL Requests
def artifacts(request):

    art = Artifact.objects
    context = {'soc':soc, 'art':art}

    return render(request, 'artifacts/artifacts.html', context)

def artifact_detail(request, Artifact_id):

    art = get_object_or_404(Artifact, pk=Artifact_id)
    context = {'soc':soc, 'art':art}
    
    return render(request, 'artifacts/artifact_detail.html', context)