from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models  import User


   

class ProfileSerializar(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ["id","phone_number","profile_picture"]

class RegisterSerializar(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id","username","email","first_name","last_name","password"]
        extra_kwargs = {'password': {'write_only': True}}

class UserSerializar(serializers.ModelSerializer):
    user_profile = ProfileSerializar(source="userprofile", required=False)
  
    class Meta:
        model = User
        fields = ["id","username","email","first_name","last_name","user_profile"]
        