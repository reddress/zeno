# Generated by Django 2.0.1 on 2018-02-07 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registros', '0010_auto_20180207_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registros.Produto')),
            ],
            options={
                'verbose_name_plural': 'Itens',
            },
        ),
    ]
