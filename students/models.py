from django.db import models
from levels.models import Level
from departments.models import Department
from faculties.models import Faculty
from subjects.models import Subject


# Create your models here.

class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    TITLE = (
        ('Mr.', 'Mr.'),
        ('Miss.', 'Miss.'),
        ('Mrs.', 'Mrs.'),
        ('Dr.', 'Dr.'),
        ('Engr.', 'Engr.'),
        ('Barr.', 'Barr.'),
        ('Prof.', 'Prof.'),
    )
    id = models.AutoField(primary_key=True)
    regNumber = models.CharField(blank=False, unique=True, max_length=15)
    firstName = models.CharField(blank=False, max_length=50)
    lastName = models.CharField(blank=False, max_length=50)
    dateOfBirth = models.DateField(blank=False)
    title = models.CharField(max_length=5, choices=TITLE, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER, blank=False)
    phone = models.CharField(blank=False, max_length=15)
    address = models.TextField(blank=False)
    email = models.EmailField(max_length=100, unique=True)
    courses = models.ManyToManyField(Subject, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    yearOfEntry = models.DateField(blank=False)
    yearOfGraduation = models.DateField(blank=False)
    username = models.EmailField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media')
    
    
    def __str__(self):
        return f'{self.lastName} {self.firstName}'