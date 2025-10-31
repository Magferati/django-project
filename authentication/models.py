from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11,blank=True,null=True)
    profile_picture = models.ImageField(upload_to="profile",blank=True,null=True)

