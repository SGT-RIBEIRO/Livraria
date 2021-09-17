from django.contrib import admin
from .models import Cliente, Livro, Autor, Genero, Venda, Editora, ItensVenda


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone']

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['livro', 'preco', 'estoque']

#@admin.register(Livro_Autor)
#class Livro_AutorAdmin(admin.ModelAdmin):
#    list_display = ['Fk_Livro', 'Fk_Autor']

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome_autor', 'email']

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['genero', 'descricao']

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ['nome_editora', 'telefone_editora']

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['data',]

@admin.register(ItensVenda)
class ItensVendaAdmin(admin.ModelAdmin):
    list_display = ['quantidade', 'total']