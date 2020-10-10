from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from .models import Question, Choice #choice를 import 해오지 않아도 되는 이유는 question_id를 프라이머리키로 가져오기 때문에
from django.urls import reverse

class IndexView(generic.ListView):
    template_name = 'cbv/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailVeiw(generic.DetailView):
    model = Question
    template_name = "cbv/detail.html"

class ResultsVeiw(generic.DetailView):
    model = Question
    template_name = "cbv/results.html"

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
