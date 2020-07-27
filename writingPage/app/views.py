from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Writing
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.models import User

class index(ListView):
    template_name = "index.html"
    context_object_name = "writing_list" 
    def get_queryset(self):
        return Writing.objects.all

class detail(DetailView):
    model = Writing
    template_name = 'detail.html'
    context_object_name = 'writing'

class delete(DeleteView):
    model = Writing
    template_name = 'delete.html'
    context_object_name = 'writing'
    success_url = reverse_lazy('index')

class update(UpdateView):
    model = Writing
    template_name = 'update.html'
    fields = ['title','text']
    success_url = reverse_lazy('index')

class create(CreateView):
    model = Writing
    template_name = 'create.html'
    fields = ['title','text']
    def form_valid(self,form):
        Writing = form.save(commit=False)
        Writing.author = self.request.user
        Writing.save()
        return HttpResponseRedirect(self.request.POST.get('next','/'))


def result(request):
    WritingPosts = Writing.objects.all()
    query = request.GET.get('query', '')
    setting = request.GET.get('setting', '')
    user =request.user
    if query and setting == "all":
        WritingPosts = WritingPosts.filter(Q(title__icontains = query)| Q(text__icontains = query) | Q(author__username__icontains = query) ).order_by('-time')
    elif query and setting == "title":
        WritingPosts = WritingPosts.filter(Q(title__icontains = query)).order_by('-time')
    elif query and setting == "text":
        WritingPosts = WritingPosts.filter(Q(text__icontains = query)).order_by('-time')
    elif query and setting == "author":
        WritingPosts = WritingPosts.filter(Q(author__username__icontains = query)).order_by('-time')
    return render(request, 'result.html',{'WritingPosts' : WritingPosts, 'query':query,'setting':setting,'user':user,})
