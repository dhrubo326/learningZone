from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path("", views.index, name="home_page"),
    path("about", views.about_us, name="about_page"),
    path("contact", views.contact, name="contact_page"),
    path("instructors", views.instructors, name="instructors_page"),
    path("become-a-teacher", views.becomeATeacher, name="become_a_teacher_page"),
]