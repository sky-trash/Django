from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.http import HttpRequest

def register(req:HttpRequest):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('mainPage') 
    else:
        form = RegisterForm()
        return render(req, 'practic11_registration.html', context = {
            'title':'Регистрация',
            'form':form,
        })
