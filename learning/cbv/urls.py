

from django.urls import path
from .views import addCountry

urlpatterns = [
    
    path('addcountry/',addCountry.as_view(),name='addcountry'),
]