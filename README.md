# django-py

## Installation

Install all the packages (you may also use virtual env i.e. venv to be sure you're on Python 3.10.6)

```bash
pip install -r requirements.txt
```

If you're installing new packages, you can do this

```bash
pip install <some-package>
pip freeze > requirements.txt
```

## Starting up

Start up the server with

```bash
cd django-py/src
python manage.py runserver
```

It should run on `localhost:8000/`
