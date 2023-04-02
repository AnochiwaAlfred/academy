from django.db import models
from faculties.models import Faculty
from django.forms import ModelForm

# Create your models here.

class Department(models.Model):
    DURATION = (
        ('4', '4 Years'),
        ('5', '5 Years'),
        ('6', '6 Years')
    )
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(blank=False, max_length=100, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    courseDuration =  models.CharField(max_length=1, choices=DURATION, blank=False)
    
    def __str__(self):
        return f'Department of {self.departmentName}'

