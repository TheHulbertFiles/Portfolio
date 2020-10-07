from django.shortcuts import render,get_object_or_404, get_list_or_404

from Global.models import Skills, Social

def skills(request):

    tech = Skills.tech_skills()
    soft = Skills.soft_skills()
    other = Skills.other_skills()
    soc = Social.objects

    context = {'tech':tech, 'soft':soft, 'other':other, 'soc':soc}

    return render(request, 'skills/skills.html', context)

def skill_details(request, Skill_id):

    skill = Skills.objects
    skill_det = get_object_or_404(skill, pk=Skill_id)
    soc = Social.objects

    context = {'skill':skill_det, 'soc':soc}
    
    return render(request, 'skills/skill_details.html', context)