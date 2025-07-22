from django.shortcuts import render
# from django.http import HttpResponse
# from . import views



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),  # 👈 ชื่อของ path นี้คือ 'home'
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
# ]
