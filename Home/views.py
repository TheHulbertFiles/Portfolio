from django.shortcuts import render

from .models import Section
from Global.models import Social

# URL Requests
def home(request):

    sections = Section.objects
    soc = Social.objects
    context = {'sections':sections, 'soc':soc}
    
    return render(request, 'home/home.html', context)