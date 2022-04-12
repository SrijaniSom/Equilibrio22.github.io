from distutils.command.upload import upload
from email.policy import default
from operator import truediv
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    CHOICES = (
        ("Btech from GGV students","Btech GGV"),
        ("Non-Btech from GGV students","Non-Btech GGV"),
        ("Non-GGV students","Non-GGV"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100,default=None)
    phone = models.BigIntegerField(null=True)
    college_name = models.CharField(null=True,max_length=50)
    department = models.CharField(null=True,max_length=100)
    semester = models.IntegerField(default=1)
    part_of = models.CharField(max_length = 50,choices = CHOICES)

    def __str__(self):
        return (self.user.username,self.part_of)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'


class Category(models.Model):
    category_name = models.CharField(default="category name",max_length=100)
    category_caption = models.CharField(default="category caption",max_length=100)
    category_svg = models.TextField()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Workshop(models.Model):
    workshop_name = models.CharField(default="workshop name",max_length=100)
    category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE)
    workshop_desc = models.TextField(null=True)
    date = models.CharField(null=True, max_length=50)
    time = models.CharField(default="time",max_length=100,null=True)
    image = models.TextField(null=True)
    completed = models.BooleanField(null=True)

    def __str__(self):
        return self.workshop_name

    class Meta:
        verbose_name = 'Workshop'
        verbose_name_plural = 'Workshops'

class Event(models.Model):
    event_name = models.CharField(default="event name",max_length=100)
    image = models.TextField()
    category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE)
    event_desc = models.TextField(null=True)
    date = models.CharField(max_length=100,null=True)
    time = models.CharField(default="time of event",max_length=50,null=True)
    round1 = models.TextField(null=True)
    round2 = models.TextField(null=True)
    round3 = models.TextField(null=True)
    Theme = models.TextField(null=True)
    rules = models.TextField(null=True)
    judge = models.TextField(null=True)
    perks = models.TextField(null=True)
    completed = models.BooleanField(null=True)

    def __str__(self):
        return self.event_name

    def round_1(self):
        return filter(None, (line.strip() for line in self.round1.splitlines()))

    def round_2(self):
        return filter(None, (line.strip() for line in self.round2.splitlines()))

    def round_3(self):
        return filter(None, (line.strip() for line in self.round3.splitlines()))

    def themes(self):
        return filter(None, (line.strip() for line in self.Theme.splitlines()))

    def rul(self):
        return filter(None, (line.strip() for line in self.rules.splitlines()))
    
    def jud(self):
        return filter(None, (line.strip() for line in self.judge.splitlines()))
    
    def perk(self):
        return filter(None, (line.strip() for line in self.perks.splitlines()))

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class EventRegister(models.Model):
    name = models.CharField(null=True,max_length=500)
    email = models.EmailField(null=True)
    phone = models.BigIntegerField(null=True)
    college_name = models.CharField(null=True,max_length=500)
    department = models.CharField(null=True,max_length=500)
    semester = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(self):
        return (self.name,self.event.event_name)

    class Meta:
        verbose_name = 'EventRegistration'


class WorkshopRegister(models.Model):
    name = models.CharField(null=True,max_length=100,default="name")
    email = models.EmailField(null=True)
    phone = models.BigIntegerField(null=True)
    college_name = models.CharField(null=True,max_length=50,default="college_name")
    department = models.CharField(null=True,max_length=100,default="department")
    semester = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    workshop = models.ForeignKey(Workshop,on_delete=models.CASCADE)

    def __str__(self):
        return (self.name,self.workshop.workshop_name)

    class Meta:
        verbose_name = 'WorkshopRegistration'
