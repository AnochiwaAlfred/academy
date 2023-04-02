from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from students.models import Student
from lecturers.models import Lecturer
from departments.models import Department
from faculties.models import Faculty
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def search(request):
    query = request.GET.get('q')
    if query:
        # results = Faculty.objects.filter(Q(facultyName__icontains=query) | Q(description__icontains=query))
        results = Faculty.objects.filter(facultyName__contains=query)
    else:
        results = Faculty.objects.all()
    context = {
        'results':results
    }
    return render(request, 'dashboard/index.html', context)


@login_required()
def base(request):
    users = User.objects.all()
    firstName = request.user.first_name
    newUser = Student.objects.filter(firstName=firstName)
    
    context = {
        'users':users,
        'new-user':newUser
    }
    return render(request, 'dashboard/new-dash.html', context)

@login_required()
def index(request):
    studentsCount = Student.objects.count()
    lecturersCount = Lecturer.objects.count()
    facultiesCount = Faculty.objects.count()
    departmentsCount = Department.objects.count()
    studentsList = Student.objects.all()
    paginator = Paginator(studentsList, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    studentz =Student.objects.get(id=1)
    context = {
        'studentsCount':studentsCount,
        'lecturersCount':lecturersCount,
        'facultiesCount':facultiesCount,
        'departmentsCount':departmentsCount,
        'studentsList':page_obj,
        'studentz':studentz,
    }
    return render(request, 'dashboard/index.html', context)
    


        




