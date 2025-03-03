from django.shortcuts import render

# Create your views here.

def all_courses(request):
    return render(request, "courses/allCourses.html", {
       "bannerImage": "home-bg.jpg"
    }) 

def single_course(request):
    return render(request, "courses/courseDetails.html", {
       "headImage": "about-bg.jpg"
    })

def events(request):
   return render(request, "courses/events.html")

def eventDetails(request):
   return render(request, "courses/eventDetails.html")

def lessonVideo(request):
   return render(request, "courses/lesson_video.html")

def lessonText(request):
   return render(request, "courses/lesson_text.html")

def lessonQuiz(request):
   return render(request, "courses/lesson_quiz.html")

def lessonQuizResult(request):
   return render(request, "courses/lesson_quiz_result.html")

def lessonAssignments(request):
   return render(request, "courses/lesson_assignments.html")

def lessonAssignmentsSubmit(request):
   return render(request, "courses/lesson_assignments_submit.html")

