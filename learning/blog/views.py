from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print(request)
    #return HttpResponse("INDEX CALLED....")\
    return render(request,'index.html')

def food(request):
    return render(request,'foodblog.html')    