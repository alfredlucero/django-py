import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# Model = single, definitive source of information about your data
# Contains essential fields and behaviors of data you're storing; migrations entirely derived from models file
# Django can update database schema to match your current models

# Django is able to CREATE TABLE based on this database schema
# and create a Python database-access API for accessing Question and Choice objects
# We need to include the app for polls in INSTALLED_APPs as things are pluggable
# python manage.py makemigrations polls
# - migrations are how Django stores changes to models and database schema as files on disk
# - to see the SQL that the migration would run, do python manage.py sqlmigrate polls 0001
# - carry out migration with python manage.py migrate
# 1. Change models in models.py
# 2. Run python manage.py makemigrations to create migrations for those changes
# 3. Run python manage.py migrate to apply those changes to the database
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __str__(self):
    return self.question_text
  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  # Return a better string representation of the object
  def __str__(self):
    return self.choice_text
