from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,"mainapp/index.html",{
        'title':'Inicio'
    })

def about(request):
    return render(request,"mainapp/about.html",{
        'title':'Sobre mí'
    })