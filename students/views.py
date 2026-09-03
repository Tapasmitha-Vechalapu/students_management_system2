from django.shortcuts import render


def home(request):
    course_names=["DBMS","OS","Web technologies","Computer Networks","SE"]
    return render(request, 'students/home.html', {'course_names': course_names})
# Create your views here.

def about(request):
    return render(request,'students/about.html')

def contact(request):
    return render(request,'students/contact.html')
