from django.shortcuts import render, get_object_or_404, redirect
from .models import myFriend

# Create your views here.

def home(request):
    myFriends = myFriend.objects
    return render(request, 'home.html',{'myFriends': myFriends})

def detail(request, id):
    column_data = get_object_or_404(myFriend, pk=id)
    return render(request, 'detail.html', {"friend":column_data})

def create(request):
    MyFriend = myFriend()
    MyFriend.title = request.POST['title']
    MyFriend.text = request.POST['text']
    MyFriend.recipe = request.POST['recipe']
    MyFriend.image = request.FILE['image']
    MyFriend.save()
    return redirect('home') #여기들어갈 것은?!

def new(request):
    return render(request, "create.html")