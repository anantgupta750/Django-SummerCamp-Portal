from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contactus,name="contact"),
    path('feedback',views.feedback,name="feedback"),
    path('registration',views.registration,name="registration"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('organizer_home',views.organizer_home,name="organizer_home"),
    path('program_details',views.program_details,name="program_details"),
    path('job_description',views.job_description,name="job_description"),
    path('organizer_editprofile',views.organizer_editprofile,name="organizer_editprofile"),
    path('viewevents',views.viewevents,name="viewevents"),
    path('viewprograms',views.viewprograms,name="viewprograms"),
    path('viewjobs',views.viewjobs,name="viewjobs"),

]
