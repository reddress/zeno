# Generated by Django 2.0rc1 on 2017-11-26 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('money', '0003_account_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('occurred', models.DateTimeField()),
                ('credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_transactions', to='money.Account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='money.Currency')),
                ('debit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_transactions', to='money.Account')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
