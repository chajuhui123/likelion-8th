from django.shortcuts import render, get_object_or_404, redirect
from .models import Youtuber

# Create your views here.

def youtuber(request):
    youtuber = Youtuber.objects.all()
    return render(request,'youtuber.html',{'youtuber' : youtuber})

def detail(request,detail_id):
    detail = get_object_or_404(Youtuber, pk = detail_id)
    return render(request, 'detail.html',{'content':detail})

def create(request):
    Youtube = Youtuber()
    Youtube.channel = request.POST['name']
    Youtube.creater = request.POST['creator']
    Youtube.subscriber = request.POST['subscribe_num']
    Youtube.link1 = request.POST['youtube_link1']
    Youtube.link2 = request.POST['youtube_link2']
    Youtube.link3 = request.POST['youtube_link3']
    Youtube.summary = request.POST['summary']
    Youtube.text = request.POST['text']
    Youtube.onAir = request.POST['choices']
    Youtube.save()
    return redirect("youtuberList")

def new(request):
    return render(request, "create.html")