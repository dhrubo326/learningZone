from django.urls import path
from . import views

app_name = "courses"
urlpatterns = [
    path("", views.all_courses, name="course_page"),
    path("details", views.single_course, name="single_course"),
    path("events", views.events, name="events_page"),
    path("eventDetails", views.eventDetails, name="event_details_page"),
    path("lessonVideo", views.lessonVideo, name="lesson_video_page"),
    path("lessonText", views.lessonText, name="lesson_text_page"),
    path("lessonQuiz", views.lessonQuiz, name="lesson_quiz_page"),
    path("lessonQuizResult", views.lessonQuizResult, name="lesson_quiz_result_page"),
    path("lessonAssignments", views.lessonAssignments, name="lesson_assignment_page"),
    path("lessonAssignmentsSubmit", views.lessonAssignmentsSubmit, name="lesson_assignment_submit_page"),
]