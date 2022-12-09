from django.shortcuts import render, redirect
from student.models import student_mark, student_detail

# Create your views here.

def index(request):
    marks = []
    if request.method == 'GET':

        rollno = request.GET.get('rollno')

        student = student_detail.objects.get(rollno = rollno)

        std_mark = student_mark.objects.filter(student = student)   

    else:
        return redirect('/')    
   
    return render(request, "show.html", {'std': student, 'std_mark': std_mark})