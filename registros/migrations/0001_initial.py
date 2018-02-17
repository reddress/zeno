# Generated by Django 2.0.1 on 2018-01-30 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Configurações',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('rua', models.CharField(blank=True, max_length=255)),
                ('cidade', models.CharField(blank=True, max_length=63)),
                ('estado', models.CharField(blank=True, max_length=63)),
                ('cep', models.CharField(blank=True, max_length=15)),
                ('pais', models.CharField(blank=True, max_length=31)),
                ('telefone', models.CharField(blank=True, max_length=31)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('cadastro_nacional', models.CharField(blank=True, max_length=35)),
                ('cadastro_estadual', models.CharField(blank=True, max_length=35)),
                ('cadastro_municipal', models.CharField(blank=True, max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empregador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registros.Empresa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Moeda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmme', models.CharField(max_length=63)),
                ('codigo', models.CharField(max_length=6)),
                ('mostrar_centavos', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=63)),
                ('nome', models.CharField(max_length=127)),
                ('por_caixa', models.IntegerField(default=1)),
                ('foto', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registros.Funcionario'),
        ),
        migrations.AddField(
            model_name='configuracao',
            name='empresa_ativa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registros.Empresa'),
        ),
    ]