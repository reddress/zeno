from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import general
from .views import account_type
from .views import account

app_name = 'money'

urlpatterns = [
    path('',
         general.IndexView.as_view(),
         name='index'),
    
    # AccountType

    path('accountType/',
         login_required(account_type.AccountTypeList.as_view()),
         name='accountTypeList'),
    
    path('accountType/<int:pk>/',
         login_required(account_type.AccountTypeDetail.as_view()),
         name='accountTypeDetail'),
    
    path('accountType/create/',
         login_required(account_type.AccountTypeCreate.as_view()),
         name="accountTypeCreate"),

    path('accountType/update/<int:pk>/',
         login_required(account_type.AccountTypeUpdate.as_view()),
         name="accountTypeUpdate"),

    path('accountType/delete/<int:pk>/',
         login_required(account_type.AccountTypeDelete.as_view()),
         name="accountTypeDelete"),

    # Account

    path('account/',
         login_required(account.AccountList.as_view()),
         name='accountList'),
    
    path('account/<int:pk>/',
         login_required(account.AccountDetail.as_view()),
         name='accountDetail'),
    
    path('account/create/',
         login_required(account.AccountCreate.as_view()),
         name="accountCreate"),

    path('account/update/<int:pk>/',
         login_required(account.AccountUpdate.as_view()),
         name="accountUpdate"),

    path('account/delete/<int:pk>/',
         login_required(account.AccountDelete.as_view()),
         name="accountDelete"),

]
