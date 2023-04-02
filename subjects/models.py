
from django.db import models
from lecturers.models import Lecturer
from courses.models import Course

# Create your models here.

    
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ManyToManyField(Lecturer)
    
    
    def __str__(self):
        return f'{self.course}'
    
    class Meta:
        verbose_name_plural = 'Subjects'