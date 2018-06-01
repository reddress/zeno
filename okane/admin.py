from django.contrib import admin

from .models import Currency, Account, AccountType, Transaction, Budget

admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(Transaction)
admin.site.register(Budget)

