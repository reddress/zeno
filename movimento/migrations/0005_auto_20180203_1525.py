# Generated by Django 2.0.1 on 2018-02-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimento', '0004_auto_20180131_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdelinha',
            name='qtde',
            field=models.IntegerField(default=0),
        ),
    ]