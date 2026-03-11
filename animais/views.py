from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Animal
from .serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.select_related('tutor').all()
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['especie', 'tutor']
    search_fields = ['nome', 'raca']
