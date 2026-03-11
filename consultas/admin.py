from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['animal', 'veterinario', 'data_hora', 'status']
    list_filter = ['status']
    search_fields = ['animal__nome', 'veterinario__nome']