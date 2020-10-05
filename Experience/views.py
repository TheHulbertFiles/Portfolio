from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Experience
from Global.models import Social

# Variables
soc = Social.objects

# URL Requests
def experience(request):

    exp = Experience.objects
    context = {'exp':exp, 'soc':soc}

    return render(request, 'experience/experience.html', context)

def exp_details(request, Exp_id):

    exp = Experience.objects
    exp_det = get_object_or_404(exp, pk=Exp_id)
    context = {'exp':exp_det, 'soc':soc}

    return render(request, 'experience/exp_details.html', context)