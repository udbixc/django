import random

from django.shortcuts import render

#导包，还需要导入模版的包

from django.http import HttpResponse
# Create your views here.

#添加数据库的包
from App.models import Student

#定义路由（这个路由是使用HttpResponse这个包）
def hello(request):
    return HttpResponse("emmmmmmm")

def lala(request):
    return HttpResponse("lalalala")

def index(request):
    return render(request, 'index.html')

def add_student(request):
    student = Student()
    student.s_name = "zhengh%d" %(random.randrange(100))
    student.save()
    return HttpResponse('Add Student %s success' % student.s_name)

def get_students(request):
    #student = Student()
    students = Student.objects.all()
    for student in students:
        print(student.s_name)
    #return HttpResponse("Student List")

    context = {
        "students": students
    }
    return render(request, 'student_list.html', context=context)

def update_student(request):
    #pk是指主键值
    student = Student.objects.get(pk=2)
    student.s_name = 'udbixc'
    student.save()

    return HttpResponse("Student update success")

def delete_student(request):
    student = Student.objects.get(pk=5)
    student.delete()
    return HttpResponse("Student Delete Success")


