from decimal import Decimal

from django.db import models
from django.db.models import Max, Min
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import localtime

# Currency
# Settings
# AccountType
# Account
# Budget
# Transaction
# AccountTag (for grouping accounts)

class Currency(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)  # New Taiwan Dollar
    code = models.CharField(max_length=6)   # TWD
    symbol = models.CharField(max_length=6) # NT$
    show_cents = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['owner', 'code']
        unique_together = ('owner', 'code')
        verbose_name_plural = "Currencies"

    def __str__(self):
        # return "{}'s {}".format(self.owner, self.code)
        return "{} [{}]".format(self.code, self.owner)

        
class Settings(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    default_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}'s settings".format(self.owner)
    
    class Meta:
        ordering = ['owner']
        verbose_name_plural = "Settings"


class AccountType(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    equity_type = models.BooleanField(default=False)

    class Meta:
        ordering = ['owner', 'name']

    def get_absolute_url(self):
        return reverse('money:accountTypeDetail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return "{} [{}]".format(self.name, self.owner)


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)

    class Meta:
        ordering = ['owner', 'name']

    def balance(self, currency_code=None, from_when=None, to_when=None):
        if currency_code is None:
            currency = Settings.objects.get(owner=self.owner).default_currency
        else:
            currency = Currency.objects.get(owner=self.owner, code=currency_code)
            
        debit_transactions = self.debit_transactions.filter(owner=self.owner, currency=currency)
        credit_transactions = self.credit_transactions.filter(owner=self.owner, currency=currency)
        
        if from_when is None:
            from_when = (debit_transactions | credit_transactions).aggregate(Min('when'))['when__min']
            
        if to_when is None:
            to_when = (debit_transactions | credit_transactions).aggregate(Max('when'))['when__max']

        total = Decimal('0.00')
        
        if debit_transactions:
            debit_in_timeframe = debit_transactions.filter(when__gte=from_when, when__lte=to_when)
        
            for debit in debit_in_timeframe:
                if self.account_type.equity_type:
                    total -= debit.amount
                else:
                    total += debit.amount

        if credit_transactions:
            credit_in_timeframe = credit_transactions.filter(when__gte=from_when, when__lte=to_when)

            for credit in credit_in_timeframe:
                if self.account_type.equity_type:
                    total += credit.amount
                else:
                    total -= credit.amount
                
        return total

    
    def get_absolute_url(self):
        return reverse('money:accountDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{} [{}]".format(self.abbreviation, self.owner)


class Budget(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

    class Meta:
        ordering = ['owner', 'account']
        
    def __str__(self):
        return "{} budget: {} {} [{}]".format(self.account.abbreviation, self.currency.code, self.amount, self.owner)

    
class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    debit = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="debit_transactions")
    credit = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="credit_transactions")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    when = models.DateTimeField()

    class Meta:
        ordering = ['owner', '-when']
    
    def get_absolute_url(self):
        return reverse('money:transactionDetail', kwargs={'pk': self.pk})

    def __str__(self):
        display_str = "{}: {} {} {} {}/{} [{}]"
        return display_str.format(localtime(self.when).strftime("%d/%m/%y %H:%M:%S"),
                                  self.name,
                                  self.currency.symbol, self.amount,
                                  self.debit.abbreviation,
                                  self.credit.abbreviation,
                                  self.owner)

    
class Tag(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    accounts = models.ManyToManyField(Account)

    class Meta:
        ordering = ['owner', 'name']
        
    def __str__(self):
        return "{} [{}]".format(self.name, self.owner)

