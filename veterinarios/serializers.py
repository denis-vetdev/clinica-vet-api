from rest_framework import serializers
from .models import Veterinario

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = ['id', 'nome', 'crmv', 'especialidade', 'telefone', 'email', 'ativo']