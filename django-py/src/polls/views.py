from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Choice, Question
from django.views import generic
from django.utils import timezone

# Create your views here. Map views to web pages
# We need to map it to a URL in urls.py (URLconf)
# Views only care about returning HttpResponse or an exception
# Django has a default templating system - can add to templates directory

# Generic views to trim down code even more
# Display a list of objects
class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """Return the last five published questions (not including those set to be published in the future)."""
    # return Question.objects.order_by('-pub_date')[:5]
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# Display a detail page for a particular type of object
# DetailView expects primary key value captured from URL to be called "pk" in urls.py
class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
    # returns string like /polls/3/results/
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def index(request):
#   latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   # template = loader.get_template('polls/index.html')
#   # Context is a dictionary mapping template variable names to Python objects
#   # Context is passed into the template to render the logic
#   context = {
#     'latest_question_list': latest_question_list,
#   }
#   # Shortcut way to render a template given a certain context without needing loader and HttpResponse explicitly
#   return render(request, 'polls/index.html', context)
#   # return HttpResponse(template.render(context, request))
#   # output = ', '.join([q.question_text for q in latest_question_list])
#   # return HttpResponse(output)

# def detail(request, question_id):
#   # Long way
#   # try:
#   #   question = Question.objects.get(pk=question_id)
#   # except Question.DoesNotExist:
#   #   raise Http404("Question does not exist")
#   # Shortcut
#   # There is also get_list_or_404() which uses filter() instead of get() underneath and returns Http404 if list is empty
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/detail.html', { 'question': question })

# def results(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/results.html', { 'question': question })
#   # response = "You're looking at the results of question %s."
#   # return HttpResponse(response % question_id)

# def vote(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   try:
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#   except (KeyError, Choice.DoesNotExist):
#     # Redisplay the question voting form.
#     return render(request, 'polls/detail.html', {
#       'question': question,
#       'error_message': "You didn't select a choice.",
#     })
#   else:
#     selected_choice.votes += 1
#     selected_choice.save()
#     # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
#     # returns string like /polls/3/results/
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
