from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import Account

# Account
    
class AccountList(ListView):
    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class AccountDetail(DetailView):
    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])
    

class AccountCreate(CreateView):
    model = Account
    fields = ['account_type', 'name', 'abbreviation']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class AccountUpdate(UpdateView):
    model = Account
    fields = ['account_type', 'name', 'abbreviation']

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])


class AccountDelete(DeleteView):
    model = Account
    success_url = reverse_lazy('money:accountList')

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])
