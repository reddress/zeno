from django.urls import path

from . import views

app_name = 'bulletinboard'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add_form/', views.add_form, name='add_form'),
    path('add/', views.add, name='add'),
]
