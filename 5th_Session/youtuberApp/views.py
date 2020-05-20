from django.shortcuts import render
from .models import Youtuber

# Create your views here.

def youtuber(request):
    youtuber1 = Youtuber.objects.get(id=1)
    youtuber2 = Youtuber.objects.get(id=2)
    youtuber3 = Youtuber.objects.get(id=3)

    return render(request,'youtuber.html',{'youtuber1' : youtuber1, 'youtuber2':youtuber2, 'youtuber3' : youtuber3})