# Generated by Django 2.0.1 on 2018-01-30 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moeda',
            options={},
        ),
        migrations.RenameField(
            model_name='moeda',
            old_name='nmme',
            new_name='nome',
        ),
    ]