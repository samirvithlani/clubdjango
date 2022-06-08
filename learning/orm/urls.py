from django.contrib import admin
from django.urls import path,include
from orm import views

urlpatterns = [
    
    path('list/',views.getStudentData,name='list'),
    path('add/',views.addStudent,name='add'),
    path('update/',views.updateStudent,name='update'),
    path('delete/',views.deleteStudent,name='delete'),
    path('adddoctor/',views.addDocotr_paitnet,name='addDocotr_paitnet'),
    path('listdoctor/',views.getDoctor_paitentData,name='listdoctor'),
    
    
]
