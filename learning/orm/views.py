from django.shortcuts import render

from .models import Student

# Create your views here.
def getStudentData(request):
    studentList = Student.objects.all().values()
    print(studentList)

    return render(request,"orm/studentList.html",{'studentList':studentList})

