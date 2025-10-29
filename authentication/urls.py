from django.urls import path
from .views import register,signin,user_logout

urlpatterns = [
    path("regform/", register , name="regform"),
    path("login/", signin , name="signin"),
    path("logout/", user_logout , name="logout"),
   
]