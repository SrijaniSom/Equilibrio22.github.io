from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Newsletter)
admin.site.register(Workshop)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(EventRegister)
admin.site.register(WorkshopRegister)