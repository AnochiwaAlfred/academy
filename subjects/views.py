from django.shortcuts import render, redirect
from .models import Subject
from lecturers.models import Lecturer
from courses.models import Course
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def subjects(request):
    subjects = Subject.objects.all()
    context = {
        'subjects':subjects,
    }
    print('Samuel')
    return render(request, 'subjects-page.html', context)

@login_required
def createSubject(request):
    courses = Course.objects.all()
    lecturers = Lecturer.objects.all()
    context = {
        'courses':courses,
        'lecturers':lecturers,
    }
    return render(request, 'create-subject.html', context)

@login_required
def create(request):
    courseName = request.POST.get('course')
    courseTitle = courseName[10:]
    course = Course.objects.get(courseTitle=courseTitle)
    lecturerIdList = request.POST.getlist('lecturer')
    newSubject = Subject.objects.create(course=course)
    newSubject.save()
    for i in lecturerIdList:
        lecturer = Lecturer.objects.get(id=i)
        print(type(lecturer))
        newSubject.lecturer.add(lecturer)
    return redirect('/courses')

@login_required
def cancel(request):
    return redirect('/subjects')

@login_required
def deleteSubject(request, id):
    subject = Subject.objects.get(pk=id)
    context = {'subject':subject}
    return render(request, 'delete-subject.html', context)

@login_required
def delete(request, id):
    subject = Subject.objects.get(pk=id)
    subject.delete()
    return redirect('/subjects')

@login_required
def cancelDelete(request):
    return redirect('/subjects')