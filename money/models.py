from decimal import Decimal

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Currency
# AccountType
# Account
# Budget
# Transaction
# Settings (default currency, get first if this is not set)
# AccountTag (for grouping accounts, do mytags first)

class Currency(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)  # New Taiwan Dollar
    code = models.CharField(max_length=6)   # TWD
    symbol = models.CharField(max_length=6) # NT$
    show_cents = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['owner', 'code']
        verbose_name_plural = "Currencies"

    def __str__(self):
        return "{}'s {}".format(self.owner, self.code)

        
class AccountType(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    equity_type = models.BooleanField(default=False)

    class Meta:
        ordering = ['owner', 'name']

    def get_absolute_url(self):
        return reverse('money:accountTypeDetail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return "{}'s {}".format(self.owner, self.name)


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)

    class Meta:
        ordering = ['owner', 'name']
        
    def __str__(self):
        return "{}'s {}".format(self.owner, self.name)


class Budget(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

    class Meta:
        ordering = ['owner', 'account']
        
    def __str__(self):
        return "{}'s budget for {}: {}".format(self.owner, self.account, self.amount)

    
class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    debit = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="debit_transactions")
    credit = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="credit_transactions")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    when = models.DateTimeField()

    class Meta:
        ordering = ['owner', 'when']
    
    def __str__(self):
        display_str = "{}'s {} on {}: {} {}"
        return display_str.format(self.owner, self.name,
                                  self.occurred.strftime("%d/%m/%y"),
                                  self.currency.symbol, self.amount)

    
class Tag(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    accounts = models.ManyToManyField(Account)

    class Meta:
        ordering = ['owner', 'name']
        
    def __str__(self):
        return "{}'s {}".format(self.owner, self.name)

    
class Settings(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    default_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}'s settings".format(self.owner)
    
    class Meta:
        ordering = ['owner']
        verbose_name_plural = "Settings"
