from django.shortcuts import render
from .models import Person

# Create your views here.
def home(request):
    persons = Person.objects
    return render(request, 'home.html',{'persons':persons})