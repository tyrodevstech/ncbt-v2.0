from django.urls import path
from . import views

app_name = "app_main"

urlpatterns = [
    path("", views.index_view, name="home"),
    path("aboutus/", views.about_us_view, name="aboutus"),
    path("admission/", views.admission_view, name="admission"),
    path("teachers/", views.teachers_view, name="teachers"),
    path("founder/", views.founder_view, name="founder"),
    path("course-details/<str:slug>", views.course_details_view, name="course_details"),
    path("notices/", views.notices_view, name="notices"),
    path("notice-details/<int:pk>", views.notice_details_view, name="notice_details"),
    path("contactus/", views.contact_us_view, name="contactus"),
]
