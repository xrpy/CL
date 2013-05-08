from django.http import HttpResponse
from survey.models import ANSWERS, QUESTIONS, RESULTS, WEIGHT
from django.template import Context, loader
from survey.logic import getResults
from django.shortcuts import render

def index(request):
    all_question_list = QUESTIONS.objects.all()
    all_answer_list = ANSWERS.objects.all()
    return render(request,'survey/welcome.html',{'questionList': all_question_list, 'answerList': all_answer_list,})

def results(request):
    answer_list = request.POST.getlist('answer')
    result_list=getResults(answer_list)[:3]

    return render(request, 'survey/results.html', {'results':result_list})

