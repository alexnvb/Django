from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import *

# Create your views here.

def index(request):
    template = loader.get_template('main.html')

    cpu = Brand.objects.filter(category=2)
    mon = Brand.objects.filter(category=1)

    items = Item.objects.all()

    context = {'cpu':cpu, 'mon':mon, 'items':items}
    return HttpResponse(template.render(context, request))

def item(request, item_id):
    template = loader.get_template('category.html')

    category = Category.objects.filter(id=item_id)
    item_by_cat = Item.objects.filter(category=item_id)
    item_by_brand = Item.objects.filter(brand_id=item_id)

    cpu = Brand.objects.filter(category=2)
    mon = Brand.objects.filter(category=1)

    items = Item.objects.all()

    context = {'category':category, 'item_by_cat':item_by_cat,'cpu': cpu, 'mon': mon, 'items': items, 'item_by_brand':item_by_brand}
    return HttpResponse(template.render(context, request))

def brand(request, item_brand):
    template = loader.get_template('brand.html')

    category = Category.objects.all()
    item_by_cat = Item.objects.all()
    item_by_brand = Item.objects.filter(brand__name=item_brand)

    cpu = Brand.objects.filter(category=2)
    mon = Brand.objects.filter(category=1)

    items = Item.objects.all()

    context = {'category':category, 'item_by_cat':item_by_cat,'cpu': cpu, 'mon': mon, 'items': items, 'item_by_brand':item_by_brand}
    return HttpResponse(template.render(context, request))
