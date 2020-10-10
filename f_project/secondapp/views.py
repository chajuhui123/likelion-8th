from django.shortcuts import render
from django.urls import path


def home (request):
    return render(request,'secondapp_templates/home.html') #변수를 불러줌