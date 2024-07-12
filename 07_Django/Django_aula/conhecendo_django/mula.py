views

from django.shortcuts import render
from django. http import HttpResponse
# Create your views here.

def blog(request):
    print('blog')
    return render(
        request,
        'home.html'
    )

def exemplo(request):
    print('exemplo')
    return render(
        request,
        'exemplo.html'
    )


Urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
]
