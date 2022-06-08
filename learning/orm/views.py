import email
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import *


from .models import Doctor, Paitent, Student

# Create your views here.
def getStudentData(request):
    studentList = Student.objects.all().values()
    students = Student.objects.filter(name__startswith='h')
    students1 = Student.objects.filter(email__endswith='.com').values()
    #students2 = Student.objects.filter
    students3 = Student.objects.filter(age__gte=20).values()
    student4 = Student.objects.filter(password__contains='@').values()
    students5 = Student.objects.filter(id__exact=1).values()
    students6 = Student.objects.filter(rollno__range=(8,10)).values()
    students7 = Student.objects.filter(rollno__range=(1,10)).count()

    students8 = Student.objects.all().aggregate(Sum('age'))
    students9 = Student.objects.all().aggregate(Avg('age'))
    students10 = Student.objects.all().aggregate(Max('age'))
    print(students8)
    print('max age',students10)
    

    print(students)
    print(students7)
    print(students9)
    return render(request,"orm/studentList.html",{'studentList':studentList})

def addStudent(request):
    s = Student(name="tejas",age = "35",email="tejas@gmail.com",isActive = "True",password = "tejas@1121",rollno = "6")
    s.name = "dhiraj"
    s.save()
    return render(request,"orm/studentList.html")

def updateStudent(request):
    s = Student.objects.get(id =4)
    s.name = "rama"
    s.save()
    return render(request,"orm/studentList.html")

def deleteStudent(request):
    s = Student.objects.filter(email__startswith="t").delete()
    return render(request,"orm/studentList.html")


def addDocotr_paitnet(request):
    #d = Doctor(name="tejas",age = "35",email="raj@doc.com",isActive = "True",password = "tejas@1121",rollno = "6")
    #d.save()
    d = Doctor.objects.get(id = 1)
    p = Paitent(doctor = d,name = "harshil",age = "35")
    p.save()

    return HttpResponse("<h1>Doctor and Paitent Added</h1>")

def getDoctor_paitentData(request):
    doctorList = Doctor.objects.all().values()
    paitentList = Paitent.objects.all().values()
    return render(request,"orm/doctorList.html",{'doctorList':doctorList,'paitentList':paitentList})    