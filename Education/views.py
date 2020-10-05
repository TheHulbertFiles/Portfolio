from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Education, Other, Courses
from Global.models import Social

# Variables
soc = Social.objects

# URL Requests
def education(request):

    edu = Education.objects
    individual = Other.objects
    context = {'edu':edu, 'soc':soc, 'individual':individual}

    return render(request, 'education/education.html', context)
    
def edu_details(request, Edu_id, Edu_degree):

    edu = Education.objects
    courses = Courses.coursesFilter(Edu_degree)
    edu_det = get_object_or_404(edu, pk=Edu_id)
    context = {'courses':courses, 'edu':edu_det, 'soc':soc}

    return render(request, 'education/edu_details.html', context)

def course_details(request, Edu_id, Course_id):

    edu = Education.objects
    course = Courses.objects
    edu_det = get_object_or_404(edu, pk=Edu_id)
    course_det = get_object_or_404(course, pk=Course_id)
    context = {'courses':course_det, 'edu':edu_det, 'soc':soc}
    
    return render(request, 'education/education_course_detail.html', context)