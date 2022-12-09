from django.contrib import admin
from student.models import student_detail, student_mark

# Register your models here.
admin.site.register(student_detail)
admin.site.register(student_mark)
