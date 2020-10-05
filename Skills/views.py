from django.shortcuts import render,get_object_or_404, get_list_or_404

from Global.models import Skills, Social

def skills(request):

    t_skills = Skills.skillFilter('Technical')
    s_skills = Skills.skillFilter('Soft')
    o_skills = Skills.skillFilter('Other')
    soc = Social.objects

    context = {'t_skills':t_skills, 's_skills':s_skills, 'o_skills':o_skills, 'soc':soc}

    return render(request, 'skills/skills.html', context)

def skill_details(request, Skill_id):

    skill = Skills.objects
    skill_det = get_object_or_404(skill, pk=Skill_id)
    soc = Social.objects

    context = {'skill':skill_det, 'soc':soc}
    
    return render(request, 'skills/skill_details.html', context)