from django.db import models
from departments.models import Department
from faculties.models import Faculty
from levels.models import Level

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    courseCode = models.CharField(max_length=7, unique=True, blank=False)
    courseTitle = models.CharField(blank=False, max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    creditLoad = models.IntegerField()

    def __str__(self):
        return f'{self.courseCode} - {self.courseTitle}'    
    
    
    
    
    
    