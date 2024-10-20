from django.contrib import admin
from .models import *

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_provider_name', 'Catagory')
    
admin.site.register(Catagory)
admin.site.register(Courses,CoursesAdmin)