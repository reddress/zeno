Zeno

A collection of productivity and personal organization apps

Set TIME_ZONE to 'America/Sao_Paulo'
Set LOGIN_URL, LOGIN_REDIRECT_URL, and LOGOUT_REDIRECT_URL

- Catalogo
- Sistema
- Benny (All Cents)

### Ubuntu setup

Installing Django

~$ virtualenv -p /usr/bin/python3 django2.0
~$ source django2.0/bin/activate
~$ pip install Django
~$ django-admin startproject zeno

zeno$ python manage.py migrate
zeno$ python manage.py createsuperuser
zeno$ python manage.py runserver

~$ source django2.0/bin/activate


### Windows setup

# -v is for verbose
$ virtualenv -v -p /c/Users/Heitor/AppData/Local/
    Programs/Python/Python35-32/python.exe django2.0
$ source django2.0/Scripts/activate
$ pip install Django


### Create a .gitignore

__pycache__/
*.py[cod]
*$py.class

# Django stuff:
*.log
db.sqlite3

media/

# settings
zeno/settings.py

# 'touch runserver' to tab-complete
runserver

### Setting up All Cents' demo data (Benny)

python manage.py createsuperuser (username 'demo',
                                  then use any strong password)

python manage.py shell

from django.contrib.auth.models import User

u = User.objects.get(username='demo')
u.set_password('demo')
u.save()
