from django.db import models

# Create your models here.


class Faculty(models.Model):
    facultyId = models.AutoField(primary_key=True)
    facultyName = models.CharField(blank=False, max_length=100, unique=True)
    
    def __str__(self):
        return f'Faculty of {self.facultyName}'

    class Meta:
        verbose_name_plural = 'Faculties'











    # lecturers = 0
    # departments = 0
    # students = 0

