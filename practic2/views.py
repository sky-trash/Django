from django.shortcuts import render, HttpResponse


def hello(request):
    return render(request, 'index.html',{
        'title':'book page',
        'bookName':'Чеовек паук: Вдали от дома',
    })