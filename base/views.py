from django.shortcuts import render

req = 'intro'

def home(request):
    req = 'HOME'
    return render(request, 'base/home.html', {'req':req})

def intro(request):
    req = 'INTRO'
    return render(request, 'base/intro.html', {'req':req})


# <!-- {% extends 'base/temp.html' %} -->


