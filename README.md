# Django Playground
Just a cool place to hangout and learn django.

> Quickstart just type ./initscript

cd !$ ? 

## How I set up the virtual env
```bash
pip install virtualenv
virtualenv regression_env
source regression_env/Scripts/activate
which python
```

## Installing some packages local to the env to test
```bash
pip list

pip install numpy
pip install pytz
pip install psutil

pip list
```

### Exporting requirements documentation
```bash
pip freeze --local > requirements.txt
```

> you can use 'deactivate' in the bash to exit your virtual environment

### Created a new project ``regression`` via
```bash
django-admin startproject regression
```

### Booting up app
```bash
python regression/manage.py runserver
```

### Creating a database and super user
```bash
python regression/manage.py makemigrations
python regression/manage.py migrate
python regression/manage.py createsuperuser
```

### Checking what SQL will be run by migration
```bash
python regression/manage.py sqlmigrate blog 0001
```

### Run to migrate changes to schema
```bash
python regression/manage.py makemigrations
python regression/manage.py migrate
```

### Opening shell to work with db model
```bash
python regression/manage.py shell # open shell
from blog.models import Post
from django.contrib.auth.models import User
User.objects.all()
User.objects.filter(username='stujmar')
Post.objects.all()
user = User.objects.filter(username='stujmar').first()

post_1 = Post(title='Blog Title One', content='First Post Content', author=user)

post_2 = Post(title='Pickle Pepper', content='Pickle Content', author=user)

post_1.save()
post_2.save()
```

### Date Formatting

docs 
> https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#date

example
```bash
<small class="text-muted">{{ post.date_posted|date:"F jS Y" }}</small>
```
