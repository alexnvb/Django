from django.shortcuts import render
from .forms import SubscribersForm

def landing(request):
    form = SubscribersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_form = form.save()
        print(request.POST)


    return render(request, 'landing/landing.html', locals())