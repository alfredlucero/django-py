from django.contrib import admin

from .models import Question, Choice

# Customize the admin experience by creating a model admin class, then pass it in as second argument to register
class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  # fields = ['pub_date', 'question_text']
  fieldsets = [
    (None, { 'fields': ['question_text'] }),
    ('Date information', { 'fields': ['pub_date'] })
  ]
  # Choice objects are edited on the Question admin page, provide enough fields for 3 choices
  inlines = [ChoiceInline]
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']
  search_fields = ['question_text']

# Register your models here.
# For polls app to display on the admin index page, we need to register the models
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)