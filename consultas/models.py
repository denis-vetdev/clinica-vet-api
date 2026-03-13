from django.db import models
from animais.models import Animal
from veterinarios.models import Veterinario

class Consulta(models.Model):
    STATUS = [
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='consultas')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='consultas')
    data_hora = models.DateTimeField()
    motivo = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='agendada')
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.animal.nome} - {self.data_hora.strftime("%d/%m/%Y %H:%M")}'
    
    class Meta:
        ordering = ['-data_hora']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'