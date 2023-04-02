from django.shortcuts import render, redirect
from .models import Course
from students.models import Student
from departments.models import Department
from faculties.models import Faculty
from levels.models import Level
import csv, io
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
def courses(request):
    courses = Course.objects.all()
    students= Student.objects.all()
    paginator = Paginator(courses, 13)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'courses':page_obj,
        'students':students,
    }
    return render(request, 'courses-page.html', context)

def createCourse(request):
    departments = Department.objects.all()
    faculties = Faculty.objects.all()
    levels = Level.objects.all()
    context = {
        'departments':departments,
        'faculties':faculties,
        'levels':levels,
    }
    return render(request, 'create-course.html', context)

def create(request):
    courseCode = request.POST.get('courseCode')
    courseTitle = request.POST.get('courseTitle')
    creditLoad = request.POST.get('creditLoad')
    departmentName = request.POST.get('department')
    department = Department.objects.get(departmentName=str(departmentName).replace('Department of ', ''))
    facultyName = request.POST.get('faculty')
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    levelName = request.POST.get('level')
    level = Level.objects.get(title=levelName)
    if courseCode != '':
        if courseTitle != '':
            newCourse = Course.objects.create(courseCode=courseCode, courseTitle=courseTitle, creditLoad=creditLoad, department=department, faculty=faculty, level=level)
            newCourse.save()
    return redirect('/courses')

def cancel(request):
    return redirect('/courses')

def deleteCourse(request, id):
    course = Course.objects.get(pk=id)
    context = {'course':course}
    return render(request, 'delete-course.html', context)

def delete(request, id):
    course = Course.objects.get(pk=id)
    course.delete()
    return redirect('/courses')

def cancelDelete(request):
    return redirect('/courses')

def details(request, id):
    course = Course.objects.get(pk=id)
    context = {
        'course':course,
    }
    return render(request, 'course-details.html', context)

def editCourse(request, id):
    course = Course.objects.get(pk=id)
    departments = Department.objects.all()
    faculties = Faculty.objects.all()
    levels = Level.objects.all()
    context = {
        'departments':departments,
        'faculties':faculties,
        'levels':levels,
        'course':course
    }
    return render(request, 'edit-course.html', context)

def edit(request, id):
    editCourse = Course.objects.get(pk=id)
    courseCode = request.POST.get('courseCode')
    courseTitle = request.POST.get('courseTitle')
    creditLoad = request.POST.get('creditLoad')
    departmentName = request.POST.get('department')
    department = Department.objects.get(departmentName=str(departmentName).replace('Department of ', ''))
    facultyName = request.POST.get('faculty')
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    levelName = request.POST.get('level')
    level = Level.objects.get(title=levelName)
    if courseCode != '':
        if courseTitle != '':
            editCourse.courseCode = courseCode
            editCourse.courseTitle = courseTitle
            editCourse.department = department
            editCourse.faculty = faculty
            editCourse.creditLoad = creditLoad
            editCourse.save()
           
    return redirect('/courses')


def batchCreate(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_files']
        data = []
        file_data = csv_file.read().decode('utf-8')
        f = io.StringIO(file_data)
        
        reader = csv.reader(f)
        for row in reader:
            try:
                department = Department.objects.get(departmentName=str(row[2]))
                faculty = Faculty.objects.get(facultyName=str(row[3]))
                level = Level.objects.get(title=row[4])
                data.append(Course(courseCode=row[0], courseTitle=row[1], department=department, faculty=faculty, level=level, creditLoad=row[5]))
            except:
                pass
        # data.pop(0) 
        Course.objects.bulk_create(data)
        return redirect('/courses')
    else:
        return render(request, 'create-course.html')
    
    
def courseListTemplate(request):
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Course-List-Template':'attachment; filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['courseCode', 'courseTitle', 'department', 'faculty', 'level', 'creditLoad'])
    return response
    
