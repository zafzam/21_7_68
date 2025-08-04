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

def contact(request):
    context = {}
    # context['count'] = list(range(1, 11))  # Example context variable
    context['message'] = "This is the for page."

    if request.method == 'POST' and request.POST.get('number') != '':
        number = int(request.POST.get('number'))
        print(request.POST['number'])
        context['count'] = list(range(1, number + 1))
    else:
        context['count'] = list(range(1, 2))

    return render(request, 'for.html', context)

# urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),  # 👈 ชื่อของ path นี้คือ 'home'
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
# ]
