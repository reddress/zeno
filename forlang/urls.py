from django.urls import path

from . import views

app_name = 'forlang'

urlpatterns = [
    path('', views.index, name='index'),
    path('addEntry/', views.addEntry, name='addEntry'),
]
