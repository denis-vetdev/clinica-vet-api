from django.db import models

class Veterinario(models.Model):
    nome = models.CharField(max_length=100)
    crmv = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} - CRMV {self.crmv}'
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Veterinário'
        verbose_name_plural = 'Veterinários'


