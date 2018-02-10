from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import AccountType, Account, Transaction, Currency, Settings
from ..forms import TransactionForm

# Transaction
    
class TransactionList(ListView):
    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)


class TransactionDetail(DetailView):
    def get_object(self):
        return Transaction.objects.get(owner=self.request.user, pk=self.kwargs['pk'])
    

class TransactionCreate(CreateView):
    form_class = TransactionForm
    template_name = "money/transaction_form.html"

    def get_form(self):
        form = super().get_form()
        form.fields['currency'].queryset = Currency.objects.filter(owner=self.request.user)            
        form.fields['debit'].queryset = Account.objects.filter(owner=self.request.user)
        form.fields['credit'].queryset = Account.objects.filter(owner=self.request.user)
        form.initial['currency'] = Settings.objects.get(owner=self.request.user).default_currency.id
        form.initial['when'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return form
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TransactionUpdate(UpdateView):
    form_class = TransactionForm
    template_name = "money/transaction_form.html"

    def get_form(self):
        form = super().get_form()
        form.fields['currency'].queryset = Currency.objects.filter(owner=self.request.user)            
        form.fields['debit'].queryset = Account.objects.filter(owner=self.request.user)
        form.fields['credit'].queryset = Account.objects.filter(owner=self.request.user)
        return form
    
    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TransactionDelete(DeleteView):
    model = Transaction
    success_url = reverse_lazy('money:transactionList')

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])
