from django.contrib import admin
from .models import Veterinario

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'crmv', 'especialidade', 'ativo']
    list_filter = ['ativo', 'especialidade']
    search_fields = ['nome', 'crmv']