from django.contrib import admin
from .models import Peca


class pecaadmin(admin.ModelAdmin):
    list_display = ('nome','valor_venda', 'quantidade_estoque')
    list_display_links = ('nome',)

admin.site.register(Peca, pecaadmin)