from django.shortcuts import render
from .forms import Firstform, Secondform
 #forms에서 Fristform을 불러온다

# Create your views here.
def index(request):
    form = Firstform()
    form2 = Secondform()
    return render(request, 'index.html', {'form':form, 'form2':form2,})