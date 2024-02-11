from django.shortcuts import render

# Create your views here.

def home(rewuest):
    return render(request, 'home.html', {})