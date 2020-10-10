from django.shortcuts import render
from .models import Orders, Members, Goods, Sheets

# Create your views here.

def index(request):
    sheets_rows = Sheets.objects.all()
    return render(request, 'index.html', {"sheets_rows":sheets_rows})