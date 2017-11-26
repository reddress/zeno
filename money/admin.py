from django.contrib import admin

from . import models

admin.site.register(models.Currency)
admin.site.register(models.AccountType)
admin.site.register(models.Account)
admin.site.register(models.Budget)
admin.site.register(models.Transaction)
admin.site.register(models.Settings)
admin.site.register(models.Tag)
