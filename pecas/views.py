from django.shortcuts import get_object_or_404, render, redirect
from .forms import PecaForm, RetiradaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Peca, Retirada

def home(request):
    return render(request, 'home.html')

#@login_required
def cadastro_peca(request):
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_peca')
    else:
        form = PecaForm()
    return render(request, 'cadastro_peca.html', {'form': form})

#@login_required
#def retirada_peca(request):
    Peca = get_object_or_404(Peca)
    if request.method == 'POST':
        form = RetiradaForm(request.POST, request.FILES)
        if Retirada.tipo == 'ENTRADA':
                Peca.quantidade += Retirada.quantidade
        elif Retirada.tipo == 'SAIDA' and Peca.quantidade >= Retirada.quantidade:
                Peca.quantidade -= Retirada.quantidade
        Peca.save()
        Retirada.save()
        return redirect('lista_peca')
    else:
        form = RetiradaForm()
#    return render(request, 'retirada_peca.html',{'form': form})

def retirada_peca(request, produto_id):
    produto = get_object_or_404(produto, id=produto_id)
    if request.method == 'POST':
        form = RetiradaForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.produto = produto
            if movimentacao.tipo == 'ENTRADA':
                produto.quantidade += movimentacao.quantidade
            elif movimentacao.tipo == 'SAIDA' and produto.quantidade >= movimentacao.quantidade:
                produto.quantidade -= movimentacao.quantidade
            produto.save()
            movimentacao.save()
            return redirect('lista_peca')
    else:
        form = RetiradaForm()
    return render(request, 'Retirada_peca.html', {'produto': produto,'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_pecas')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def ver_lista_pecas(request):
    lista_pecas = Peca.objects.all()
    return render(request, 'lista_peca.html', {'lista_pecas': lista_pecas})