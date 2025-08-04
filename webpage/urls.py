# from django.contrib import path
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('for/', views.contact, name='for_page'),
]