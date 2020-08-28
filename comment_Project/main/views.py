from django.views import generic
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post'
    def get_queryset(self): #ListView에서 사용-표시 하려는 개체 목록을 결정한다. 
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post #queryset = Post.objects.all()이랑 같은 기능
    template_name = 'detail.html'
    context_object_name='ppost'

    #다른 정보를 더 보내고 싶으면
    def get_context_data(self, **kwargs):
        #코멘트모델을 보내기위해 작성하는 함수
        context_data = super(DetailView,self).get_context_data(**kwargs) # 오버라이딩하기 위해 필수로 작성해야하는 부분
        context_data['form'] = CommentForm()
        context_data['comments'] = self.object.comment_set.all()
        #self.object는 밖의 모델을 사용하기위해 작성
        #'_set'은 comment가 어디에 ForenginKey로 엮여있는 지 알려주기 위해.
        return context_data

def comment_create(request, post_id):
    if not request.user.is_anonymous:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit = False) #comit은 데이터를 DataBase에 저장하기 전에 특정 행위(DB에 넣을 내용을 추가)를 하기 위해 작성. comit은 기본값이 True이기 때문
            comment.author = request.user
            comment.post_id = post_id
            comment.save()
        else:
            messages.info(request, '올바르지 않은 댓글 형식입니다')
    else:
        messages.info(request, "로그인이 필요합니다")
    return HttpResponseRedirect(reverse('detail', args=(post_id,))) #render는 템플릿에 보내고싶은 DB가 있을 때 사용


def delete(request, delete_id, post_id):
    delete_obj = get_object_or_404(Comment, pk=delete_id)
    if delete_obj.author == request.user:
        delete_obj.delete()
        return HttpResponseRedirect(reverse('detail', args=(post_id,)))
    else:
        messages.info(request, "유저정보가 일치하지않습니다")
    return HttpResponseRedirect(reverse('detail', args=(post_id,)))


def change(request, change_id, post_id):
    change_obj = get_object_or_404(Comment, pk=change_id)
    if change_obj.author == request.user:
        if request.method == "POST":
            change_obj.content = request.POST['Recomment']
            change_obj.save()
            return HttpResponseRedirect(reverse('detail', args=(post_id,)))
        else:
            pass
        return render(request,'change.html')
    else:
        messages.info(request, "유저정보가 일치하지않습니다")
    return redirect('change')


