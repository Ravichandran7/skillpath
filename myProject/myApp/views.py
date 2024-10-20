from django.shortcuts import render, redirect
from .models import Courses, Catagory
from django.contrib import messages

def home(request):
    return render(request, "myApp/index.html")

def register(request):
    return render(request, "myApp/register.html")

def courses(request):
    categories = Catagory.objects.filter(status=0)
    return render(request, "myApp/Courses.html", {"categories": categories})

def courses_view(request, name):
    try:
        # Ensure you fetch a single category, since filter returns a queryset
        category = Catagory.objects.get(name=name, status=0)  # use get() for single category
        # Now filter courses by the related category using the correct field name
        courses = Courses.objects.filter(Catagory__name=name)
        return render(request, "myApp/products/index.html", {"courses": courses, "catagory__name": name})
    except Catagory.DoesNotExist:  # Handle the case where the category doesn't exist
        messages.warning(request, "NO SUCH COURSES FOUND")
        return redirect('courses')
