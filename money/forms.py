from django.forms import ModelForm

from .models import Account, Transaction

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ('account_type', 'name', 'abbreviation')

        
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ('name', 'currency', 'amount', 'debit', 'credit', 'when')
