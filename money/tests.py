from decimal import Decimal
from datetime import datetime
import pytz

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Currency, AccountType, Account, Transaction, Settings

class TransactionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="u", email="u@u.com", password="u")
        cls.usd = Currency.objects.create(owner=cls.user, name="usd", code="usd", symbol="$")
        cls.settings = Settings.objects.create(owner=cls.user, default_currency=cls.usd)
        cls.income = AccountType.objects.create(owner=cls.user, name="Income", equity_type=True)
        cls.assets = AccountType.objects.create(owner=cls.user, name="Assets", equity_type=False)
        cls.expenses = AccountType.objects.create(owner=cls.user, name="Expenses", equity_type=False)
        cls.salary = Account.objects.create(owner=cls.user, account_type=cls.income, name="Salary", abbreviation="sal")
        cls.wallet = Account.objects.create(owner=cls.user, account_type=cls.assets, name="Wallet", abbreviation="wal")
        cls.food = Account.objects.create(owner=cls.user, account_type=cls.expenses, name="Food", abbreviation="food")

    def createTransaction(self, debit, credit, amount):
        return Transaction.objects.create(owner=self.user, debit=debit, credit=credit, currency=self.usd, name="dummy", amount=Decimal(amount), when=datetime.now().replace(tzinfo=pytz.UTC))
    
    def testSingleTransactionBalance(self):
        amount = "100.00"
        self.createTransaction(self.wallet, self.salary, amount).save()
        
        self.assertEquals(self.salary.balance(), Decimal("100.00"))
        self.assertEquals(self.wallet.balance(), Decimal("100.00"))

    def testMultipleTransactionsBalance(self):
        self.createTransaction(self.wallet, self.salary, "1000.00").save()
        self.createTransaction(self.wallet, self.salary, "1000.00").save()
        self.createTransaction(self.food, self.wallet, "200.00").save()

        self.assertEquals(self.wallet.balance(), Decimal("1800.00"))
        self.assertEquals(self.food.balance(), Decimal("200.00"))
        self.assertEquals(self.salary.balance(), Decimal("2000.00"))
