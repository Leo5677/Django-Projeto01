from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from .models import *


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produto'] = Produto.objects.all()
        context['cliente'] = Cliente.objects.all()
        return context


class ContatoView(TemplateView):
    template_name = 'contato.html'


class ProdutoView(TemplateView):
    template_name = 'produto.html'

    def get_context_data(self, pk, **kwargs):
        context = super(ProdutoView, self).get_context_data(**kwargs)
        context['produto'] = Produto.objects.get(id=pk)
        return context
