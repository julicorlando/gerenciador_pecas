from django.contrib import admin
from .models import Peca


class pecaadmin(admin.ModelAdmin):
    list_display = ('nome','codigo_barras', 'quantidade_estoque', 'local_armazenamento')
    list_display_links = ('nome', 'local_armazenamento')

admin.site.register(Peca, pecaadmin)