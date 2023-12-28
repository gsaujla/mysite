from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.

def firsthello(request):
   return HttpResponse('Welcome to The Polls Website!')

def q_detail(request, q_id):
   try:
        question = Question.objects.get(pk=q_id)
   except Question.DoesNotExist:
        raise Http404("Question does not exist")
   return render(request, 'polls/details.html', {"question" : question , "q_id" : q_id})

def results(request, q_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % q_id)


def vote(request, q_id):
    return HttpResponse("You're voting on question %s." % q_id)

def index(request):
    questionList = Question.objects.order_by("-when_aksed")[:5]
    context = {
        "questionList" : questionList
        }
    return render(request , 'polls/index.html', context)
