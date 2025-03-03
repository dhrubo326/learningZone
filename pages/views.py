from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "pages/home.html", {
       "bannerImage": "home-bg.jpg"
    }) 

def about_us(request):
    return render(request, "pages/about.html", {
       "headImage": "about-bg.jpg"
    }) 

def contact(request):
    return render(request, "pages/contact.html", {
       "headImage": "contact-bg.jpg"
    })

def instructors(request):
   return render(request, "pages/instructors.html", {
       "bannerImage": "home-bg.jpg"
    })
def becomeATeacher(request):
   return render(request, "pages/become_a_teacher.html", {
       "bannerImage": "home-bg.jpg"
    })
