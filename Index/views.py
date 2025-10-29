from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Myself
# Create your views here.
from .form import MyselfForm 
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect("signin")

# def about(request):
#     message = "This is a scrolling news ticker in Django!"
#     return render(request, "about.html", {"message": message})

def about(request):
    return render(request, "about.html")



def get_all(request):
    print("request",request)
    
    myself_list = Myself.objects.all().order_by("-create_at")
    context = {
        "data": myself_list,
        "html_title" : "My Information page."
    }
    return render(request, "view_info.html", context)



def get_data_by_id(request, id):
    print("request",request)
    
    myself_list = Myself.objects.get(id=id)
    
    context = {
        "items": myself_list,
        "html_title" : "View Information page"
    }
    return render(request, "view_info.html", context)



def create(request):
    
    if request.method == "POST":
        print("request",request.FILES)
        form = MyselfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Add Information successfully")
            return redirect("add-info")
        
        messages.error(request, "error adding data.")
        return redirect("add-info")
    else:
        
        form = MyselfForm()
        context = {
            "form": form
        }
    
        return render(request, "add_info.html", context)
    
    
    

def update(request, id):
    
    try:

      myself = Myself.objects.get(id=id)
    except Exception as e:
        print(e)
        return HttpResponse(f"{id} {e}")
      
    if request.method =="POST":
        
        form = MyselfForm(request.POST, instance=myself)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Info sucessfully updated")
            
            return redirect("update", id=myself.id)
        
        messages.error("error updating data")
        return redirect("update", id=myself.id)
   

    form = MyselfForm(instance=myself)
    
    context = {
    "id": myself.id,
    "form": form
    }

    return render(request, "edit_info.html", context)
    

    

def delete(request, id):
    try:

     myself = Myself.objects.get(id=id)
    except Exception as e:
        print(e)
        return HttpResponse(f"{id} {e}")

    myself.delete()
    messages.success(request, "Data deleted succesfully")
    return redirect("get-all")


