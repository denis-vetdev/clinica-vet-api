from django.db import models
from tutores.models import Tutor

class Animal(models.Model):
    ESPECIES = [
        ('cao', 'Cão'),
        ('gato', 'Gato'),
        ('ave', 'Ave'),
        ('roedor', 'Roedor'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=ESPECIES)
    raca = models.CharField(max_length=50, blank=True)
    nascimento = models.DateField()
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='animais')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} ({self.get_especie_display()})'
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'