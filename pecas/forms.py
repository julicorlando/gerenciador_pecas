from django import forms
from .models import Peca, Retirada

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['nome', 'codigo_barras', 'quantidade_estoque', 'local_armazenamento']

class RetiradaForm(forms.ModelForm):
    class Meta:
        model = Retirada
        fields = ['peca', 'quantidade']
