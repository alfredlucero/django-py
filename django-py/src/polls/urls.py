from django.urls import path

from . import views

# Make sure to point the root URLconf at polls.urls module in outer urls.py
# We namespace the URLconf to avoid conflicts with other apps
app_name = 'polls'
urlpatterns = [
  # /polls/
  path('', views.index, name='index'),
  # /polls/5/
  path('<int:question_id>/', views.detail, name='detail'),
  # /polls/5/results/
  path('<int:question_id>/results/', views.results, name='results'),
  # /polls/5/vote/
  path('<int:question_id>/vote/', views.vote, name='vote'),
]