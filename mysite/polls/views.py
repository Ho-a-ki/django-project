from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question





def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    res =  f"당신은 {question_id}번 째 질문의 결과를 보고 있습니다."
    return HttpResponse(res)

def vote(request, question_id):
    res =  f"당신은 {question_id}번 째 질문에다가 투표했습니다."
    return HttpResponse(res)

