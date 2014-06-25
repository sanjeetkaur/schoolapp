from django.shortcuts import render
from app.models import *

def index(request):
    return render(request, 'first.html')
def display (request):
    if 'info' in  request.GET:
        info = request.GET.getlist('info')
        return render(request, 'final.html', { 'info': info })
    else:
        a = 'nothing selected'
        return render(request, 'final.html', {'error':True, 'else':a})
