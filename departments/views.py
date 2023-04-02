from django.shortcuts import render, redirect
from .models import Department
# from .forms import DepartmentForm
from faculties.models import Faculty
from students.models import Student
from django.http import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import csv, io
from reportlab.pdfgen import canvas

# Create your views here.
@login_required
def department(request):
    dept = Department.objects.all()
    paginator = Paginator(dept, 13)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'dept':page_obj,
    }
    return render(request, 'dept-page.html', context)

@login_required
def addDepartment(request):
    faculty = Faculty.objects.all()
    context = {
        'faculty':faculty,
    }
    return render(request, 'add-department.html', context)

@login_required
def add(request):
    departmentName = request.POST.get('newDepartment')
    facultyName = request.POST.get('faculty')
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    courseDurationText = request.POST.get('courseDuration')
    courseDuration = str(courseDurationText).replace(' Years', '')
    if departmentName != '':
        newDepartment = Department.objects.create(departmentName=departmentName, courseDuration=courseDuration, faculty=faculty)
        newDepartment.save()
    return redirect('/departments')

def cancel(request):
    return redirect('/departments')

@login_required
def delete(request, id):
    department = Department.objects.get(pk=id)
    department.delete()
    return redirect('/departments')

@login_required
def deleteDepartment(request, id):
    department = Department.objects.get(pk=id)
    context = {'department':department}
    return render(request, 'delete-department.html', context)

def cancelDelete(request):
    return redirect('/departments')

@login_required
def details(request, id):
    department = Department.objects.get(pk=id)
    student = Student.objects.filter(department=department)
    context = {
        'department':department,
        'student':student,
    }
    return render(request, 'department-details.html', context)

@login_required
def editDepartment(request, id):
    department = Department.objects.get(pk=id)
    faculty = Faculty.objects.all()
    context = {
        'department':department,
        'faculty':faculty,
    }
    return render(request, 'edit-department.html', context)

@login_required
def edit(request, id):
    departmentName = request.POST.get('newDepartment')
    facultyName = request.POST.get('faculty')
    faculty = Faculty.objects.get(facultyName=str(facultyName).replace('Faculty of ', ''))
    courseDurationText = request.POST.get('courseDuration')
    courseDuration = str(courseDurationText).replace(' Years', '')
    department = Department.objects.get(pk=id)
    if departmentName != '':
        department.departmentName = departmentName
        department.faculty = faculty
        department.courseDuration =courseDuration
        department.save()
    return redirect('/departments')

def departmentListCsv(request):
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Departments-List':'attachment; filename="somefilename.csv"'},
    )
    
    writer = csv.writer(response)
    writer.writerow(['departmentName', 'faculty', 'courseDuration'])
    department = Department.objects.all()
    for i in department:
        writer.writerow([i.departmentName, i.faculty, i.courseDuration])
    return response

def departmentListPdf(request):
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
                faculty = Faculty.objects.get(facultyName=str(row[1]))

                data.append(Department(
                    departmentName = row[0],
                    faculty = faculty,
                    courseDuration = row[2],
            ))
            except:
                pass
        Department.objects.bulk_create(data)
        return redirect('/departments')
    else:
        return render(request, 'add-department.html')
    
        
def departmentListTemplate(request):
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Department-List-Template':'attachment; filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['departmentName', 'faculty', 'courseDuration'])
    return response
    
