from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("instructor-dahboard", views.instructor, name="instructor_dashboard_page"),
    path("student-dahboard", views.student, name="student_dashboard_page"),
]