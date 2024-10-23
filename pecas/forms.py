from django import forms
from .models import Peca, Retirada

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome', 'valor_compra', 'valor_venda', 'quantidade_estoque', 'local_armazenamento']

class RetiradaForm(forms.ModelForm):
    class Meta:
        model = Retirada
        fields = ['peca', 'quantidade', 'valor_vendido']
