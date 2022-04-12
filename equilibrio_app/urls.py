from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('loginuser',login,name="login"),
    path('signup',register,name="register"),
    path('subscribe',subscribe,name="subscribe"),
    path('workshop',workshop,name="workshop"),
    path('workshopregister/<int:id>',workshopregister,name="workshopregister"),
    path('',index,name="index"),
    path('faq',faq,name="faq"),
    path('teams',teams,name="teams"),
    path('logout',logoutuser,name="logoutuser"),
    path('gallery',gallery,name="gallery"),
    path('deskof',deskof,name="deskof"),
    path('sponsor',sponsor,name="sponsor"),
    path('teams',teams,name="teams"),
    path('eventinfo/<int:id>', eventinfo, name="eventinfo"),
    path('eventcategory',events_cat,name="eventcategory"),
    path('events/<int:id>',events,name="events"),
    path('registerevent/<int:id>', registerevent,name="registerevent"),
    path('profile/<int:id>',profile,name="profile"),
    path('editprofile/<int:id>',editprofile,name="editprofile"),
]