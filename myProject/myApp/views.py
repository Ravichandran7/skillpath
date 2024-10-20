from django.shortcuts import render, redirect
from myApp.form import CustomUserForm
from .models import  Courses, Catagory
from django.contrib import messages

def home(request):
    courses = Courses.objects.filter(trending=1)
    return render(request, "myApp/index.html",{"courses":courses})

def register(request):
    form=CustomUserForm()
    return render(request, "myApp/register.html",{'form':form})

def courses(request):
    categories = Catagory.objects.filter(status=0)
    return render(request, "myApp/Courses.html", {"categories": categories})

def courses_view(request, name):
    try:
        # Ensure you fetch a single category, since filter returns a queryset
        Catagory.objects.get(name=name, status=0)  # use get() for single category
        # Now filter courses by the related category using the correct field name
        courses = Courses.objects.filter(Catagory__name=name)
        return render(request, "myApp/products/index.html", {"courses": courses, "catagory__name": name})
    except Catagory.DoesNotExist:  # Handle the case where the category doesn't exist
        messages.warning(request, "NO SUCH COURSES FOUND")
        return redirect('courses')
    
def courses_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Courses.objects.filter(name=pname,status=0)):
            courses=Courses.objects.filter(name=pname,status=0).first()
            return render(request, "myApp/products/courses_details.html", {"courses": courses})
        else:
            messages.error(request, "NO SUCH COURSES FOUND")
            return redirect('courses')
    else:
        messages.error(request, "NO SUCH COURSES FOUND")
        return redirect('courses')