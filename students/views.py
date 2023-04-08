from django.shortcuts import render, redirect
from departments.models import Department
from faculties.models import Faculty
from levels.models import Level
from .models import Student
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import csv, io
from reportlab.pdfgen import canvas
from django.http import HttpResponse, FileResponse

# Create your views here.

@login_required
def studentsPage(request):
    students = Student.objects.all()
    paginator = Paginator(students, 13)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'students':page_obj
    }
    return render(request, 'students-page.html', context)

@login_required
def addStudent(request):
    level = Level.objects.all()
    faculty = Faculty.objects.all()
    department = Department.objects.all()
    context = {
        'level':level,
        'faculty':faculty,
        'department':department,
    }
    return render(request, 'add-student.html', context)

@login_required
def add(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    address = request.POST['address']
    phone = request.POST['phone']
    title = request.POST['title']
    regNumber = request.POST['regNumber']
    gender = request.POST['gender']
    yearOfEntry = request.POST['yearOfEntry']
    yearOfGraduation = request.POST['yearOfGraduation']
    departmentName = request.POST['department']
    facultyName = request.POST['faculty']
    department = Department.objects.get(departmentName=str(departmentName).replace('Department of ', ''))
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    levelName = request.POST.get('level')
    level = Level.objects.get(title=str(levelName))
    email = request.POST['email']
    dateOfBirth = request.POST['dateOfBirth']
    firstNameL = str(firstName).lower()
    lastNameL = str(lastName).lower()
    username = f'{firstNameL}{lastNameL}'
    newStudent = Student.objects.create(firstName=firstName, lastName=lastName, address=address, phone=phone, title=title, regNumber=regNumber, gender=gender, yearOfEntry=yearOfEntry, yearOfGraduation=yearOfGraduation, department=department, faculty=faculty, email=email, dateOfBirth=dateOfBirth, username=username, level=level)
    newStudent.save()
    return redirect('/students')

def cancel(request):
    return redirect('/students')

@login_required
def studentProfile(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student':student
    }
    return render(request, 'student-profile.html', context)

@login_required
def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student':student
    }
    return render(request, 'delete-student.html', context)

@login_required
def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/students')

def cancelDelete(request, id):
    return redirect('/students')

@login_required
def editStudent(request, id):
    student = Student.objects.get(pk=id)
    context = {
        'student':student
    }
    return render(request, 'edit-student.html', context)

@login_required
def edit(request, id):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    title = request.POST['title']
    phone = request.POST['phone']
    email = request.POST['email']
    address = request.POST['address']
    student = Student.objects.get(pk=id)
    student.firstName = firstName
    student.lastName = lastName
    student.title = title
    student.phone = phone
    student.email = email
    student.address = address
    student.save()
    return redirect('/students')
    
@login_required
def studentsListCsv(request):
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Students-List':'attachment; filename="somefilename.csv"'},
    )
    
    writer = csv.writer(response)
    writer.writerow(['regNumber', 'firstName', 'lastName', 'dateOfBirth', 'title', 'gender', 'phone', 'address', 'email', 'department', 'faculty', 'level', 'username'])
    students = Student.objects.all()
    for s in students:
        writer.writerow([s.regNumber, s.firstName, s.lastName, s.dateOfBirth, s.title, s.gender, s.phone, s.address, s.email, s.department, s.faculty, s.level, s.username])
    return response

@login_required
def studentsListPdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "We'll be adding this feature shortly")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

    
@login_required
def batchAdd(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_files']
        data = []
        file_data = csv_file.read().decode('utf-8')
        f = io.StringIO(file_data)
        
        reader = csv.reader(f)
        for row in reader:
            try:
                department = Department.objects.get(departmentName=str(row[9]))
                faculty = Faculty.objects.get(facultyName=str(row[10]))
                level = Level.objects.get(title=row[11])
                data.append(Student(
                        regNumber = row[0],
                        firstName = row[1],
                        lastName = row[2],
                        dateOfBirth = row[3],
                        title = row[4],
                        gender = row[5],
                        phone = row[6],
                        address = row[7],
                        email = row[8],
                        department = department,
                        faculty = faculty,
                        level = level,
                        yearOfEntry = row[12],
                        yearOfGraduation = row[13],
                        username = row[14]
                ))
            except:
                pass
            # data.pop(0)
        Student.objects.bulk_create(data)
        return redirect('/students')
    else:
        return render(request, 'add-student.html')

def studentListTemplate(request):
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Student-List-Template':'attachment; filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['regNumber', 'firstName', 'lastName', 'dateOfBirth', 'title', 'gender', 'phone', 'address', 'email', 'department', 'faculty', 'level', 'yearOfEntry', 'yearOfGraduation', 'username'])
    return response
    
