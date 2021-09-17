from urllib import request
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic import FormView, DetailView, ListView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Livro


# Create your views here.

class IndexView(ListView):
    model = Livro
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        search = self.request.GET.get('search')
        option = self.request.GET.get('options')
        if search:
            if option == 'Título':
                queryset = queryset.filter(livro__icontains=search)
            elif option == 'Gênero':
                queryset = queryset.filter(Fk_Genero__genero__icontains=search)
            else:
                queryset = queryset.filter(Fk_Autor__nome_autor__icontains=search)
        return queryset

class paginaEmConstrucaoView(TemplateView):
    template_name = 'paginaEmConstrucao.html'