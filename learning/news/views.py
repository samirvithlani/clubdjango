from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.conf import settings
from django.core.mail import send_mail

from .models import News

# Create your views here.

class CreateNewsView(CreateView):
    template_name = "news/create_news.html"
    success_url = "/news/"
    model = News
    fields = "__all__"
    
    subject = "Test"
    message = "Hello this mail from e-  Gift"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['samir.vithlani83955@gmail.com','harshilmodh77@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    
    