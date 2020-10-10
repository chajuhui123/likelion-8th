from django.shortcuts import render
from django.urls import path
import datetime



#데이터를 웹에 보내고 싶을 때 views.py 를 이용하면 된다.

def home (request):
    a = 3
    b = 6
    c = a + b
    name = "Juhee"
    now = datetime.datetime.now()
    day = ['mon','tue','wed']
    return render(request,'firstapp_templates/home.html',{"day" : day}) #변수를 불러줌

def first (request):
    return render(request,'firstapp_templates/first.html')


def second (request):
    return render(request,'firstapp_templates/second.html')

def third (request):
    return render(request,'firstapp_templates/third.html')