from django.contrib.auth import models,authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Person
# Create your views here
def Homepage(request):
        if request.method=="GET":
             return render(request,"index.html")
        elif request.method=="POST":
             user=request.POST.get("name")
             pwd=request.POST.get("password")
             u=authenticate(name=user,password=pwd)
             try:
                person = Person.objects.get(name=user, password=pwd)
                request.session['id'] = person.id
                return redirect("appPage")
             except Person.DoesNotExist:
                return HttpResponse("Login Failed: Invalid credentials")
def SignupPage(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        usr = request.POST.get("name")
        pwd = request.POST.get("password")
        repwd = request.POST.get("password2")
        email = request.POST.get("email")

        if pwd != repwd:
            messages.error(request, "Passwords do not match")
            return render(request, "signup.html")

        if Person.objects.filter(name=usr).exists():
            messages.error(request, "Username already exists")
            return render(request, "signup.html")

        person = Person(name=usr, password=pwd, email=email)
        person.save() 

        return redirect("login")
def signout():
     return redirect("login")
def appPage(request):
    userid=request.session.get("id")
    if userid:
        person= Person.objects.get(id=userid)
        return render(request,"appPage.html",{"Username":person.name})
    return HttpResponse("User not logged in ")