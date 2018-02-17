from django.urls import path
from django.contrib.auth.views import login, logout

from . import views

app_name = 'zenousers'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_and_login/', views.create_and_login, name='create_and_login'),
    path('login/', login,
         {'template_name': 'users/login.html'}, name='login'),
    path('logout/', logout, name='logout'),
]
