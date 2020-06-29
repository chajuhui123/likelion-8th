from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import gallery_photo

# Create your views here.
def home(request):
    photos = gallery_photo.objects
    return render(request,'home.html',{'photos':photos})

def detail(request, detail_id):
    detail_obj = get_object_or_404(gallery_photo, pk=detail_id)
    return render(request,'detail.html',{"detail_key":detail_obj})

def add(request):
    if request.method == "POST":
        Gallery_photo = gallery_photo()
        Gallery_photo.photo = request.POST['photo']
        Gallery_photo.title = request.POST['title']
        Gallery_photo.date = request.POST['date']
        Gallery_photo.save()
        return redirect('home')
    else:
        pass
    return render(request, 'add.html')

def change(request, change_id):
    change_obj = get_object_or_404(gallery_photo,pk=change_id)
    if request.method == "POST":
        change_obj.photo = request.POST['photo']
        change_obj.title = request.POST['title']
        change_obj.date = request.POST['date']
        change_obj.save()
        return redirect(reverse('detail',args=(change_id,)))
    else:
        pass
    return render(request, 'change.html',{'change_key':change_obj})
    
def delete(request, delete_id):
    delete_obj = get_object_or_404(gallery_photo, pk = delete_id)
    delete_obj.delete()
    return redirect('home')
