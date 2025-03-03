from django.shortcuts import render

# Create your views here.

def instructor(request):
    return render(request, "accounts/instructor.html", {
       "bannerImage": "home-bg.jpg"
    }) 

def student(request):
    return render(request, "accounts/student.html", {
       "headImage": "about-bg.jpg"
    }) 
