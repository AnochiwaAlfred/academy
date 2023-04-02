from django.shortcuts import render, redirect
from .models import Lecturer
from faculties.models import Faculty
from departments.models import Department
from subjects.models import Subject
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import csv, io
from django.http import HttpResponse

# Create your views here.

@login_required
def lecturer(request):
    lecturer = Lecturer.objects.all()
    paginator = Paginator(lecturer, 13)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'lecturer':page_obj,
    }
    return render(request, 'lecturer-page.html', context)

@login_required
def createLecturer(request):
    faculty = Faculty.objects.all
    department = Department.objects.all()

    context = {
        'faculty':faculty,
        'department':department,
    }
    return render(request, 'create-lecturer.html', context)

@login_required
def create(request):
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    idNumber = request.POST.get('idNumber')
    dateOfBirth = request.POST.get('dateOfBirth')
    title = request.POST.get('title')
    gender = request.POST.get('gender')
    rank = request.POST.get('rank')
    phone = str(request.POST.get('phone')).replace(' ', '')
    email = request.POST.get('email')
    address = request.POST.get('address')
    yearOfAppointment = request.POST.get('yearOfAppointment')
    departmentName = request.POST.get('department')
    facultyName = request.POST.get('faculty')
    department = Department.objects.get(departmentName=str(departmentName).replace('Department of ', ''))
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    firstNameLower = str(firstName).lower()
    lastNameLower = str(lastName).lower()
    username = f'{firstNameLower}{lastNameLower}'
    newLecturer = Lecturer.objects.create(firstName=firstName, lastName=lastName, idNumber=idNumber, dateOfBirth=dateOfBirth, title=title, gender=gender, rank=rank, phone=phone, email=email, address=address, department=department, faculty=faculty, yearOfAppointment=yearOfAppointment, username=username)
    newLecturer.save()
    return redirect('/lecturers')

def cancel(request):
    return redirect('/lecturers')

@login_required
def deleteLecturer(request, id):
    lecturer = Lecturer.objects.get(pk=id)
    context = {'lecturer':lecturer}
    return render(request, 'delete-lecturer.html', context)

@login_required
def delete(request, id):
    lecturer = Lecturer.objects.get(pk=id)
    lecturer.delete()
    return redirect('/lecturers')

def cancelDelete(request):
    return redirect('/lecturers')

@login_required
def profile(request, id):
    lecturer = Lecturer.objects.get(pk=id)
    subject = Subject.objects.filter(lecturer=lecturer)
    context = {
        'lecturer':lecturer,
        # 'subject':subject,
    }
    return render(request, 'lecturer-profile.html', context)

@login_required
def editLecturer(request, id):
    lecturer = Lecturer.objects.get(pk=id)
    faculty = Faculty.objects.all
    department = Department.objects.all()

    context = {
        'faculty':faculty,
        'department':department,
        'lecturer':lecturer,
    }
    return render(request, 'edit-lecturer.html', context)


@login_required
def edit(request, id):
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    title = request.POST.get('title')
    rank = request.POST.get('rank')
    phone = str(request.POST.get('phone')).replace(' ', '')
    email = request.POST.get('email')
    address = request.POST.get('address')
    firstNameLower = str(firstName).lower()
    lastNameLower = str(lastName).lower()
    username = f'{firstNameLower}{lastNameLower}@sharashellacademy.com'
    lecturer = Lecturer.objects.get(pk=id)

    lecturer.firstName=firstName
    lecturer.lastName=lastName
    lecturer.title=title
    lecturer.rank=rank
    lecturer.phone=phone
    lecturer.email=email
    lecturer.address=address
    lecturer.username=username

    lecturer.save()

    return redirect('/lecturers')

@login_required
def batchCreate(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_files']
        data = []
        file_data = csv_file.read().decode('utf-8')
        f = io.StringIO(file_data)
        
        reader = csv.reader(f)
        for row in reader:
            try:
                department = Department.objects.get(departmentName=str(row[10]))
                faculty = Faculty.objects.get(facultyName=str(row[11]))
                data.append(Lecturer(
                        idNumber = row[0],
                        firstName = row[1],
                        lastName = row[2],
                        dateOfBirth = row[3],
                        title = row[4],
                        gender = row[5],
                        rank = row[6],
                        phone = row[7],
                        email = row[8],
                        address = row[9],
                        department = department,
                        faculty = faculty,
                        yearOfAppointment = row[12],
                        username = row[13]
                ))
            except:
                pass
            # data.pop(0)
        Lecturer.objects.bulk_create(data)
        return redirect('/lecturers')
    else:
        return render(request, 'create-lecturer.html')

def lecturerListTemplate(request):
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Lecturer-List-Template':'attachment; filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['idNumber', 'firstName', 'lastName', 'dateOfBirth', 'title', 'gender', 'rank', 'phone', 'email', 'address', 'department', 'faculty', 'level', 'yearOfAppointment', 'username'])
    return response
    
