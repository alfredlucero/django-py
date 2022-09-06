# django-py

## Installation

Install all the packages (you may also use virtual env i.e. venv to be sure you're on Python 3.10.6 - `source django-py/bin/activate` and check `python --version`)

```bash
pip install -r requirements.txt
```

If you're installing new packages, you can do this

```bash
pip install <some-package>
pip freeze > requirements.txt
```

If you see initial database migration errors, you can do this

```bash
# In the src folder
python manage.py migrate
```

To migrate changes to your database models, you can do this

```bash
# In the src folder, run this to prepare the migrations
python manage.py makemigrations polls # <someapp>
# To see the SQL the migration would run
python manage.py sqlmigrate polls 0001 # migration file version
# Then carry out the migration to synchronize everything
python manage.py migrate
```

## Starting up

Start up the server with

```bash
cd django-py/src
python manage.py runserver
```

It should run on `localhost:8000/`

To check if any problems in your project, try

```bash
python manage.py check
```

There is also an interactive Python shell to play around with the free API Django gives you

```bash
python manage.py shell
```

```python
# Inside you can interact with the database API and import model classes
from polls.model import Choice, Question

# No questions in system yet
Question.objects.all()

# Create a question
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())

# Save object to database
q.save()

# Should have ID
q.id

# Access model field values via Python attributes
q.question_text
q.pub_date

# Change values and save
q.question_text = "What's up?"
q.save()

# objects.all() displays all the questions in the database
Question.objects.all()

# Create a choice
q.choice_set.create(choice_text='Yes', votes=0)
# Get all choices for question
q.choice_set.all()
```

## Running tests

We can run our tests like this

```bash
python manage.py test polls # <app>
```

## Admin Management

Django automates the creation of admin interfaces for models.

Create a user who can login to the admin site with

```bash
python manage.py createsuperuser
```

After running the server with `python manage.py runserver`, go to `localhost:8000/admin/` to see the admin site where you can log in with the user you created.
