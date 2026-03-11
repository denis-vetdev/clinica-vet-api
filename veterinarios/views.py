from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Veterinario
from .serializers import VeterinarioSerializer

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['ativo', 'especialidade']
    search_fields = ['nome', 'crmv']