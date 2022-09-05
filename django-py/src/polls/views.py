from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# We need to map it to a URL in urls.py (URLconf)
def index(request):
  return HttpResponse("Hello, django unchained. You're at polls index")
