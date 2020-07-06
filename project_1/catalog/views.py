from django.shortcuts import render
from .models import *

# Create your views here.

def index(request, category_id):
    return render(request,'index.html')