from msilib.schema import RadioButton
from secrets import choice
from tkinter import Widget
from django import forms
from django.db import models
from django.forms import RadioSelect

# Create your models here.
hobbies = [
    ("reading", "Reading"),
    ("writing", "Writing"),
    ("playing", "Playing"),
    ("colleting", "Collecting"),
]
gender = (
    ("male","Male"),
    ("female","Female")
)
class Doctor1(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    exp = models.IntegerField()
    hobbies = models.CharField(choices=hobbies, max_length=100)
    gender = models.IntegerField(choices=gender,null=True)
    
    
    
    class Meta:
        db_table = "doctor1"
    