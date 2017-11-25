Zeno

A collection of productivity and personal organization apps.

Set USE_TZ = False

- pollsbasic: Tutorial up to "basic math/calculator" comment
- pollscalc: Tutorial "using a calculator"
- bulletinboard: users can post, anyone can read
- todo: Tasks
- diary: Mytags/tagdiary
- money: Alexie Beans clone

Pontual-related
- Aguardando

* Ubuntu setup

Installing Django

~$ virtualenv -p /usr/bin/python3 django2.0
~$ source django2.0/bin/activate
~$ pip install --pre django
~$ django-admin startproject zeno

zeno$ python manage.py migrate
zeno$ python manage.py createsuperuser
zeno$ python manage.py runserver

~$ source django2.0/bin/activate

Create a .gitignore

__pycache__/
*.py[cod]
*$py.class

# Django stuff:
*.log
db.sqlite3

media/

# settings
zeno/settings.py

runserver
