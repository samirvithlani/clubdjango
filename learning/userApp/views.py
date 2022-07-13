from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.hashers import make_password

from .models import User

from .forms import UserForm

# Create your views here.
class UserRegisterView(FormView):
    
    form_class=UserForm
    model = User
    template_name = "userApp/register.html"
    success_url = "/userApp/login/"
    
    def form_valid(self, form):
        user = form.save()
        user.is_staff = True
        user.password = make_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)