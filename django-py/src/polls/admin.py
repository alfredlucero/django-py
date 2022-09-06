from django.contrib import admin

from .models import Question, Choice

# Register your models here.
# For polls app to display on the admin index page, we need to register the models
admin.site.register(Question)
admin.site.register(Choice)