from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import AccountType

class IndexView(TemplateView):
    template_name = "money/index.html"


# AccountType

class AccountTypeList(ListView):
    # model = AccountType  # this returns every AccountType

    def get_queryset(self):
        return AccountType.objects.filter(owner=self.request.user)


class AccountTypeDetail(DetailView):
    # model = AccountType  # this will allow getting other users' data
    
    def get_queryset(self):
        return AccountType.objects.filter(owner=self.request.user, pk=self.kwargs['pk'])
    

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
