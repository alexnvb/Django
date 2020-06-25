"""samplesite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bboard.views import index
from bboard.views import by_rubric
from bboard.views import BbCreateView

urlpatterns = [
    path('bboard/<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('bboard/', index, name='index'),
    path('bboard/add/', BbCreateView.as_view(), name='add'),
    path('admin/', admin.site.urls),
]