
from django.db import models
from departments.models import Department
from faculties.models import Faculty

# Create your models here.

class Lecturer(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    TITLE = (
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Miss.', 'Miss.'),
        ('Dr.', 'Dr.'),
        ('Engr.', 'Engr.'),
        ('Barr.', 'Barr.'),
        ('Prof.', 'Prof.'),
    )
    RANK = (
        ('Lecturer Assistant','Lecturer Assistant'),
        ('Assistant Lecturer','Assistant Lecturer'),
        ('Lecturer I','Lecturer I'),
        ('Lecturer II','Lecturer II'),
        ('Senior Lecturer','Senior Lecturer'),
        ('Associate Professor','Associate Professor'),
        ('Professor','Professor'),
    )
    id = models.AutoField(primary_key=True)
    idNumber = models.CharField(blank=False, unique=True, max_length=15)
    firstName = models.CharField(blank=False, max_length=200)
    lastName = models.CharField(blank=False, max_length=200)
    dateOfBirth = models.DateField(blank=False)
    title = models.CharField(max_length=5, choices=TITLE, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER, blank=False)
    rank = models.CharField(max_length=20, choices=RANK, blank=False)
    phone = models.CharField(blank=False, max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField(blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    yearOfAppointment = models.DateField(blank=False)
    username = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title} {self.lastName} {self.firstName}'