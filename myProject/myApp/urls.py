from . import views
from django.urls import path

urlpatterns = [
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
    path("login",views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path("Courses",views.courses,name="Courses"),
    path('courses/<str:name>/', views.courses_view, name='courses'),
    path('courses/<str:cname>/<str:pname>', views.courses_details, name='courses_details'),

]
