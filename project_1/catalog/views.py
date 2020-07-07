from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import *

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    cat = Category.objects.all()
    # mon = Brand.objects.filter(category=1)
    # cpu = Brand.objects.filter(category=2)
    context = {'mon': mon,'cpu': cpu, 'cat':cat}
    return HttpResponse(template.render(context, request))