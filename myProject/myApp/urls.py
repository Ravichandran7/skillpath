from . import views
from django.urls import path

urlpatterns = [
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
    path("Courses",views.courses,name="Courses"),
    path('courses/<str:name>/', views.courses_view, name='courses'),

]
