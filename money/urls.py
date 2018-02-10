from django.urls import path

from .views import IndexView, AccountTypeList

app_name = 'money'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accountTypes/', AccountTypeList.as_view()),
]
