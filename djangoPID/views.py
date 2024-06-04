from django.shortcuts import render

def index(request):
    return render(request, 'djangoPID/index.html')

def predictions(request):
    return render(request, 'djangoPID/predictions.html')
