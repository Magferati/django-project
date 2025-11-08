from django.shortcuts import render,redirect, get_object_or_404
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout
# from .models import UserProfile
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from .form import ProfileForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view,permission_classes
from .serializars import UserProfile,RegisterSerializar, UserSerializar,ProfileSerializar
from .models import UserProfile
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth.models import User
@api_view(["POST"])
def register(request):
     serializar = RegisterSerializar(data= request.data)
     if serializar.is_valid():
          user = serializar.save()
          user.set_password(serializar.validated_data['password'])
          user.save()


          user_serializar = UserSerializar(user)
          refresh = RefreshToken.for_user(user)
          context = {
               "message":"user successfully register",
               "access_token":str(refresh.access_token),
               "refresh_token": str(refresh),
               "user":user_serializar.data
          }

          return Response(context, status=status.HTTP_201_CREATED)
     return Response(serializar.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
     username = request.data.get("username")
     password = request.data.get("password")

     user = authenticate(username=username, password=password)

     if user :
          refresh = RefreshToken.for_user(user)
          user_serialixar = UserSerializar(user)
          context = {
               "message":"user successfully logged in",
               "access_token":str(refresh.access_token),
               "refresh_token": str(refresh),
               "user":user_serialixar.data
          }

          return Response(context, status=status.HTTP_200_OK)
     return Response({"error":"username and password is invalide"}, status= status.HTTP_401_UNAUTHORIZED)

           
@api_view(["GET"])   
@permission_classes([IsAuthenticated])
def profile(request):
     user = request.user
     profile, created = User.objects.get_or_create(user=user)
     serializer = UserSerializar(profile) 

     return Response(serializer.data,status=status.HTTP_200_OK)  




    
#     if request.method == "POST":
#        # print("request",request.FILES)
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "User created successfully")
#             return redirect("regform")
        
#         messages.error(request, form.errors)
#         return redirect("regform")
#     else:
        
#         form = RegistrationForm()
#         context = {
#             "form": form
#         }
    
#         return render(request, "registration.html", context)
    
# def signin(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     else:
#         if request.method == "POST":
#             form = AuthenticationForm(request, data=request.POST)
#             if form.is_valid():
#               user = form.get_user()
#               auth_login(request, user)
#               messages.success(request, "Login successful!")
#               return redirect("home")
#             else:
#                messages.error(request, "Invalid username or password")
#         else:
#            form = AuthenticationForm()

#            context = {
#            "form": form
#            }
#         return render(request, "login.html", context)
    
# def user_logout(request):
#     logout(request)
#     return redirect("signin")

# @login_required
# def create_profile(request):
#     profile, created = UserProfile.objects.get_or_create(user=request.user)  

#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES, instance=profile)  
#         if form.is_valid():
#             form.save()
#             if created:
#                 messages.success(request, "Profile created successfully!")
#             else:
#                 messages.success(request, "Profile updated successfully!")
#             return redirect("view-pro")
#     else:
#         form = ProfileForm(instance=profile)

#     context = {"form": form}
#     return render(request, "cre_pro.html", context)


# def view_profile(request):
#     profile, created = UserProfile.objects.get_or_create(user=request.user)
#     return render(request, 'view_pro.html', {'profile': profile})

    

# def edit_profile(request):
#     profile, created = UserProfile.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully!")
#             return redirect('view-pro')
#     else:
#         form = ProfileForm(instance=profile)
#         context = {
#             "form" : form
#         }
#     return render(request, 'edit_pro.html', context)


# def delete_profile(request):
#     profile = get_object_or_404(UserProfile, user=request.user)
#     profile.delete()
#     messages.success(request, "Profile deleted successfully!")
#     return redirect('view-pro')


#  #     username = request.POST.get("username")
#     #     password = request.POST.get("password")

#     #     user = authenticate(request, username=username,password=password)
#     #     if user is not None:
#     #      login(request,user)
#     #      return redirect("home")
#     #     messages.error(request, "Invalid username or password")
#     #     return redirect("signin")
#  # return render(request, "login.html")