from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    tutor_nome = serializers.CharField(source='tutor.nome', read_only=True)
    especie_display = serializers.CharField(source='get_especie_display', read_only=True)

    class Meta:
        model = Animal
        fields = ['id', 'nome', 'especie', 'especie_display', 'raca', 'nascimento', 'tutor', 'tutor_nome', 'criado_em']
        read_only_fields = ['criado_em']