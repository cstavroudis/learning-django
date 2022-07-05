from django.contrib import admin

# Register your models here.
from .models import Course
print(Course)
admin.site.register(Course)