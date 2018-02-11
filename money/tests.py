from decimal import Decimal
from datetime import datetime

from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Currency, AccountType, Account, Transaction, Settings

def dt(year, month, day):
    return datetime(year, month, day).replace(tzinfo=timezone.get_default_timezone())

class TransactionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="u")
        cls.usd = Currency.objects.create(owner=cls.user, name="usd", code="USD", symbol="$")
        cls.brl = Currency.objects.create(owner=cls.user, name="brl", code="BRL", symbol="R$")
        cls.settings = Settings.objects.create(owner=cls.user, default_currency=cls.usd)
        cls.income = AccountType.objects.create(owner=cls.user, name="Income", equity_type=True)
        cls.assets = AccountType.objects.create(owner=cls.user, name="Assets", equity_type=False)
        cls.expenses = AccountType.objects.create(owner=cls.user, name="Expenses", equity_type=False)
        cls.salary = Account.objects.create(owner=cls.user, account_type=cls.income, name="Salary", abbreviation="sal")
        cls.wallet = Account.objects.create(owner=cls.user, account_type=cls.assets, name="Wallet", abbreviation="wal")
        cls.food = Account.objects.create(owner=cls.user, account_type=cls.expenses, name="Food", abbreviation="food")
        
        # scheduled transactions
        cls.schedSal = Account.objects.create(owner=cls.user, account_type=cls.income, name="Sched. Salary", abbreviation="schedsal")
        cls.bank = Account.objects.create(owner=cls.user, account_type=cls.assets, name="Bank", abbreviation="bank")
        
        cls.jan01 = Transaction.objects.create(owner=cls.user, debit=cls.bank, credit=cls.schedSal, name="Jan. salary", currency=cls.brl, amount=Decimal("2000.00"), when=dt(2017, 1, 1))
        cls.feb01 = Transaction.objects.create(owner=cls.user, debit=cls.bank, credit=cls.schedSal, name="Feb. salary", currency=cls.brl, amount=Decimal("2000.00"), when=dt(2017, 2, 1))
        cls.mar01 = Transaction.objects.create(owner=cls.user, debit=cls.bank, credit=cls.schedSal, name="Mar. salary", currency=cls.brl, amount=Decimal("2000.00"), when=dt(2017, 3, 1))

        cls.usdjan = Transaction.objects.create(owner=cls.user, debit=cls.bank, credit=cls.schedSal, name="USD Jan.", currency=cls.usd, amount=Decimal("500.00"), when=dt(2017, 1, 1))
        cls.usdfeb = Transaction.objects.create(owner=cls.user, debit=cls.bank, credit=cls.schedSal, name="USD Feb.", currency=cls.usd, amount=Decimal("500.00"), when=dt(2017, 2, 1))
        cls.usdmar = Transaction.objects.create(owner=cls.user, debit=cls.bank, credit=cls.schedSal, name="USD Mar.", currency=cls.usd, amount=Decimal("500.00"), when=dt(2017, 3, 1))

    def setUp(self):
        self.user.set_password('u')
        self.user.save()
        self.client.login(username='u', password='u')
        
    def createTransaction(self, debit, credit, amount):
        return Transaction.objects.create(owner=self.user, debit=debit, credit=credit, currency=self.usd, name="dummy", amount=Decimal(amount), when=datetime.now().replace(tzinfo=timezone.get_default_timezone()))
    
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

    def testAccountTypeFromAndTo(self):
        # from and to dates
        r = self.client.get('/money/accountType/2016/4/6/2017/9/15/')
        self.assertContains(r, "TEST schedsal [u]\n\n1500.00")

        r = self.client.get('/money/accountType/2017/1/1/2017/9/9/')
        self.assertContains(r, "TEST schedsal [u]\n\n1500.00")

        r = self.client.get('/money/accountType/2017/1/1/2017/2/1/')
        self.assertContains(r, "TEST schedsal [u]\n\n1000.00")
        
        r = self.client.get('/money/accountType/2017/1/1/2017/1/15/')
        self.assertContains(r, "TEST schedsal [u]\n\n500.00")

        
    def testAccountTypeCurrencyFromAndTo(self):
        # currency and from and to dates
        r = self.client.get('/money/accountType/BRL/2016/5/6/2017/10/11/')
        self.assertContains(r, "TEST schedsal [u]\n\n6000.00")
