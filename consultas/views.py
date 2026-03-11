from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.select_related('animal', 'veterinario').all()
    serializer_class = ConsultaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'veterinario', 'animal']
    search_fields = ['motivo', 'animal__nome', 'veterinario__nome']
    ordering_fields = ['data_hora', 'criado_em']