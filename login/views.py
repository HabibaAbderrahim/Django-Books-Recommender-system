from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse, HttpResponseBadRequest ,  HttpResponseRedirect
from django.http.request import  HttpRequest
from .forms import RegisterForm , UserLoginForm ,  UserLoginForm , LoginForm
from django.urls import reverse


def send_email(response):
    if response.method == "POST":
      form = RegisterForm(response.POST) 
      if form.is_valid():
        
         form.save()
         

        
      
    else:
      form = RegisterForm()
    return render(response,"login/login.html",{"form":form})



        

  

def user_login (request): 
 
 if request.method == "POST":
   form =  UserLoginForm(request.POST)
   username = request.POST["username"]
   password  = request.POST["password"]
   user = authenticate(username = username , password =password)
   if user :
     login(request, user)
     return HttpResponseRedirect(reverse('user_login'))
   

 else :
    form = UserLoginForm()
    return render(request,"login/loginUser.html",{"form":form})

def user_success(request): 
  pass
def user_logout (request): 
  pass 

def profile(request):   # I need to change directory form here
    return render(request, 'movie/templates/movie/movie_list.html')


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'movie/movie_archive_year.html')
        else:
            print("error.......")

    return render(request, "login/loginU.html", context=context)



def logout_page(request):
    logout(request)
    return render(request,  'movie/movie_list.html')