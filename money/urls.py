from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'money'

urlpatterns = [
    path('',
         views.IndexView.as_view(),
         name='index'),
    
    path('accountType/',
         login_required(views.AccountTypeList.as_view()),
         name='accountTypeList'),
    
    path('accountType/<int:pk>/',
         login_required(views.AccountTypeDetail.as_view()),
         name='accountTypeDetail'),
    
    path('accountType/create/',
         login_required(views.AccountTypeCreate.as_view()),
         name="accountTypeCreate"),

    path('accountType/update/<int:pk>/',
         login_required(views.AccountTypeUpdate.as_view()),
         name="accountTypeUpdate"),

    path('accountType/delete/<int:pk>/',
         login_required(views.AccountTypeDelete.as_view()),
         name="accountTypeDelete"),
]
