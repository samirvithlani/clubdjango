from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Country

# Create your views here.
#form -->

class addCountry(CreateView):
    model = Country
    template_name= "cbv/add_country.html"
    fields = ['name', 'code', 'capital']
    success_url = '/cbv/addcountry/'