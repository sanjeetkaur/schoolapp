from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

def index(request):
    return render(request, 'first.html')
# Create your views here.
