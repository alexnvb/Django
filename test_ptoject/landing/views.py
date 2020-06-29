from django.shortcuts import render
from .forms import SubscribersForm

def landing(request):
    form = SubscribersForm(request.POST or None)
    return render(request, 'landing/landing.html', locals())