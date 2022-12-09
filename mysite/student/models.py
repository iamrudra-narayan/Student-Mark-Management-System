from django.db import models

# Create your models here.

class student_detail(models.Model):
    name = models.CharField(max_length=50, default="name") 
    college = models.CharField(max_length=50, default="college") 
    examination = models.CharField(max_length=100, default="examination")
    rollno = models.CharField(max_length=10, unique=True, default="rollno")
    branch = models.CharField(max_length=100, default="branch")
    
    def __str__(self):
        return (self.name) 


class student_mark(models.Model):
    student = models.ForeignKey(student_detail, on_delete=models.CASCADE, default="")
    odia = models.CharField(max_length=3, default="") 
    eng = models.CharField(max_length=3, default="") 
    phy = models.CharField(max_length=3, default="")
    chem = models.CharField(max_length=3, default="")
    math = models.CharField(max_length=3, default="")
    it = models.CharField(max_length=3, default="")

    def __str__(self):
        return (self.student.name)
            
