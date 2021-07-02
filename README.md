# regression-cluster-be
The back end for a regression clustering test I am working on.

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