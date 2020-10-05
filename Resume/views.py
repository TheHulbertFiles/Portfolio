from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Courses, Education, Experience, Other
from Global.models import Skills, Tags, Social

# Variables
soc = Social.objects

# URL Requests
def resume(request):
    exp = Experience.objects
    edu = Education.objects
    context = {'soc':soc, 'exp':exp, 'edu':edu}
    return render(request, 'resume/resume.html', context)

def experience(request):
    exp = Experience.objects
    context = {'exp':exp, 'soc':soc}
    return render(request, 'resume/experience/experience.html', context)

def exp_details(request, Exp_id):
    exp = Experience.objects
    exp_det = get_object_or_404(exp, pk=Exp_id)
    context = {'exp':exp_det, 'soc':soc}
    return render(request, 'resume/experience/exp_details.html', context)

def education(request):
    edu = Education.objects
    courses = Other.objects
    context = {'edu':edu, 'soc':soc, 'courses':courses}
    return render(request, 'resume/education/education.html', context)
    
def edu_details(request, Edu_id, Edu_degree):
    edu = Education.objects
    courses = Courses.coursesFilter(Edu_degree)
    edu_det = get_object_or_404(edu, pk=Edu_id)
    
    context = {'courses':courses, 'edu':edu_det, 'soc':soc}
    return render(request, 'resume/education/edu_details.html', context)

def course_details(request, Edu_id, Course_id):
    edu = Education.objects
    course = Courses.objects
    edu_det = get_object_or_404(edu, pk=Edu_id)
    course_det = get_object_or_404(course, pk=Course_id)
    context = {'courses':course_det, 'edu':edu_det, 'soc':soc}
    return render(request, 'resume/education/education_course_detail.html', context)

def skills(request):
    t_skills = Skills.skillFilter('Technical')
    s_skills = Skills.skillFilter('Soft')
    o_skills = Skills.skillFilter('Other')

    context = {'t_skills':t_skills, 's_skills':s_skills, 'o_skills':o_skills, 'soc':soc}
    return render(request, 'resume/skills/skills.html', context)

def skill_details(request, Skill_id):
    skill = Skills.objects
    skill_det = get_object_or_404(skill, pk=Skill_id)
    context = {'skill':skill_det, 'soc':soc}
    return render(request, 'resume/skills/skill_details.html', context)