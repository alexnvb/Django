# from django.conf.urls import path, url, include
# from django.contrib import admin
# from landing import views
#
# urlpatterns = [
#     path('landing/', views.landing, name='landing')
# ]

from django.contrib import admin
from django.urls import path, include
from landing import views

urlpatterns = [
    path('landing/', views.landing, name='landing'),
]