from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import AccountType

class IndexView(TemplateView):
    template_name = "money/index.html"

@method_decorator(login_required, name='dispatch')
class AccountTypeList(ListView):
    # model = AccountType  # this returns every AccountType

    def get_queryset(self):
        return AccountType.objects.filter(owner=self.request.user)

    
