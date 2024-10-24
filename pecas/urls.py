"""
URL configuration for gerenciador_pecas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pecas import views


urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('cadastro_peca/', views.cadastro_peca, name='cadastro_peca'),  # Cadastro de peça
    #path('retirada_peca/', views.retirada_peca, name='retirada_peca'),  # Retirada de peça
    path('retirada_peca/<int:pecas_id>', views.retirada_peca, name='retirada_peca'), #Retirada de peça
    path('login/', views.login_view, name='login'),  # Página de login
    path('home', views.home, name='home'), #Pagina inicial
    path('lista_peca/', views.ver_lista_pecas, name='lista_peca'), #lista de peças
]

