from django.db import models
from django.contrib.auth.models import User

class Peca(models.Model):
    nome = models.CharField(max_length=100)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    local_armazenamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Retirada(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_vendido = models.DecimalField(max_digits=10, decimal_places=2)
    data_retirada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.peca} - {self.usuario}"

# Usuario já é definido no Django via o model User da autenticação padrão
