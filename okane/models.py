import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

class Currency(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name="okane_currency_owner")
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=6)
    symbol = models.CharField(max_length=6)
    hasCents = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Currencies"
        
    def __str__(self):
        return "[{}] {}".format(self.owner, self.code)

class AccountType(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name="okane_account_type_owner")
    name = models.CharField(max_length=80)
    sign = models.IntegerField()  # -1 = Equity type

    def __str__(self):
        return "[{}] {}".format(self.owner, self.name)

class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name="okane_account_owner")
    accountType = models.ForeignKey(AccountType, on_delete=models.CASCADE, related_name="okane_account_owner")
    name = models.CharField(max_length=100)

    def __str__(self):
        return "[{}] {}".format(self.owner, self.name)

class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name="okane_transaction_owner")
    name = models.CharField(max_length=160)
    currency = models.ForeignKey(Currency, on_delete=CASCADE)
    amount = models.IntegerField()
    debit = models.ForeignKey(Account, on_delete=CASCADE, related_name="debit_transactions")
    credit = models.ForeignKey(Account, on_delete=CASCADE, related_name="credit_transactions")
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return "[{}] {} {} {} {}".format(self.owner, self.date, self.amount, self.currency, self.name)

class Budget(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE, related_name="okane_budget_owner")
    account = models.ForeignKey(Account, on_delete=CASCADE, related_name="okane_budget_account")
    currency = models.ForeignKey(Account, on_delete=CASCADE, related_name="okane_budget_currency")
    amount = models.IntegerField()

    def __str__(self):
        return "[{}] {} {} {}".format(self.owner, self.account, self.amount, self.currency)
        





