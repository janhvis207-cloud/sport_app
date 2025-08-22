from django.urls import path,include
from .import views,user_views
urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("about_academy/",views.about_academy,name="about_academy"),
    path("contact/",views.contact,name="contact"),
    path("feedback/",user_views.feedback,name="feedback"),
    path("user_login/",user_views.user_login,name="login"),
    path("registration/",user_views.registration,name="registeration"),
    path("cricket/",views.cricket,name="cricket"),
    path("basketball/",views.basketball,name="basketball"),
    path("badminton/",views.badminton,name="badminton"),
    path("football/",views.football,name="football"),
    path("home/",user_views.home,name="home"),
    path("user_logout/",user_views.user_logout,name="user_logout"),
    path("user_coach/",user_views.user_coach,name="user_coach"),
    path("view_programs/",views.view_programs,name="view_programs"),
    path("coach/",views.coach,name="coach"),
    path("admission/",user_views.admission,name="admission_form"),
    path("admission_status/",user_views.admission_status,name="admission_Status"),
    path("user_editprofile/",user_views.user_editprofile,name="edit_profile"),
    
]
