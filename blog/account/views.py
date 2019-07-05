from django.shortcuts import render
from django.contrib.auth import authenticate,login
# Create your views here.

def user_login(request):
    return render(request,"account/login.html")

def login_handler(request):
    uname = request.POST["uname"]
    upwd=request.POST["upwd"]
    user=authenticate(username=uname,password=upwd)
    if user:
        login(request,user)
        return render(request,"account/index.html")
    else:
        return render(request,"account/login.html")
        
def user_logout(request):
    #logout(request)
    return render(request,"account/login.html")