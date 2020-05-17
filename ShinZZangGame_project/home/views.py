from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, '짱구.html')
