from rest_framework import serializers
from .models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    animal_nome = serializers.CharField(source='animal.nome', read_only=True)
    veterinario_nome = serializers.CharField(source='veterinario.nome', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Consulta
        fields = [
            'id', 'animal', 'animal_nome', 'veterinario', 'veterinario_nome',
            'data_hora', 'motivo', 'status', 'status_display', 'observacoes', 'criado_em'
        ]
        read_only_fields = ['criado_em']