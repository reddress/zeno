from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import AccountType, Account
from ..forms import AccountForm

# Account
    
class AccountList(ListView):
    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class AccountDetail(DetailView):
    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])
    

class AccountCreate(CreateView):
    form_class = AccountForm
    template_name = "money/account_form.html"

    def get_form(self):
        form = super().get_form()
        form.fields['account_type'].queryset = AccountType.objects.filter(owner=self.request.user)
        return form
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class AccountUpdate(UpdateView):
    form_class = AccountForm
    template_name = "money/account_form.html"

    def get_form(self):
        form = super().get_form()
        form.fields['account_type'].queryset = AccountType.objects.filter(owner=self.request.user)
        return form

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AccountDelete(DeleteView):
    model = Account
    success_url = reverse_lazy('money:accountList')

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])
