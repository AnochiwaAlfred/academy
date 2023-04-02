from django.shortcuts import render, redirect
from departments.models import Department
from .models import Faculty
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
import io, csv

# Create your views here.

@login_required
def faculties(request):
    faculties = Faculty.objects.all()
    dept = Department.objects.all()
    context = {
        'faculties':faculties,
        'dept':dept,
    }
    return render(request, 'faculties-page.html', context)

@login_required
def details(request, id):
    faculty = Faculty.objects.get(pk=id)
    dept = Department.objects.filter(faculty=faculty)
    context = {
        'dept':dept,
        'faculty':faculty,
    }
    return render(request, 'faculty-details.html', context)

@login_required
def addFaculty(request):
    return render(request, 'add-faculty.html')

@login_required
def add(request):
    facultyName = request.POST.get('newFaculty')
    # facultyList = Faculty.objects.all()
    # facultyCheck = True
    if facultyName != '':
        # for f in facultyList:
        #     if f.facultyName==facultyName:
        #         facultyCheck&=False
        #         raise Http404("Faculty already exists")
        #     else:
        newFaculty = Faculty.objects.create(facultyName=facultyName)
        newFaculty.save()
    return redirect('/faculties')

def cancel(request):
    return redirect('/faculties')

@login_required
def delete(request, id):
    faculty = Faculty.objects.get(pk=id)
    faculty.delete()
    return redirect('/faculties')

@login_required
def deleteFaculty(request, id):
    faculty = Faculty.objects.get(pk=id)
    context = {'faculty':faculty}
    return render(request, 'delete-faculty.html', context)
    
def cancelDelete(request):
    return redirect('/faculties')

@login_required
def editFaculty(request, id):
    faculty = Faculty.objects.get(pk=id)
    context ={
        'faculty':faculty
    }
    return render(request, 'edit-faculty.html', context)

@login_required
def edit(request, id):
    faculty = Faculty.objects.get(pk=id)
    facultyName = request.POST.get('newFaculty')
    if facultyName != '':
        faculty.facultyName = facultyName
        faculty.save()
    return redirect('/faculties')


@login_required
def batchAdd(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_files']
        data = []
        file_data = csv_file.read().decode('utf-8')
        f = io.StringIO(file_data)
        
        reader = csv.reader(f)
        for row in reader:
            data.append(Faculty(
                    facultyName = row[0],
            ))
        data.pop(0)
        for i in data:
            print(i)
            Faculty.objects.bulk_create(data)
        return redirect('/faculties')
    else:
        return render(request, 'add-faculty.html')
    
    
def facultyListTemplate(request):
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Faculty-List-Template':'attachment; filename="somefilename.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['facultyName'])
    return response
    
