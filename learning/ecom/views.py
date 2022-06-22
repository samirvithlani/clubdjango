
from dataclasses import field
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Product

# Create your views here.
class ProductList(ListView):
    model = Product
    products1 = model.objects.filter(price__gt=700)
    template_name ="product/list.html"
    context_object_name="products1"

class CreateProduct(CreateView):
    model = Product
    fields = ['name','description','price','qty']
    template_name ="product/create.html"
    success_url = "/product/list/"

class DeleteProduct(DeleteView):
    model = Product
    template_name ="product/delete.html"
    success_url = "/product/list/" 

def index(request):
    return render(request,"index.html")