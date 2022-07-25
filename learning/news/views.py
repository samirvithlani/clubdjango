from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import News

# Create your views here.

class CreateNewsView(CreateView):
    template_name = "news/create_news.html"
    success_url = "/news/"
    model = News
    fields = "__all__"
    
    