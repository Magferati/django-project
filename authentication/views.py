from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
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

    



 #     username = request.POST.get("username")
    #     password = request.POST.get("password")

    #     user = authenticate(request, username=username,password=password)
    #     if user is not None:
    #      login(request,user)
    #      return redirect("home")
    #     messages.error(request, "Invalid username or password")
    #     return redirect("signin")
 # return render(request, "login.html")