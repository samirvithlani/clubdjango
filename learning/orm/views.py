from django.shortcuts import render
from django.db.models import *


from .models import Student

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



    return render(request,"orm/studentList.html",{'studentList':students})

