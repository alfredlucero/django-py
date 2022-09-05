from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

# Create your views here. Map views to web pages
# We need to map it to a URL in urls.py (URLconf)
# Views only care about returning HttpResponse or an exception
# Django has a default templating system - can add to templates directory
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  # Context is a dictionary mapping template variable names to Python objects
  # Context is passed into the template to render the logic
  context = {
    'latest_question_list': latest_question_list,
  }
  # Shortcut way to render a template given a certain context without needing loader and HttpResponse explicitly
  return render(request, 'polls/index.html', context)
  # return HttpResponse(template.render(context, request))
  # output = ', '.join([q.question_text for q in latest_question_list])
  # return HttpResponse(output)

def detail(request, question_id):
  # Long way
  # try:
  #   question = Question.objects.get(pk=question_id)
  # except Question.DoesNotExist:
  #   raise Http404("Question does not exist")
  # Shortcut
  # There is also get_list_or_404() which uses filter() instead of get() underneath and returns Http404 if list is empty
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', { 'question': question })

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)