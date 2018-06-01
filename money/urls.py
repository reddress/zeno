from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import general
from .views import account_type, account, transaction

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

    path('accountType/edit/<int:pk>/',
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

    path('account/edit/<int:pk>/',
         login_required(account.AccountUpdate.as_view()),
         name="accountUpdate"),

    path('account/delete/<int:pk>/',
         login_required(account.AccountDelete.as_view()),
         name="accountDelete"),


    # Transaction

    path('transaction/',
         login_required(transaction.TransactionList.as_view()),
         name='transactionList'),
    
    path('transaction/<int:pk>/',
         login_required(transaction.TransactionDetail.as_view()),
         name='transactionDetail'),
    
    path('transaction/create/',
         login_required(transaction.TransactionCreate.as_view()),
         name="transactionCreate"),

    path('transaction/edit/<int:pk>/',
         login_required(transaction.TransactionUpdate.as_view()),
         name="transactionUpdate"),

    path('transaction/delete/<int:pk>/',
         login_required(transaction.TransactionDelete.as_view()),
         name="transactionDelete"),

    
    # Account Type summary: filter transactions
    
    # Account Type summary for default currency, given 'from' and 'to' dates
    path('accountType/<int:from_d>/<int:from_m>/<int:from_y>/<int:to_d>/<int:to_m>/<int:to_y>/',
         login_required(account_type.AccountTypeListTime.as_view()),
         name='accountTypeListTime'),

    # Account Type summary for given currency, all dates
    path('accountType/<str:currency_code>/',
         login_required(account_type.AccountTypeListCurrency.as_view()),
         name='accountTypeListCurrency'),

    # Account Type summary for given currency and 'from' and 'to' dates
    path('accountType/<str:currency_code>/<int:from_d>/<int:from_m>/<int:from_y>/<int:to_d>/<int:to_m>/<int:to_y>/',
         login_required(account_type.AccountTypeListCurrencyTime.as_view()),
         name='accountTypeListCurrencyTime'),

    # Account Type summary starting from given date
    path('accountType/<int:from_d>/<int:from_m>/<int:from_y>/',
         login_required(account_type.AccountTypeListFrom.as_view()),
         name='accountTypeListFrom'),
    
    path('accountType/<str:currency_code>/<int:from_d>/<int:from_m>/<int:from_y>/',
         login_required(account_type.AccountTypeListCurrencyFrom.as_view()),
         name='accountTypeListCurrencyFrom'),


    # Account summary: filter transactions

    # Account summary for default currency, given 'from' and 'to' dates
    path('account/<int:pk>/<int:from_d>/<int:from_m>/<int:from_y>/<int:to_d>/<int:to_m>/<int:to_y>/',
         login_required(account.AccountDetailTime.as_view()),
         name='accountDetailTime'),

    # Account summary for given currency, all dates
    path('account/<int:pk>/<str:currency_code>/',
         login_required(account.AccountDetailCurrency.as_view()),
         name='accountDetailCurrency'),

    # Account summary for given currency and 'from' and 'to' dates
    path('account/<int:pk>/<str:currency_code>/<int:from_d>/<int:from_m>/<int:from_y>/<int:to_d>/<int:to_m>/<int:to_y>/',
         login_required(account.AccountDetailCurrencyTime.as_view()),
         name='accountDetailCurrencyTime'),

    # Account summary starting from given date
    path('account/<int:pk>/<int:from_d>/<int:from_m>/<int:from_y>/',
         login_required(account.AccountDetailFrom.as_view()),
         name='accountDetailFrom'),
    
    path('account/<int:pk>/<str:currency_code>/<int:from_d>/<int:from_m>/<int:from_y>/',
         login_required(account.AccountDetailCurrencyFrom.as_view()),
         name='accountDetailCurrencyFrom'),

]
