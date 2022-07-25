from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('createnews/',CreateNewsView.as_view(),name='createnews'),
]
