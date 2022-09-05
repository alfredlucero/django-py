from django.urls import path

from . import views

# Make sure to point the root URLconf at polls.urls module in outer urls.py
urlpatterns = [
  path('', views.index, name='index')
]