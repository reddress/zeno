from django.db import models
from django.db.models import Model
from django.db.models import CharField
from django.db.models import ForeignKey, CASCADE, SET_NULL

from registros.models import Produto


class MenuPasta(Model):
    nome = CharField(max_length=79)

    class Meta:
        ordering = ['nome']
        
    def __str__(self):
        return self.nome
        

class Lista(Model):
    nome = CharField(max_length=79)

    class Meta:
        ordering = ['nome']
        
    def __str__(self):
        return self.nome


class MenuItem(Model):
    nome = CharField(max_length=79)
    lista = ForeignKey(Lista, on_delete=CASCADE)
    pasta = ForeignKey(MenuPasta, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = "Menu itens"
        ordering = ['nome']        
        
    def __str__(self):
        return self.nome
        

class Item(Model):
    produto = models.OneToOneField(Produto, on_delete=CASCADE)
    listas = models.ManyToManyField(Lista, blank=True)
    
    class Meta:
        verbose_name_plural = "Itens"
        ordering = ["produto__codigo"]
        
    def __str__(self):
        return "[{}] {}".format(self.produto.codigo, self.produto.nome)

