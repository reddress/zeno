from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import AccountType

class IndexView(TemplateView):
    template_name = "money/index.html"


# AccountType

class AccountTypeList(ListView):
    # model = AccountType  # this returns every AccountType
    template_name = "money/accounttype_list_filter.html"

    def get_queryset(self):
        return AccountType.objects.filter(owner=self.request.user)

    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        context['filter_type'] = 'all'
        return context

class AccountTypeListTime(AccountTypeList):
    template_name = "money/accounttype_list_filter.html"

    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        context['filter_type'] = 'from_to'
        
        context['from_y'] = self.kwargs['from_y']
        context['from_m'] = self.kwargs['from_m']
        context['from_d'] = self.kwargs['from_d']

        context['to_y'] = self.kwargs['to_y']
        context['to_m'] = self.kwargs['to_m']
        context['to_d'] = self.kwargs['to_d']
        return context


class AccountTypeListCurrency(AccountTypeList):
    template_name = "money/accounttype_list_filter.html"

    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        context['filter_type'] = 'currency'
        
        context['currency_code'] = self.kwargs['currency_code']
        return context


class AccountTypeListCurrencyTime(AccountTypeList):
    template_name = "money/accounttype_list_filter.html"

    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        context['filter_type'] = 'currency_from_to'
        
        context['currency_code'] = self.kwargs['currency_code']
        
        context['from_y'] = self.kwargs['from_y']
        context['from_m'] = self.kwargs['from_m']
        context['from_d'] = self.kwargs['from_d']

        context['to_y'] = self.kwargs['to_y']
        context['to_m'] = self.kwargs['to_m']
        context['to_d'] = self.kwargs['to_d']
        return context


class AccountTypeListFrom(AccountTypeList):
    template_name = "money/accounttype_list_filter.html"

    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        context['filter_type'] = 'from'
        
        context['from_y'] = self.kwargs['from_y']
        context['from_m'] = self.kwargs['from_m']
        context['from_d'] = self.kwargs['from_d']
        return context
    

class AccountTypeListCurrencyFrom(AccountTypeList):
    template_name = "money/accounttype_list_filter.html"

    def get_context_data(self, **context_kwargs):
        context = super().get_context_data(**context_kwargs)
        context['filter_type'] = 'currency_from'
        
        context['currency_code'] = self.kwargs['currency_code']
        
        context['from_y'] = self.kwargs['from_y']
        context['from_m'] = self.kwargs['from_m']
        context['from_d'] = self.kwargs['from_d']
        return context
    
    
class AccountTypeDetail(DetailView):
    # model = AccountType  # this will allow getting other users' data
    
    def get_object(self):
        return AccountType.objects.get(owner=self.request.user, pk=self.kwargs['pk'])
    

class AccountTypeCreate(CreateView):
    model = AccountType
    fields = ['name', 'equity_type']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class AccountTypeUpdate(UpdateView):
    model = AccountType
    fields = ['name', 'equity_type']

    def get_queryset(self):
        return AccountType.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])


class AccountTypeDelete(DeleteView):
    model = AccountType
    success_url = reverse_lazy('money:accountTypeList')

    def get_queryset(self):
        return AccountType.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])


class Bens(DetailView):
    template_name = "money/predefined/bens.html"
    
    def get_object(self):
        return AccountType.objects.get(owner=self.request.user, name="Bens")
    
        
class Receitas(DetailView):
    template_name = "money/predefined/receitas.html"
    
    def get_object(self):
        return AccountType.objects.get(owner=self.request.user, name="Receitas")
    
    
class Despesas(DetailView):
    template_name = "money/predefined/despesas.html"
    
    def get_object(self):
        return AccountType.objects.get(owner=self.request.user, name="Despesas")
    
    
class Credito(DetailView):
    template_name = "money/predefined/credito.html"
    
    def get_object(self):
        return AccountType.objects.get(owner=self.request.user, name="Crédito")
    
    
class Outros(DetailView):
    template_name = "money/predefined/outros.html"
    
    def get_object(self):
        return AccountType.objects.get(owner=self.request.user, name="Outros")
    
    

