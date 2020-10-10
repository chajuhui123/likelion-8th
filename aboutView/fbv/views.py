from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice #choice를 import 해오지 않아도 되는 이유는 question_id를 프라이머리키로 가져오기 때문에
from django.urls import reverse

#Question 모델에 pub_date기준 가장 최신 5개 리스트로 보여주기
def index(request):
    #question_obj = Question.objects
    #return render(request, 'fbv/index.html', {"question_key":question_obj})
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #pub date 기준으로 내림차순 0개부터 4개까지
    return render(request, 'fbv/index.html', {"latest_question_list":latest_question_list})

#Question 모델에 질문 하나를 클릭하면 그거에 해당하는 detail 페이지를 보여주기
def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {
        'question':question
    }
    return render(request, 'fbv/detail.html', context)

#Question의 질문 투표 결과를 보여주기
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'fbv/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExit):
        return render(request, 'fbv/detail.html', {'question':question, 'error_msg':"you didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save() #갱신되기위해선 save가 있어야함
    return HttpResponseRedirect(reverse('fbv:results', args=(question.id,)))
