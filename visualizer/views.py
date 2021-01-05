from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {}
    return render(request, 'home.html', context)
    
def user(request):
    context = {}
    return render(request, 'user.html', context)

def repo(request):
    context = {}
    return render(request, 'repo.html', context)