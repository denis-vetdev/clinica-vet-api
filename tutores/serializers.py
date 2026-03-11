from rest_framework import serializers
from .models import Tutor

class TutorSerializer(serializers.ModelSerializer):
    total_animais = serializers.IntegerField(source='animais.count', read_only=True)

    class Meta:
        model = Tutor
        fields = ['id', 'nome', 'cpf', 'telefone', 'email', 'total_animais', 'criado_em']
        read_only_fields = ['criado_em']