from django.db import models
from stdimage.models import StdImageField
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    telefone = models.CharField('Telefone', max_length=15)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome_editora = models.CharField('Nome da editora', max_length=50)
    telefone_editora = models.CharField('Telefone da editora', max_length=15)

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

    def __str__(self):
        return self.nome_editora


class Genero(models.Model):
    genero = models.CharField('Genero', max_length=50)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.genero


class Autor(models.Model):
    nome_autor = models.CharField('Nome do autor', max_length=50)
    email = models.EmailField('Email')


    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome_autor


class Livro(models.Model):
    livro = models.CharField('Livro', max_length=50)
    preco = models.FloatField('Preço')
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='Livros', variations={'thumb': {'width': 416, 'height': 416, 'crop': False}})
    Fk_Genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    Fk_Editora = models.ForeignKey('Editora', on_delete=models.CASCADE)
    Fk_Autor = models.ManyToManyField('Autor')
    #Fk_Autor = models.ManyToManyField('Autor', through='Livro_Autor')

    class Meta:
        verbose_name = 'livro'
        verbose_name_plural = 'livros'
        ordering = ['livro']

    def __str__(self):
        return self.livro


class Venda(models.Model):
    data = models.DateField('Data', auto_now_add=True)
    Fk_Cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    Fk_ItensVenda = models.ManyToManyField('Livro', through='ItensVenda')


    class Meta:
        verbose_name = f'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return self.Fk_Cliente.nome #precisa retornar uma string!! Verificar depois


class ItensVenda(models.Model):
    Fk_Venda = models.ForeignKey('Venda', on_delete=models.CASCADE)
    Fk_Livro = models.ForeignKey('Livro', on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')
    total = models.FloatField('Total')



'''
class Livro_Autor(models.Model):
    Fk_Livro = models.ForeignKey('Livro', on_delete=models.CASCADE)
    Fk_Autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
'''