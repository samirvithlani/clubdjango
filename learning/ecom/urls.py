

from django.urls import path
from . import views

urlpatterns = [
    
    path('list/',views.ProductList.as_view(),name='product_list'),
    path('create',views.CreateProduct.as_view(),name='product_create'),
    path('delete/<int:pk>',views.DeleteProduct.as_view(),name ='product_delete'),
]