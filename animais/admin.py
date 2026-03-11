from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'especie', 'raca', 'tutor', 'nascimento']
    list_filter = ['especie']
    search_fields = ['nome', 'tutor__nome']