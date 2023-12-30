from django.shortcuts import render , get_object_or_404
from django.http import  HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questionList"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-when_aksed")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        voter_choice = question.choice_set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html",{"question" : question , "error_messgae" : "You did not select a choice"})
    else:
        voter_choice.votes += 1
        voter_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        