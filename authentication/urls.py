from django.urls import path
from .views import register,signin,user_logout,create_profile,view_profile,edit_profile,delete_profile

urlpatterns = [
    path("regform/", register , name="regform"),
    path("signin/", signin , name="signin"),
    path("logout/", user_logout , name="logout"),
    path("cre-pro/",create_profile,name="cre-pro"),
    path("view-pro/",view_profile,name="view-pro"),
    path("edit-pro/",edit_profile,name="edit-pro"),
    path("del-pro/",delete_profile,name="del-pro"),
   
]