from unicodedata import category
from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import login as dj_login
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
import itertools
from django.db.models import Q
from functools import reduce
from operator import or_
import operator

# Create your views here.
def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if User.objects.filter(email=email).exists():
            return user
    return None

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email, password)
        if user is not None:
            dj_login(request,user)
            return redirect('index')
        else:
            messages.success(request,"email or password not correct!")
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        part_of = request.POST.get("part")
        try:
            if Student.objects.filter(email=email).exists() or User.objects.filter(email=email).exists():
                messages.error(request,"Email or Username already Exists!")
                return redirect('register')
            else:
                user = User.objects.create(username=username,email=email)
                user.save()
                customer = Student.objects.create(user=user,email=email,part_of=part_of,password=password)
                customer.save()
                dj_login(request, user)
                return redirect('index')
        except IntegrityError:
            messages.error(request,"Email or Username already Exists!")
            return redirect('register')
    else:
        return render(request, 'signup.html')
       
def logoutuser(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request,'index.html')

def profile(request,id):
    user = User.objects.get(id=id)
    stu = Student.objects.get(user=request.user)
    if request.user.is_authenticated:
        reg_events = EventRegister.objects.filter(name=request.user.username,email=stu.email)
        reg_work = WorkshopRegister.objects.filter(name=request.user.username,email=stu.email)
        return render(request,"profile.html",{'stu':stu,'reg_events':reg_events,'reg_work':reg_work})
    else:
        return render('login')

def editprofile(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(id=id)
        stu = Student.objects.get(user=request.user)
        if request.method == "POST":
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            
            college_name = request.POST.get('college_name')
            department = request.POST.get('department')
            semester = request.POST.get('semester')
            upload = request.POST.get('upload')
            password = request.POST.get('password')
            us = User.objects.filter(id=request.user.id).update(username=name,password=password)
            student = Student.objects.filter(user=user).update(phone=phone,email=email,college_name=college_name,department=department,semester=semester)
           
            return redirect('profile',user.id)
        return render(request,"edit.html",{'stu':stu})
    else:
        return render('login')

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        sub = Newsletter.objects.create(email=email)
        sub.save()
        messages.success(request,"Your Email has been Sent !")
        return redirect('index')

def workshop(request):
    workshops = Workshop.objects.all()
    return render(request,"workshop.html",{'workshops':workshops})

def faq(request):
    return render(request,"faq.html")

def teams(request):
    return render(request,"teams.html")

def gallery(request):
    return render(request,"gallery.html")

def deskof(request):
    return render(request,"deskof.html")

def sponsor(request):
    return render(request,"sponsor.html")

def teams(request):
    return render(request,"teams.html")

def events_cat(request):
    cat = Category.objects.all()
    return render(request,"event_cat.html",{'cat':cat})
        
def events(request,id):
    event = Event.objects.filter(category=id)
    return render(request,"event.html",{'event':event})

def eventinfo(request,id):
    event = Event.objects.get(id = id)
    return render(request, "event_info.html",{'event':event})

def workshopregister(request,id):
    event = Workshop.objects.get(id = id)
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            college_name = request.POST.get('college_name')
            department = request.POST.get('department')
            semester = request.POST.get('semester')
            reg = WorkshopRegister.objects.create(name=request.user.username,email=request.user.email,phone=phone,college_name=college_name,department=department,semester=semester,workshop=event)
            reg.save()
            return redirect('workshop')
        else:
            return render(request,"workshopregister.html",{'event':event})
    else:
        return redirect('login')

def registerevent(request,id):
    event = Event.objects.get(id = id)
    if request.user.is_authenticated:
        if request.method == "POST":
            phone = request.POST.get('phone')
            college_name = request.POST.get('college_name')
            department = request.POST.get('department')
            semester = request.POST.get('semester')
            reg = EventRegister.objects.create(name=request.user.username,email=request.user.email,phone=phone,college_name=college_name,department=department,semester=semester,event=event)
            reg.save()
            return redirect('eventcategory')
        else:
            return render(request,"eventregister.html",{'event':event})
    else:
        return redirect('login')

