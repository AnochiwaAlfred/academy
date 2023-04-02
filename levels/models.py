from django.db import models

# Create your models here.

class Level(models.Model):
    title = models.CharField(max_length=4, primary_key=True, blank=False)
    def __str__(self):
        return f'{self.title}'








    
    # students = 0