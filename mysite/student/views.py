from django.shortcuts import render, redirect
from student.models import student_mark, student_detail
from django.contrib import messages

# Create your views here.

def show(request):

    if request.method == 'GET':

        rollno = request.GET.get('rollno')

        student = student_detail.objects.get(rollno = rollno)

        std_mark = student_mark.objects.filter(student = student)

        for mark in std_mark:
            sub = [int(mark.odia), int(mark.eng), int(mark.phy), int(mark.chem), int(mark.math), int(mark.it)]

        total = sum(sub)
        per = (total/600)*100

    else:
        return redirect('/')    
   
    return render(request, "show.html", {'std': student, 'std_mark': std_mark, 'total': total, 'per': per})