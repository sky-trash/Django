from django.shortcuts import render, HttpResponse

def hello(request): 
    return HttpResponse('Hello world!!!')
