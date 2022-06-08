from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    isActive = models.BooleanField(default=True)
    password = models.CharField(max_length=20)
    rollno = models.IntegerField()

    class Meta:
        db_table = "student"


class Doctor(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    isActive = models.BooleanField(default=True)
    password = models.CharField(max_length=20)
    rollno = models.IntegerField()

    class Meta:
        db_table = "doctor"

class Paitent(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        db_table = "paitent"



    