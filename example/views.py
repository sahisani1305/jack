from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def message(request):
    return render(request, 'message.html')
