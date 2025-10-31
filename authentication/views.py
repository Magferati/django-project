from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .form import ProfileForm
# Create your views here.
from .form import RegistrationForm
from django.contrib import messages

def register(request):
    
    if request.method == "POST":
       # print("request",request.FILES)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
            return redirect("regform")
        
        messages.error(request, form.errors)
        return redirect("regform")
    else:
        
        form = RegistrationForm()
        context = {
            "form": form
        }
    
        return render(request, "registration.html", context)
    
def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
              user = form.get_user()
              auth_login(request, user)
              messages.success(request, "Login successful!")
              return redirect("home")
            else:
               messages.error(request, "Invalid username or password")
        else:
           form = AuthenticationForm()

           context = {
           "form": form
           }
        return render(request, "login.html", context)
    
def user_logout(request):
    logout(request)
    return redirect("signin")

@login_required
def create_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)  

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)  
        if form.is_valid():
            form.save()
            if created:
                messages.success(request, "Profile created successfully!")
            else:
                messages.success(request, "Profile updated successfully!")
            return redirect("view-pro")
    else:
        form = ProfileForm(instance=profile)

    context = {"form": form}
    return render(request, "cre_pro.html", context)


def view_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'view_pro.html', {'profile': profile})

    

def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('view-pro')
    else:
        form = ProfileForm(instance=profile)
        context = {
            "form" : form
        }
    return render(request, 'edit_pro.html', context)


def delete_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile.delete()
    messages.success(request, "Profile deleted successfully!")
    return redirect('view-pro')


 #     username = request.POST.get("username")
    #     password = request.POST.get("password")

    #     user = authenticate(request, username=username,password=password)
    #     if user is not None:
    #      login(request,user)
    #      return redirect("home")
    #     messages.error(request, "Invalid username or password")
    #     return redirect("signin")
 # return render(request, "login.html")