from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'students_informations'
        managed = True
        verbose_name = 'Student Data'
        verbose_name_plural = 'Student Data'
        ordering = ['name']
            
    