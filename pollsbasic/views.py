from django.http import HttpResponse

# Part 3
from django.http import Http404

# Part 3
# from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Part 4
from django.urls import reverse
from django.http import HttpResponseRedirect

# Part 3
from .models import Question

# Part 4
from .models import Choice

# Part 1, 3
def index(request):
    # return HttpResponse("Hello, you are at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # Part 3
    # template = loader.get_template("pollsbasic/index.html")
    # context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, 'pollsbasic/index.html')

# Part 3
def detail(request, question_id):
    # return HttpResponse("Viewing question %s" % question_id)
    # try:
        # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
        # raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollsbasic/detail.html', {'question': question})


def results(request, question_id):
    # response = "Viewing Results of question %s"
    # return HttpResponse(response % question_id)

    # Part 4
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollsbasic/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse("Voting on question %s" % question_id)

    # Part 4
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

