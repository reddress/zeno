from datetime import datetime, timedelta

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.timezone import make_aware

from ..models import AccountType, Account, Transaction, Currency
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


class AccountDetailTime(AccountDetail):
    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        from_y = self.kwargs['from_y']
        from_m = self.kwargs['from_m']
        from_d = self.kwargs['from_d']

        to_y = self.kwargs['to_y']
        to_m = self.kwargs['to_m']
        to_d = self.kwargs['to_d']

        from_date = make_aware(datetime(from_y, from_m, from_d))
        to_date = make_aware(datetime(to_y, to_m, to_d) + timedelta(days=1))
         
        transactions = (Transaction.objects.filter(debit=self.object, when__gte=from_date, when__lt=to_date) |
                        Transaction.objects.filter(credit=self.object, when__gte=from_date, when__lt=to_date))
        
        context['transactions'] = transactions
        return context

    
class AccountDetailCurrency(AccountDetail):
    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        currency_code = self.kwargs['currency_code']
        currency = Currency.objects.get(owner=self.request.user, code=currency_code)
        
        transactions = (Transaction.objects.filter(debit=self.object, currency=currency) |
                        Transaction.objects.filter(credit=self.object, currency=currency))
        context['transactions'] = transactions
        return context

    
class AccountDetailCurrencyTime(AccountDetail):
    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        from_y = self.kwargs['from_y']
        from_m = self.kwargs['from_m']
        from_d = self.kwargs['from_d']

        to_y = self.kwargs['to_y']
        to_m = self.kwargs['to_m']
        to_d = self.kwargs['to_d']

        from_date = make_aware(datetime(from_y, from_m, from_d))
        to_date = make_aware(datetime(to_y, to_m, to_d) + timedelta(days=1))

        currency_code = self.kwargs['currency_code']
        currency = Currency.objects.get(owner=self.request.user, code=currency_code)
        
        transactions = (Transaction.objects.filter(debit=self.object, when__gte=from_date, when__lt=to_date,
                                                   currency=currency) |
                        Transaction.objects.filter(credit=self.object, when__gte=from_date, when__lt=to_date,
                                                   currency=currency))
        context['transactions'] = transactions
        return context

    
class AccountDetailFrom(AccountDetail):
    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        from_y = self.kwargs['from_y']
        from_m = self.kwargs['from_m']
        from_d = self.kwargs['from_d']

        from_date = make_aware(datetime(from_y, from_m, from_d))

        transactions = (Transaction.objects.filter(debit=self.object, when__gte=from_date) |
                        Transaction.objects.filter(credit=self.object, when__gte=from_date))
        context['transactions'] = transactions
        return context
    
    
class AccountDetailCurrencyFrom(AccountDetail):
    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        from_y = self.kwargs['from_y']
        from_m = self.kwargs['from_m']
        from_d = self.kwargs['from_d']

        from_date = make_aware(datetime(from_y, from_m, from_d))

        currency_code = self.kwargs['currency_code']
        currency = Currency.objects.get(owner=self.request.user, code=currency_code)

        transactions = (Transaction.objects.filter(debit=self.object, when__gte=from_date, currency=currency) |
                        Transaction.objects.filter(credit=self.object, when__gte=from_date, currency=currency))
        context['transactions'] = transactions
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
