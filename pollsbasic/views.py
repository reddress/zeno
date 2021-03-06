# cleaned up, see views_allparts.py for entire history

from django.http import Http404

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'pollsbasic/index.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollsbasic/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollsbasic/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # retrieve the 'name="choice"' input from HTML form
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'pollsbasic/detail.html',
                      {'question': question,
                       'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully
        # dealing with POST data. This prevents data from being
        # posted twice if Back button it pressed
        return HttpResponseRedirect(reverse('pollsbasic:results',
                                            args=(question.id,)))

