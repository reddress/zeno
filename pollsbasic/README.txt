Part 1:
https://docs.djangoproject.com/en/2.0/intro/tutorial01/

Write your first view

Create urls.py in pollsbasic, using 'from django.urls import path'
(no longer uses 'from django.conf.urls import url')

Edit zeno/urls.py


Part 2:
https://docs.djangoproject.com/en/2.0/intro/tutorial02/

Database (just use SQLite for now)

Creating models

Add app to INSTALLED_APPS

Run python manage.py makemigrations
Then migrate

Command-line API Shell: Question and choices are created here
python manage.py shell

Register models in Admin


Part 3:
https://docs.djangoproject.com/en/2.0/intro/tutorial03/

Write more views

Create templates directory

Create index template

(long method: from django.template import loader)

render() shortcut

get_object_or_404()

template system

{% url %} template tag and URL namespacing


Part 4:
https://docs.djangoproject.com/en/2.0/intro/tutorial04/

Write a simple form

Write a functioning vote view

"Why the code-shuffle?" marks the end of pollsbasic
