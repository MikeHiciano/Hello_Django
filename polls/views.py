from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question

# Create your views here.
class IndexView(generic.ListView):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.ListView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(generic.ListView):
    model = Question
    template_name = 'polls/result.html'

def vote(request, question_id):
    question_id = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render( request, 'polls/details.html',{
                'question': question,
                'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))