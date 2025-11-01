from django.urls import path
from .views import get_data
urlpatterns = [
    path("get/student-list/", get_data)
]