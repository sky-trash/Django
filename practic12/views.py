from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import LoginForm
from django.contrib.auth import login, logout

def login_user(req:HttpRequest):
    if req.method == 'POST':
        form = LoginForm(req, data=req.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(req, user)
                return redirect('profile')
    else:
        form = LoginForm()
        return render(req, 'practic12_login.html', context={
            'title':'Авторизация',
            'form': form,
        })
    
def logout_user(req:HttpRequest):
    if req.method == 'POST':
        logout(req)
        
    return redirect('mainPage')