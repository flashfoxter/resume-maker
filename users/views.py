from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from .models import Register

def home(request):
    return render(request,'base.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/cv/resume')
    else:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                register=Register(username=form.cleaned_data['username'],
                              email=form.cleaned_data['email'])
                register.save()
                form.save()
            
                return redirect('../accounts/login')
        else:
            form = UserRegisterForm()

        context = {'form' : form}
    
        return render(request, 'register.html', context)
