from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import AccountType, Account, Transaction
from ..forms import AccountForm

# Account
    
class AccountList(ListView):
    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class AccountDetail(DetailView):
    def get_object(self):
        return Account.objects.get(owner=self.request.user, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(debit=self.object) | Transaction.objects.filter(credit=self.object)
        return context
    

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
