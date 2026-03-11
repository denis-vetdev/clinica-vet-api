from django.contrib import admin
from .models import Tutor

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone', 'email', 'criado_em']
    search_fields = ['nome', 'cpf', 'email']
