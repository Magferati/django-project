from django.urls import path
from .views import create, get_all, about , update , delete ,home ,about , get_data_by_id


urlpatterns = [
    path("add-info/", create , name="add-info"),
    path("get-all/", get_all, name="get-all"),
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("delete/<int:id>/", delete, name="delete" ),
    path("info/<int:id>/", get_data_by_id, name="get_data_by_id" ),
    path("update/<int:id>/", update, name="update"),
]